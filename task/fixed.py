import argparse
import sys
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

# testing:
# use pytest
# tmp/*.log
# pytest.raises for exceptions
# dont worry about time time or uuids being accurate. 
# dont worry about interactions (ie internal function calls)
# inputs/outputs, return values, raised errors, written files. 
# try for 10/10 score on pylint! 

OUTPUT_FILE = Path("logs") / "audit.log"
SYSTEM_NAME = "auth_service"
USER_ID_RE = re.compile(r"^user-\d+$")
KNOWN_USERS = {"user-100", "user-200", "user-300"}

# test outputs a string, ends with z, stretch: regex for basic shape (2026-04-16T11:17:54Z). 
def format_timestamp_utc_z() -> str:
    """UTC timestamp as an ISO-8601 string with Z (Zulu time)."""
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )

# optioanl: test the data shape 
def default_attempts() -> list[tuple[str, bool]]:
    return [
        ("user-100", True),
        ("user-200", False),
        ("user-100", False),
        ("user-999", True),
    ]

# test raise valueerror, convert string bools to bools, valid input + strips whitespace. 
def parse_attempt_line(raw: str, line_no: int) -> tuple[str, bool]:
    parts = [p.strip() for p in raw.split(",")]

    if len(parts) != 2:
        raise ValueError(
            f"Line {line_no}: expected exactly 2 fields separated by a single comma "
            f"(got {len(parts)} fields)"
        )

    user_id, success_raw = parts

    if not user_id:
        raise ValueError(f"Line {line_no}: empty user_id")

    if not USER_ID_RE.fullmatch(user_id):
        raise ValueError(
            f"Line {line_no}: invalid user_id {user_id!r} (expected 'user-<digits>')"
        )

    v = success_raw.lower()
    if v not in {"true", "false"}:
        raise ValueError(
            f"Line {line_no}: invalid success value {success_raw!r} (expected true|false)"
        )

    return user_id, (v == "true")

# test default is called correctly. reads file correctly, ignores lines with #, 
# test the value and runtime errors
def load_attempts(input_path: Path | None) -> list[tuple[str, bool]]:
    """
    If --input is provided, read attempts from file.
    Expected line format: user_id,true|false
    Blank lines and lines starting with # are ignored.
    """
    if input_path is None:
        return default_attempts()

    attempts: list[tuple[str, bool]] = []
    errors: list[str] = []

    try:
        with input_path.open("r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                raw = line.strip()
                if not raw or raw.startswith("#"):
                    continue

                try:
                    attempts.append(parse_attempt_line(raw, line_no))
                except ValueError as e:
                    errors.append(str(e))
    except OSError as e:
        raise RuntimeError(f"Failed to read input file {input_path}: {e}") from e

    if errors:
        raise ValueError("Invalid --input file:\n" + "\n".join(errors))

    return attempts
 
# test it contains the right fields + the input args remain the same)  
def build_event_line(user_id: str, success: bool, known: bool) -> str:
    ts = format_timestamp_utc_z()  # per-event timestamp
    outcome = "success" if success else "failure"
    user_status = "known" if known else "unknown"
    event_id = uuid.uuid4().hex
    return (
        f"event_id={event_id} time={ts} system={SYSTEM_NAME} user_id={user_id} "
        f"user_status={user_status} outcome={outcome}"
    )

# test for folder created, appends on 2nd call rather than overwrite. 
def write_lines_append_only(path: Path, lines: list[str]) -> None:
    # Append-only + context manager
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        raise RuntimeError(f"Cannot create log directory {path.parent}: {e}") from e

    try:
        with path.open("a", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")
    except OSError as e:
        raise RuntimeError(f"Failed to write to log file {path}: {e}") from e 
 
def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Stage 0 audit log writer")
    parser.add_argument(
        "--input",
        type=Path,
        default=None,
        help="Optional input file (lines: user_id,true|false). If omitted, defaults are used.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=OUTPUT_FILE,
        help="Optional output file path"
    )
    return parser.parse_args(argv)

# happy path returns 0, invalid input returns 2, missing file returns 3.
def main(argv: list[str]) -> int:
    args = parse_args(argv)

    try:
        attempts = load_attempts(args.input)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 2
    except RuntimeError as e:
        print(str(e), file=sys.stderr)
        return 3

    lines: list[str] = []

    for user_id, success in attempts:
        known = user_id in KNOWN_USERS
        lines.append(build_event_line(user_id, success, known))

    try:
        write_lines_append_only(args.output, lines)
    except RuntimeError as e:
        print(str(e), file=sys.stderr)
        return 3

    print(f"Wrote {len(lines)} lines to {args.output}")
    return 0
 
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))