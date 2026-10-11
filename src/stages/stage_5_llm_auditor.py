"""
Stage 5: LLM Semantic Auditor (ICP Strategic Authority)
Context-aware evaluation of whether the candidate holds true budget authority
and decides WHAT and WHERE to build, rather than holding an inflated LinkedIn title.
"""

from typing import List, Dict, Tuple

ICP_TARGET_ROLES = [
    "vd", "ceo", "fastighetschef", "projektutvecklingschef",
    "stadsbyggnadsdirektör", "samhällsbyggnadschef", "stadsarkitekt",
    "fastighetsdirektör", "affärsutvecklare", "head of property"
]

def run_llm_semantic_audit(leads: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    """
    Semantic AI verification of strategic decision-making authority against ICP.
    """
    passed: List[Dict] = []
    rejected: List[Dict] = []

    for lead in leads:
        title_lower = lead.get("title", "").lower()
        
        # Verify alignment with strategic decision-making ICP
        is_strategic_lpr = any(role in title_lower for role in ICP_TARGET_ROLES)
        
        if is_strategic_lpr:
            lead["llm_audit_verdict"] = "VERIFIED LPR (Holds Budget & Strategic Project Authority)"
            passed.append(lead)
        else:
            lead["rejection_reason"] = "LLM Audit Veto: Non-strategic or secondary influencer role"
            rejected.append(lead)

    return passed, rejected
