"""
Main entry point for running the B2B Lead Generation Quality Funnel.
"""

import sys
import os

# Add src to python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from pipeline import execute_pipeline

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "data", "sample_raw_leads.csv")
    execute_pipeline(data_path)
