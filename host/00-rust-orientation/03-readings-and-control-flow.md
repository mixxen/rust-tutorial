# Part 3. Readings and control flow

[Lesson 00](README.md) · [Part 2. Functions and variables](02-functions-and-variables.md)

Keep editing `src/main.rs` in your `hello_rust` project. Run `cargo run` from that project. If your terminal reopened at the repository root, return to `practice/hello_rust/` or to the folder you used in part 1.

## 1. Use a Boolean result in an if statement

Replace `src/main.rs` with this program. It checks one reading.

<!-- walkthrough: condition -->
```rust
fn is_above_limit(reading: i32, limit: i32) -> bool {
    reading > limit
}

fn main() {
    let reading = 29;
    let limit = 25;

    if is_above_limit(reading, limit) {
        println!("Reading qualifies.");
    } else {
        println!("Reading does not qualify.");
    }
}
```

Save the file and run `cargo run`. The program prints the result.

```text
Reading qualifies.
```

The function returns `true`, so Rust runs the first block. For `false`, Rust runs the `else` block. The braces mark the start and end of each block.

Rust expects a `bool` after `if`. To check whether an integer is nonzero, write `if reading != 0`. The operator `!=` means "is different from."

## 2. Use an array and a loop

Now count how many of 18, 22, 25, and 29 are strictly above 25. Replace `src/main.rs` with this program.

<!-- walkthrough: count_readings -->
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

Save the file and run `cargo run`. The program prints the count.

```text
Readings above 25: 1
```

The square brackets in `[18, 22, 25, 29]` create an *array*. An array has a fixed length and one type for all its elements. Rust infers `i32` for these elements because the loop passes them to `is_above_limit`.

`for reading in readings` visits each element of the array. Inside the loop, `reading` is the current element.

The outer braces enclose the loop body. The inner braces enclose the code that runs when a reading qualifies. That code updates `qualifying_count`, so the counter needs `mut`.

The count after each reading is:

| Current reading | Is it greater than 25? | Count after this iteration |
|---|---|---|
| 18 | No | 0 |
| 22 | No | 0 |
| 25 | No, it equals the limit | 0 |
| 29 | Yes | 1 |

The last `println!` sits outside the loop, so it prints the final count once.

## 3. Connect this to C++ and Python

The C++ and Python versions use the same inputs and count the readings with the same rule. See how each language declares the counter and returns the result from `is_above_limit`. [C++, Python, and Rust comparison](COMPARISON.md)

### Optional references

[Rust Book, data types and arrays](https://doc.rust-lang.org/book/ch03-02-data-types.html) · [Rust Book, control flow](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
