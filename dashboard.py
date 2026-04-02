import streamlit as st
import json

st.set_page_config(
    page_title="KeenFox Intelligence Dashboard",
    layout="wide"
)

st.title("🚀 KeenFox Competitive Intelligence Dashboard")


# =========================
# 🔧 HELPER FUNCTION
# =========================
def display_list(items):
    if not items:
        st.write("No data available")
    else:
        for item in items:
            st.markdown(f"• {item}")


# =========================
# 📂 LOAD DATA SAFELY
# =========================
try:
    with open("output/report.json") as f:
        content = f.read().strip()

        if not content:
            st.error("❌ report.json is empty. Run main.py first.")
            st.stop()

        data = json.loads(content)

except Exception as e:
    st.error(f"❌ Failed to load data: {e}")
    st.stop()


# =========================
# 🔍 SIDEBAR
# =========================
st.sidebar.title("🔍 Select Competitor")
competitor = st.sidebar.selectbox("", list(data.keys()))

comp_data = data[competitor]


# =========================
# 📊 TABS
# =========================
tab1, tab2, tab3 = st.tabs(["📊 Insights", "🎯 Campaign", "💬 Q&A"])


# =========================
# 📊 TAB 1: INSIGHTS
# =========================
with tab1:
    st.header(f"{competitor} Insights")

    col1, col2 = st.columns(2)

    # LEFT COLUMN
    with col1:
        st.subheader("🚀 Feature Launches")
        display_list(comp_data.get("feature_launches", []))

        st.subheader("🗣 Messaging Shifts")
        display_list(comp_data.get("messaging_shifts", []))

    # RIGHT COLUMN
    with col2:
        st.subheader("😊 Customer Loves")
        display_list(comp_data.get("customer_sentiment", {}).get("loves", []))

        st.subheader("😡 Customer Complaints")
        display_list(comp_data.get("customer_sentiment", {}).get("complaints", []))

    # FULL WIDTH SECTIONS
    st.subheader("💰 Pricing Changes")
    display_list(comp_data.get("pricing_changes", []))

    st.subheader("⚠️ Gaps / Weaknesses")
    display_list(comp_data.get("gaps", []))


# =========================
# 🎯 TAB 2: CAMPAIGN
# =========================
with tab2:
    st.header("🎯 Campaign Strategy Recommendations")

    try:
        with open("output/campaign.md") as f:
            campaign = f.read()
            st.markdown(campaign)
    except:
        st.warning("⚠️ Run main.py to generate campaign output")


# =========================
# 💬 TAB 3: Q&A
# =========================
with tab3:
    st.header("💬 Ask Questions")

    question = st.text_input("Ask something about competitors:")

    if question:
        from intelligence.query_engine import answer_query
        answer = answer_query({competitor: comp_data}, question)

        st.subheader("Answer:")
        st.write(answer)