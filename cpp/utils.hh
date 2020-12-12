
template <size_t K> class combo_iterator {
  private:
    size_t indices[K + 1];
    size_t N;

  public:
    combo_iterator(size_t N) : N(N) {
        for (size_t i = 0; i < K; ++i) {
            indices[i] = i;
        }
        indices[K] = N;
    }

    bool next() {
        int curr = K - 1;
        while (curr >= 0 && indices[curr] + 1 >= indices[curr + 1]) {
            --curr;
        }
        if (curr < 0) {
            return false;
        }
        size_t start = indices[curr];
        while (curr < K) {
            indices[curr++] = ++start;
        }
        return true;
    }

    size_t operator[](size_t i) const { return indices[i]; }
};
