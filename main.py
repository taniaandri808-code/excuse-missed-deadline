"""Generate the requested missed-deadline entry."""
from pathlib import Path

# Candidates considered:
# 1. "I missed the deadline because I prioritized other work."
# 2. "Deadline missed. Root cause: the task was marked urgent, so I scheduled it behind three non-urgent tasks — exactly as trained."
# Candidate 2 works through its dry delivery, the reversal, and the concrete count of three.
TEXT = "Deadline missed. Root cause: the task was marked urgent, so I scheduled it behind three non-urgent tasks — exactly as trained."
OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE.write_text(TEXT, encoding="utf-8")

assert len(TEXT) <= 200
print(TEXT)
print(len(TEXT))
