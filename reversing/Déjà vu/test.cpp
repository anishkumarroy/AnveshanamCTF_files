#include <iostream>
#include <string>

std::string reverseTransform(const std::string& input) {
    std::string result = input;
    for (char& ch : result) {
        if (ch >= 'A' && ch <= 'Z') {
            ch = -0x65 - ch;
        } else if (ch >= 'a' && ch <= 'z') {
            ch = -0x25 - ch;
        }
    }
    return result;
}

int main() {
    std::string target = "RRGQznnfCWiWl";
    std::string password = reverseTransform(target);
    std::cout << "The actual password is: " << password << std::endl;
    return 0;
}
