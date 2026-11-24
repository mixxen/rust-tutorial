# The same small program in C++, Python, and Rust

Each program counts how many of `[18, 22, 25, 29]` are strictly above 25. Only 29 qualifies, so each prints `Readings above 25: 1`.

## Compare the syntax

| Task | C++ | Python | Rust |
|---|---|---|---|
| Declare a parameter | `int reading` | `reading: int` | `reading: i32` |
| Return the comparison | `return reading > limit;` | `return reading > limit` | `reading > limit` |
| Set the limit | `const int limit = 25;` | `limit = 25` | `let limit = 25;` |
| Start the counter | `int qualifying_count = 0;` | `qualifying_count = 0` | `let mut qualifying_count = 0;` |
| Loop over readings | `for (int reading : readings) {` | `for reading in readings:` | `for reading in readings {` |

## C++17

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

`const` keeps the array and limit fixed. The program can update `qualifying_count` because its declaration leaves off `const`. [C++ source](examples/threshold.cpp)

## Python

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

Python uses a list for the readings. The annotations communicate intended types to readers and type-checking tools. [Python source](examples/threshold.py) · [Python typing documentation](https://docs.python.org/3/library/typing.html)

## Rust

```rust
fn is_above_limit(reading: i32, limit: i32) -> bool {
    reading > limit
}

fn main() {
    let readings = [18, 22, 25, 29];
    let limit = 25;
    let mut qualifying_count = 0;

    for reading in readings {
        if is_above_limit(reading, limit) {
            qualifying_count += 1;
        }
    }

    println!("Readings above {limit}: {qualifying_count}");
}
```

Rust infers the local types and checks them at compile time. The readings are a fixed-size array, and `let mut` allows the counter to change. The final expression `reading > limit` supplies the function's Boolean return value. [Rust source](src/main.rs) · [Walkthrough](03-readings-and-control-flow.md)

## Check the output

To run all three programs, use this command from the repository root.

```sh
make comparisons
```

This command needs `g++`, Python, and Cargo. It checks that each program prints `Readings above 25: 1`.
