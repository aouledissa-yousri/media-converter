#include <iostream>
#include <filesystem>
#include <cstdlib>

using namespace std;

int main(int argc, char** argv) {
    
    filesystem::path filePath(argv[1]);

    string command = "convert " + filePath.generic_string() + " " + filePath.filename().stem().string() + ".jpg";
    system(command.c_str());

    return 0;
}