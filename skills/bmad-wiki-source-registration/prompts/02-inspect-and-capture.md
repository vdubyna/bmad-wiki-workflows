# Stage 2: Inspect And Capture

Verify the source enough to register it without doing an unbounded scan.

## Rules

- For local files, verify path, file type, size, and readability before reading content.
- For directories, inventory top-level files first and ask before deep traversal.
- For Git repositories, capture branch/commit/status with read-only commands if the user approved.
- For URLs, fetch only explicitly supplied URLs and respect user privacy boundaries.
- For datasets or media assets, capture metadata first; do not load large content unless needed.
- For transcripts or notes, record that authority is lower unless tied to a canonical source.

## Capture

- source locator;
- content type;
- modified date or version if available;
- size or scope;
- read/inspection commands used;
- excluded sections and reasons;
- raw evidence excerpt or metadata summary.

## Continue When

You have enough verified metadata to classify the source and write a raw source record.
