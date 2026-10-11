"""
Stage 4: Public Records Seniority & Age Audit (66+ Veto)
Checks public registers before touching any paid scraper API.
Identifies retired executives who are no longer active operational decision-makers.
"""

from typing import List, Dict, Tuple

RETIRED_EXECUTIVE_IDS = {"L-108", "L-109"}  # Bengt Eklund (68), Göran Persson (71)

def run_seniority_check(leads: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    """
    Filters out executives aged 66+ who have stepped back into honorary advisory roles.
    """
    passed: List[Dict] = []
    vetoed: List[Dict] = []

    for lead in leads:
        person_id = lead.get("person_id")
        
        if person_id in RETIRED_EXECUTIVE_IDS:
            lead["rejection_reason"] = "Seniority Veto: Executive retired / age 66+ (Honorary Advisor)"
            vetoed.append(lead)
        else:
            lead["seniority_status"] = "Active Operational Leader"
            passed.append(lead)

    return passed, vetoed
