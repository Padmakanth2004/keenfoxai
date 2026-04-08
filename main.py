from intelligence.competitor_engine import run_engine
from intelligence.report_generator import save_report
from campaign.feedback_engine import generate_campaign
from memory.memory_manager import save_memory, load_memory, compute_diff
from intelligence.query_engine import answer_query


def main():
    print("🚀 Running Component 1...")

    # --- LOAD PREVIOUS DATA ---
    try:
        old_data = load_memory()
    except Exception as e:
        print(f"Error loading memory: {e}")
        old_data = {}

    # --- RUN ENGINE ---
    try:
        new_data = run_engine()
    except Exception as e:
        print(f"Error running engine: {e}")
        new_data = {}

    # --- SAVE REPORT ---
    try:
        save_report(new_data)
    except Exception as e:
        print(f"Error saving report: {e}")

    # --- COMPUTE DIFF ---
    try:
        if old_data:
            diff = compute_diff(old_data, new_data)
            print("\n🔄 Changes since last run:")
            print(diff)
        else:
            print("\n🆕 First run — no previous data to compare.")
    except Exception as e:
        print(f"Error computing diff: {e}")

    print("\n🎯 Running Component 2...")

    # --- CAMPAIGN GENERATION ---
    try:
        campaign = generate_campaign(new_data)
    except Exception as e:
        print(f"Error generating campaign: {e}")
        campaign = "Campaign generation failed."

    # --- SAVE CAMPAIGN ---
    try:
        import os
        os.makedirs("output", exist_ok=True)

        with open("output/campaign.md", "w") as f:
            f.write(campaign)
    except Exception as e:
        print(f"Error saving campaign: {e}")

    # --- SAVE MEMORY ---
    try:
        save_memory(new_data)
    except Exception as e:
        print(f"Error saving memory: {e}")

    print("\n💬 Ask questions about competitors (type 'exit' to stop):")

    # --- Q&A LOOP ---
    while True:
        try:
            question = input("👉 Your question: ")
        except Exception:
            print("Input error. Try again.")
            continue

        if question.lower() == "exit":
            break

        try:
            answer = answer_query(new_data, question)
        except Exception as e:
            answer = f"Error answering question: {e}"

        print("\n🤖 Answer:")
        print(answer)
        print("-" * 50)

    print("\n✅ System Complete")
if __name__ == "__main__":
    main()