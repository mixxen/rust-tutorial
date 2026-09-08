// Supplied verification code. Process launching is taught later in the course.
// This test checks what the executable prints, not just the small function.
use std::process::Command;

#[test]
fn prints_the_number_of_readings_strictly_above_the_limit() {
    let output = Command::new(env!("CARGO_BIN_EXE_lesson-00-rust-orientation"))
        .output()
        .expect("the built lesson executable should start");

    assert!(output.status.success());
    assert_eq!(output.stdout, b"Readings above 25: 1\n");
    assert!(output.stderr.is_empty());
}
