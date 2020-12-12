#pragma once
#import <numeric>

#import "solvers.hh"
#import "utils.hh"

class Solver3 : public Solver {
  private:
    class Grid {
      public:
        const size_t nrows, ncols;

      private:
        std::vector<int> data;
        int const *ptr;

      public:
        Grid(const std::vector<std::string> &lines)
            : nrows(lines.size()), ncols(lines[0].size()),
              data(nrows * ncols, 0), ptr(data.data()) {
            int *dataPtr = data.data();
            for (const auto &line : lines) {
                for (char letter : line) {
                    *(dataPtr++) = letter == '#' ? 1 : 0;
                }
            }
        }

        int at(int i, int j) const {
            i = i % nrows;
            j = j % ncols;
            return ptr[i * ncols + j];
        }

        size_t sweep(const int drow, const int dcol) const {
            size_t count = 0;
            for (int i = 0; i * drow < nrows; ++i) {
                count += at(i * drow, i * dcol);
            }
            return count;
        }
    };

    Grid grid;

  public:
    inline Solver3(const std::vector<std::string> &input) : grid(input) {}

    inline long part1() { return grid.sweep(1, 3); }

    inline long part2() {
        std::vector<size_t> sweeps = {grid.sweep(1, 1), grid.sweep(1, 3),
                                      grid.sweep(1, 5), grid.sweep(1, 7),
                                      grid.sweep(2, 1)};

        return std::accumulate(sweeps.begin(), sweeps.end(), (size_t)1,
                               [](size_t a, size_t b) { return a * b; });
    }
};
