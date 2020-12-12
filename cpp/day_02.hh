#pragma once
#import "solvers.hh"
#import "utils.hh"
#import <regex>

class Solver2 : public Solver {
    struct Entry {
        int min, max;
        char letter;
        std::string string;
    };
    std::vector<Entry> entries;
public:
    inline Solver2(const std::vector<std::string> &input)
    {
        std::regex pattern("^(\\d+)-(\\d+) +(\\w): +(\\w+)$");

        std::transform(input.begin(), input.end(), std::back_inserter(entries),
            [&](const auto &line) {
                std::smatch match;
                std::regex_match(line, match, pattern);
                return Entry {
                    .min = std::stoi(match[1]),
                    .max = std::stoi(match[2]),
                    .letter = match[3].str()[0],
                    .string = match[4]
                };
            });
    }

    inline long part1() {
        size_t count = 0;
        for (const auto &entry : entries) {
            size_t letterCount = count_char(entry.string.c_str(), entry.letter);
            if (letterCount >= entry.min && letterCount <= entry.max)
                ++count;
        }
        return count;
    }

    inline long part2() {
        size_t count = 0;
        for (const auto &entry : entries) {
            bool one = (entry.string[entry.min - 1] == entry.letter);
            bool two = (entry.string[entry.max - 1] == entry.letter);
            if (one != two)
                ++count;
        }
        return count;
    }

    size_t count_char(const char *curr, char letter)
    {
        size_t count = 0;
        while (*curr != '\0') {
            if (*curr == letter) ++count;
            ++curr;
        }
        return count;
    }
};
