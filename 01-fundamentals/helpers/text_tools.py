"""
text_tools — a single module inside the helpers package.

Demonstrates two things chapter 17 covers:
  * module-level code, functions, and a private-by-convention name
  * the __name__ == "__main__" guard, so this file is BOTH a script
    and an importable library

Run it directly to trigger the self-test:
    python 01-fundamentals/helpers/text_tools.py
"""

import re

# A leading underscore means "internal to this module" by convention.
# Python does not enforce it — C# has `private`, Python has manners.
_NON_WORD = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Lowercase, hyphenated, URL-safe. 'Hello, Azure Foundry!' → hello-azure-foundry"""
    return _NON_WORD.sub("-", text.lower()).strip("-")


def word_count(text: str) -> int:
    """Count whitespace-separated words."""
    return len(text.split())


def truncate(text: str, limit: int = 20, suffix: str = "…") -> str:
    """Shorten text to `limit` characters, appending a suffix when cut."""
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + suffix


def _self_test() -> None:
    """A cheap contract test that runs only when this file is executed."""
    assert slugify("Hello, Azure Foundry!") == "hello-azure-foundry"
    assert word_count("a b c d") == 4
    assert truncate("long sentence here", 10) == "long sente…"
    assert truncate("short", 10) == "short"
    print("text_tools: all self-tests passed")


if __name__ == "__main__":
    # Only runs when executed directly — importing this module is silent.
    _self_test()
