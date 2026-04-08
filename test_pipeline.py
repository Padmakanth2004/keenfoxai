from intelligence.competitor_engine import run_engine
from campaign.feedback_engine import generate_campaign

print("\n===== RUNNING COMPETITOR ENGINE =====\n")

# ✅ Test competitor engine error handling
try:
    data = run_engine()
except Exception as e:
    print(f"❌ Error running engine: {e}")
    data = {}

print("Engine Output:")
print(data)


print("\n===== GENERATING CAMPAIGN =====\n")

# ✅ Test feedback engine error handling
try:
    campaign = generate_campaign(data)
except Exception as e:
    campaign = f"❌ Error generating campaign: {e}"

print("Campaign Output:")
print(campaign)