#include <array>
#include <iostream>

bool is_above_limit(int reading, int limit) {
    return reading > limit;
}

int main() {
    const std::array<int, 4> readings = {18, 22, 25, 29};
    const int limit = 25;
    int qualifying_count = 0;

    for (int reading : readings) {
        if (is_above_limit(reading, limit)) {
            qualifying_count += 1;
        }
    }

    std::cout << "Readings above " << limit << ": " << qualifying_count << '\n';
}
