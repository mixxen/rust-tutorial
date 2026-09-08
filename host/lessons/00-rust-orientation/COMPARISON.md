# The same small program in C++, Python, and Rust

All three worked examples count readings strictly above 25. They use identical sample data and intentionally direct loops. This compares the task and its expression, not every detail of the languages' numeric types.

## C++17

Source: [`comparisons/threshold.cpp`](comparisons/threshold.cpp).

```cpp
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
```

The `const` declarations indicate which values this example does not change. This is a useful connection to Rust's immutable bindings, not a claim that C++ and Rust have identical constness rules.

## Python

Source: [`comparisons/threshold.py`](comparisons/threshold.py).

```python
def is_above_limit(reading: int, limit: int) -> bool:
    return reading > limit


def main() -> None:
    readings = [18, 22, 25, 29]
    limit = 25
    qualifying_count = 0

    for reading in readings:
        if is_above_limit(reading, limit):
            qualifying_count += 1

    print(f"Readings above {limit}: {qualifying_count}")


if __name__ == "__main__":
    main()
```

The annotations communicate intended types but Python does not enforce them by itself at runtime. The list is not the same storage abstraction as a Rust fixed-size array. Those differences do not change this sample's count. See Python's [typing documentation](https://docs.python.org/3/library/typing.html).

## Rust

The [lesson walkthrough](README.md#3-read-the-program-without-guessing-at-punctuation) shows the complete `main` function and the small function from `src/lib.rs`. The library/executable split gives the tests access to the same decision used by the program; it is not an excuse to build a large framework.

Rust infers local types while retaining compile-time checks, distinguishes mutable bindings explicitly, and permits the comparison itself to be the function's tail expression. For this program, there is no need for heap allocation, traits, references, or an iterator chain.

## Check the actual outputs

From the Lesson 00 directory:

```bash
make comparisons
```

This requires `g++` and Python in addition to Rust. The author script compiles the C++ file, executes all three programs, and checks each against `Readings above 25: 1`. Merely comparing three outputs to each other would miss a mistake copied into all three, so the expected output is specified separately.

This command is optional for learners; the normal Rust example does not need you to know how to configure a C++ build.
