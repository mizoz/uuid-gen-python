#!/usr/bin/env python3
"""Generate UUIDs (v4)."""
import uuid, sys

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 1
    for _ in range(n): print(uuid.uuid4())
