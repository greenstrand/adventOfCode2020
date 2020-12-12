#pragma once

#import <iostream>
#import <memory>
#import <vector>

class Solver {
  public:
    virtual long part1() = 0;
    virtual long part2() = 0;

    static std::shared_ptr<Solver>
    Create(int day, const std::vector<std::string> &input);
};
