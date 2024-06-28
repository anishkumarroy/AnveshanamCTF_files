# Stage 1: Use the original image and extract the file from the specific layer
FROM cyberseciitjammu/sandwich:latest as intermediate

# Revert the change from the last layer to restore the deleted file
COPY --from=sha256:4afdd2a6a555620d9f6a931c714d93cd1c8e28ec503a8e4222a37f1d62600ace /data.txt /data.txt

# Stage 2: Create the final image with the restored file
FROM cyberseciitjammu/sandwich:latest
COPY --from=intermediate /data.txt /recovered_data.txt
