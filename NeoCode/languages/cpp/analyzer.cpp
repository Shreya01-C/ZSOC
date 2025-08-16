#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char* argv[]) {
    ifstream file(argv[1]);
    string line;
    int line_num = 0;
    while (getline(file, line)) {
        if (line.find("NULL") != string::npos) {
            cout << "Line " << line_num << ": Use nullptr instead of NULL" << endl;
        }
        line_num++;
    }
    return 0;
}