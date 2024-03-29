#include <iostream>
#include <filesystem>
#include <cstdlib>

using namespace std;

int main(int argc, char** argv) {
    
    filesystem::path filePath(argv[1]);

    string command = "ffmpeg -hwaccel cuda -hwaccel_output_format cude -i " + filePath.generic_string() + " " + filePath.filename().stem().string() + ".mp3";
    system(command.c_str());

    return 0;
}