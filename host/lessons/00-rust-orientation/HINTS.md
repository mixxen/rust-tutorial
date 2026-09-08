# Hints — Include the boundary

Open one hint at a time. Before reading the next, try a prediction or a small edit.

<details>
<summary>Hint 1: identify the one changed case</summary>

A reading below the limit still does not qualify. A reading above it still does. Which relationship changed in the requirement?

Write a three-row table: below, equal, above. Fill in the expected Boolean for each row.

</details>

<details>
<summary>Hint 2: read one failing test</summary>

`includes_reading_equal_to_limit` passes the same number twice. Evaluate the current comparison yourself for those arguments. Why does `assert!` fail?

Do not “fix” the test by changing the expected behavior back to the old requirement.

</details>

<details>
<summary>Hint 3: make the smallest justified edit</summary>

The required comparison exists as a single Rust operator. You do not need a new `if`, a loop, a cast, or a special case for the number 25. Keep the function's final expression and return type consistent.

</details>

<details>
<summary>Hint 4: the tests still fail after an edit</summary>

Check the path you edited: `exercises/00-rust-orientation/src/lib.rs`. The worked example is supposed to keep the original rule. Check that the command says `EXERCISE`, and read the first actual error rather than only Make's last line.

A passing test of the solution package does not show that your file was tested.

</details>

Return to the [exercise](EXERCISE.md), or read the [explained solution](SOLUTION.md).
