#include <iostream>
#include <filesystem>
#include <cstdlib>

using namespace std;

int main(int argc, char** argv) {
    
    filesystem::path filePath(argv[1]);
    string extension = argv[2];

    string command = "ffmpeg -i " + filePath.generic_string() + " " + filePath.filename().stem().string() + "." + extension;
    system(command.c_str());

    return 0;
}