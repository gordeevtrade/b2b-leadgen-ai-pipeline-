"""
Stage 7: Outlier Gate & CRM-Ready Zero-Styling Master Export
Performs final data sanity checks (network size, realistic tenure)
and exports an uncorrupted, standard raw dataset directly into CRM.
Enforces the Zero Styling & Zero Data Loss rule.
"""

from typing import List, Dict
import pandas as pd

def run_master_export(leads: List[Dict], output_file: str = "verified_master_leads.xlsx") -> pd.DataFrame:
    """
    Validates outliers and generates a clean, unstyled Excel dataset.
    """
    verified: List[Dict] = []

    for lead in leads:
        # Sanity check: minimum professional network and reasonable tenure
        exp = lead.get("total_work_experience_years", 0)
        conn = lead.get("linkedin_connections", 0)

        if 5 <= exp <= 36 and conn >= 50:
            verified.append(lead)

    df = pd.DataFrame(verified)
    
    # Export without custom colors or fills (Standard default Excel format)
    df.to_excel(output_file, index=False)
    print(f"Master file successfully exported: {output_file} with {len(df)} verified decision-makers.")
    
    return df
