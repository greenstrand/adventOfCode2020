#pragma once
#import "solvers.hh"
#import "utils.hh"

class Solver1 : public Solver {
  const int SUM = 2020;
  std::vector<long> nums;

 public:
  inline Solver1(const std::vector<std::string> &input) {
    std::transform(input.begin(), input.end(), std::back_inserter(nums),
                   [](const auto &line) { return std::stol(line); });
  }

  inline long part1() {
    auto it = combo_iterator<2>(nums.size());
    do {
      if (nums[it[0]] + nums[it[1]] == SUM) {
        return nums[it[0]] * nums[it[1]];
      }
    } while (it.next());

    return -1;
  }

  inline long part2() {
    auto it = combo_iterator<3>(nums.size());
    do {
      if (nums[it[0]] + nums[it[1]] + nums[it[2]] == SUM) {
        return nums[it[0]] * nums[it[1]] * nums[it[2]];
      }
    } while (it.next());

    return -1;
  }
};
