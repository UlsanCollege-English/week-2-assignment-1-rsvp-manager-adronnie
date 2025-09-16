from typing import List, Tuple

def dedupe_emails_case_preserve_order(emails: List[str]) -> List[str]:
    """Return a new list with duplicate emails removed, preserving first seen.
    Treat emails case-insensitively. Ignore entries without '@'.
    """
    seen = set()
    result = []
    for email in emails:
        if '@' not in email:
            continue
        key = email.lower()
        if key not in seen:
            seen.add(key)
            result.append(email)
    return result

def first_with_domain(emails: List[str], domain: str) -> int | None:
    """Return the index of the first email whose domain matches `domain` (case-insensitive)."""
    domain_lower = domain.lower()
    for i, email in enumerate(emails):
        if '@' not in email:
            continue
        email_domain = email.split('@')[-1].lower()
        if email_domain == domain_lower:
            return i
    return None

def domain_counts(emails: List[str]) -> List[Tuple[str, int]]:
    """Return (domain, count) pairs sorted by domain (A..Z), skipping malformed emails."""
    counts = {}
    for email in emails:
        if '@' not in email:
            continue
        domain = email.split('@')[-1].lower()
        counts[domain] = counts.get(domain, 0) + 1
    # Return sorted list of tuples
    return sorted(counts.items())
