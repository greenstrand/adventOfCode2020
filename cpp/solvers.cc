#import "solvers.hh"

#import "day_01.hh"
#import "day_02.hh"

std::shared_ptr<Solver> Solver::Create(int day,
                                       const std::vector<std::string> &input) {
  switch (day) {
    case 1:
      return std::make_shared<Solver1>(input);
    case 2:
      return std::make_shared<Solver2>(input);
    default:
      throw std::runtime_error("Day " + std::to_string(day) +
                               " not yet implemented.");
  }
}
