#import <boost/algorithm/string.hpp>
#import <boost/filesystem.hpp>
#import <cstdio>
#import <fstream>
#import <iostream>
#import <vector>

#import "solvers.hh"

using boost::filesystem::path;

std::vector<std::string> get_lines(const std::string &path) {
  std::ifstream infile(path);
  if (!infile.good()) {
    throw std::runtime_error("Could not find file: " + path);
  }

  std::vector<std::string> results;
  std::string line;
  while (std::getline(infile, line)) {
    boost::algorithm::trim(line);
    results.push_back(line);
  }
  while (results.back().empty()) results.pop_back();

  return results;
}

std::string get_input_path(const path &root, int day) {
  char file_name[20];
  sprintf(file_name, "day_%02d.txt", day);

  return (root / "inputs" / file_name).string();
}

int main(int argc, const char *argv[]) {
  auto root = path(argv[0]).parent_path().parent_path();
  root = root.empty() ? ".." : root;

  try {
    if (argc != 2) {
      throw std::runtime_error("Requires 1 argument.");
    }
    int day = std::stoi(argv[1]);

    auto input_file = get_input_path(root, day);
    auto lines = get_lines(input_file);
    std::cout << input_file << ": " << lines.size() << " lines" << std::endl;

    auto solver = Solver::Create(day, lines);

    auto p1 = solver->part1();
    std::cout << "Part 1: " << p1 << std::endl;
    auto p2 = solver->part2();
    std::cout << "Part 2: " << p2 << std::endl;
  } catch (const std::runtime_error &e) {
    std::cerr << e.what() << std::endl;
    return 1;
  }
  return 0;
}