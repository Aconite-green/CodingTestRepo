#include <string>
#include <vector>
#include <map>
using namespace std;

int solution(string s) {
    map<string, int> wordToNumber = {
        {"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
        {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
        {"eight", 8}, {"nine", 9}
    };

    for (auto &word : wordToNumber) {
        size_t pos = s.find(word.first);
        while (pos != string::npos) {
            s.replace(pos, word.first.length(), to_string(word.second));
            pos = s.find(word.first, pos + 1);
        }
    }

    return stoi(s);
}