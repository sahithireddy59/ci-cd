
from app.agents import run_analysis

sample_logs = """
2026-10-28 10:30:01 ERROR Database connection timeout
2026-10-28 10:30:02 WARNING Connection pool exhausted
2026-10-28 10:30:03 ERROR Failed to execute SQL query
"""

result = run_analysis(sample_logs)

print("\n=== INCIDENT ANALYSIS ===\n")
print(result["analysis"])

print("\n=== RESOLUTION PLAN ===\n")
print(result["resolution"])
