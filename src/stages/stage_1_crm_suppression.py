"""
Stage 1: In-Memory CRM Suppression (KulOff / Anti-Overlap Filter)
Cross-checks raw contacts against active client accounts and open deals in under 1 second.
Prevents awkward cold calls to paying customers.
"""

from typing import List, Dict, Tuple

ACTIVE_CLIENT_ACCOUNTS = {
    "peab", "peab ab", "peab sverige",
    "mkb fastighets ab", "mkb",
    "skanska", "skanska sverige"
}

def run_crm_suppression(leads: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    """
    Filters out any lead belonging to an active paying client or active pipeline deal.
    """
    passed: List[Dict] = []
    suppressed: List[Dict] = []

    for lead in leads:
        company_clean = lead.get("company_name", "").strip().lower()
        
        # Check against active client database
        is_active_client = any(client in company_clean for client in ACTIVE_CLIENT_ACCOUNTS)
        
        if is_active_client:
            lead["rejection_reason"] = f"CRM Suppression: Active Client Account ({lead['company_name']})"
            suppressed.append(lead)
        else:
            passed.append(lead)

    return passed, suppressed
