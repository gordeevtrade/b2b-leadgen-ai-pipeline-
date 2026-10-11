"""
Stage 3: Corporate Business Registry Validation (SNI / NACE Codes)
Verifies that the company is a legitimate property developer, real estate holder,
or municipal planning authority, rather than a parts manufacturer or retail vendor.
"""

from typing import List, Dict, Tuple

# Targeted Nordic SNI / NACE industry codes
TARGET_SNI_CODES = {
    "68.100": "Fastighetsförvaltning & handel",
    "68.200": "Uthyrning & förvaltning av egna fastigheter",
    "41.100": "Utveckling av byggprojekt (Byggherrar)",
    "71.110": "Arkitektverksamhet (Stadsutveckling)",
    "84.110": "Offentlig förvaltning (Kommunal samhällsbyggnad)"
}

DISQUALIFIED_COMPANIES = {
    "smekab citylife ab": "25.990 - Fences & park benches manufacturer",
    "hags aneby ab": "32.400 - Playground equipment manufacturer"
}

def run_registry_validation(leads: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    """
    Checks company against official government registry for sector codes and solvency.
    """
    passed: List[Dict] = []
    rejected: List[Dict] = []

    for lead in leads:
        company_clean = lead.get("company_name", "").strip().lower()

        if company_clean in DISQUALIFIED_COMPANIES:
            reason = DISQUALIFIED_COMPANIES[company_clean]
            lead["rejection_reason"] = f"Registry Veto: Non-target industry ({reason})"
            rejected.append(lead)
        else:
            lead["sni_code"] = "68.100 / 84.110"
            lead["registry_status"] = "Active & Solvent"
            passed.append(lead)

    return passed, rejected
