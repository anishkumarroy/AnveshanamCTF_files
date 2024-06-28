import struct
import datetime

def read_info2(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    header_size = 16
    offset = header_size
    records = []

    while offset < len(data):
        # Read index (4 bytes)
        index = struct.unpack_from('<I', data, offset)[0]
        offset += 4

        # Read path length (4 bytes)
        path_length = struct.unpack_from('<I', data, offset)[0]
        offset += 4

        # Read the original path (variable length, null-terminated UTF-16LE string)
        path_end = data.find(b'\x00\x00', offset)
        if path_end == -1:
            break
        path = data[offset:path_end + 2].decode('utf-16le').strip('\x00')
        offset = path_end + 2

        # Skip to the deletion time
        offset = header_size + 4 + path_length + 272

        # Read deletion time (8 bytes, FILETIME format)
        deletion_time = struct.unpack_from('<Q', data, offset)[0]
        offset += 8

        # Read file size (8 bytes)
        file_size = struct.unpack_from('<Q', data, offset)[0]
        offset += 8

        records.append({
            'index': index,
            'path_length': path_length,
            'path': path,
            'file_size': file_size,
            'deletion_time': deletion_time,
        })

    return records

def filetime_to_datetime(filetime):
    FILETIME_EPOCH = datetime.datetime(1601, 1, 1, 0, 0, 0)
    return FILETIME_EPOCH + datetime.timedelta(microseconds=filetime / 10)

info2_path = "INFO2"  # Replace with your INFO2 file path
records = read_info2(info2_path)

for record in records:
    deletion_datetime = filetime_to_datetime(record['deletion_time'])
    print(f"File: {record['path']}")
    print(f"Deleted at: {deletion_datetime}")

# Look for the specific file you're interested in
for record in records:
    if 'flag.txt.rar' in record['path']:
        deletion_datetime = filetime_to_datetime(record['deletion_time'])
        print(f"flag.txt.rar was deleted at: {deletion_datetime}")
