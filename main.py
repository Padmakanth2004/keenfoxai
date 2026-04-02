from intelligence.competitor_engine import run_engine
from intelligence.report_generator import save_report
from campaign.feedback_engine import generate_campaign
from memory.memory_manager import save_memory, load_memory, compute_diff
from intelligence.query_engine import answer_query


def main():
    print("🚀 Running Component 1...")

    # --- LOAD PREVIOUS DATA ---
    old_data = load_memory()

    # --- RUN ENGINE ---
    new_data = run_engine()

    # --- SAVE REPORT ---
    save_report(new_data)

    # --- COMPUTE DIFF ---
    if old_data:
        diff = compute_diff(old_data, new_data)
        print("\n🔄 Changes since last run:")
        print(diff)
    else:
        print("\n🆕 First run — no previous data to compare.")

    print("\n🎯 Running Component 2...")

    # --- CAMPAIGN GENERATION ---
    campaign = generate_campaign(new_data)

    with open("output/campaign.md", "w") as f:
        f.write(campaign)

    # --- SAVE MEMORY ---
    save_memory(new_data)

    print("\n💬 Ask questions about competitors (type 'exit' to stop):")

    # --- Q&A LOOP ---
    while True:
        question = input("👉 Your question: ")

        if question.lower() == "exit":
            break

        answer = answer_query(new_data, question)
        print("\n🤖 Answer:")
        print(answer)
        print("-" * 50)

    print("\n✅ System Complete")


if __name__ == "__main__":
    main()