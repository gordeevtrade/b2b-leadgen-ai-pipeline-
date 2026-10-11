"""
Stage 2: Negative Regex Title & Seniority Filter
Executes in under 50 milliseconds.
Purges junior positions, interns, trade workers, and unrelated advisory titles.
"""

import re
from typing import List, Dict, Tuple

NEGATIVE_TITLE_PATTERNS = [
    r"\bplatschef\b",
    r"\bsite\s*foreman\b",
    r"\belektriker\b",
    r"\belectrician\b",
    r"\bvvs\b",
    r"\bplumber\b",
    r"\bmontör\b",
    r"\bintern\b",
    r"\btrainee\b",
    r"\bassistant\b",
    r"\bkoordinator\b",
    r"\blegal\s*counsel\b",
    r"\bassociate\b",
    r"\badvokat\b",
    r"\bjurist\b"
]

NEGATIVE_REGEX = re.compile("|".join(NEGATIVE_TITLE_PATTERNS), re.IGNORECASE)

def run_regex_filter(leads: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    """
    Strips out operational subordinates, trade technicians, and non-target professions.
    """
    passed: List[Dict] = []
    purged: List[Dict] = []

    for lead in leads:
        title = lead.get("title", "")
        match = NEGATIVE_REGEX.search(title)
        
        if match:
            lead["rejection_reason"] = f"Regex Veto: Subordinate / Trade keyword matched '{match.group(0)}'"
            purged.append(lead)
        else:
            passed.append(lead)

    return passed, purged
