#!/usr/bin/env python3
"""sort_posts.py

Utility script for the giordcer.github.io Jekyll site.

Scans the ``_posts`` directory for markdown files named
``YYYY-MM-DD-title.md`` (the month and day may be one or two digits).
It extracts the date and a human‑readable title from the filename and
prints a sorted list.

Usage:
    python sort_posts.py [--by date|title]

Options:
    --by date   Sort by date (newest first). This is the default.
    --by title  Sort alphabetically by title.

The script prints each entry on its own line in the form:
    YYYY-MM-DD  Title

Add the script to the repository root and make it executable if you
wish to run it directly.
"""

import argparse
import os
import re
from datetime import datetime
from pathlib import Path

POSTS_DIR = Path(__file__).parent / "_posts"

FILENAME_RE = re.compile(r"^(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})-(?P<title>.+)\.md$")

def parse_filename(filename: str):
    """Return (date: datetime, title: str) for a valid post filename.
    Raises ValueError if the filename does not match the expected pattern.
    """
    stem = Path(filename).name
    m = FILENAME_RE.match(stem)
    if not m:
        raise ValueError(f"Unexpected filename format: {filename}")
    year = int(m.group('year'))
    month = int(m.group('month'))
    day = int(m.group('day'))
    date = datetime(year, month, day)
    # Convert hyphens in the title part to spaces and capitalize words
    raw_title = m.group('title')
    title = raw_title.replace('-', ' ').title()
    return date, title

def collect_posts():
    posts = []
    if not POSTS_DIR.is_dir():
        return posts
    for entry in POSTS_DIR.iterdir():
        if entry.is_file() and entry.suffix.lower() == ".md":
            try:
                date, title = parse_filename(entry.name)
                posts.append((date, title, entry.name))
            except ValueError:
                # Skip files that don't follow the naming convention
                continue
    return posts

def main():
    parser = argparse.ArgumentParser(description="List Jekyll posts sorted by date or title.")
    parser.add_argument("--by", choices=["date", "title"], default="date",
                        help="Sorting key: 'date' (newest first) or 'title' (alphabetical)")
    args = parser.parse_args()

    posts = collect_posts()
    if args.by == "date":
        # Newest first
        posts.sort(key=lambda x: x[0], reverse=True)
    else:
        posts.sort(key=lambda x: x[1].lower())

    for date, title, filename in posts:
        print(f"{date.strftime('%Y-%m-%d')}  {title}")

if __name__ == "__main__":
    main()
