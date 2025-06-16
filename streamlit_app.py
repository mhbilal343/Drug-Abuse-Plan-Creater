import streamlit as st

# Page config
st.set_page_config(page_title="Drug Use Action Planner", page_icon="💊", layout="centered")

# Title
st.title("💊 Create Your Drug Use Action Plan")
st.markdown("Use this space to build your own plan to change or manage your drug use. It's totally private and up to you.")

st.header("🧭 Step 1: Define Your Goal")
goal = st.text_area("What is your main goal?", placeholder="E.g. I want to stop using weed for 30 days...")

st.header("✅ Step 2: List Your Action Steps")
st.markdown("Break your goal into small steps. Add as many as you'd like.")

steps = []
for i in range(1, 6):
    step = st.text_input(f"Step {i}", placeholder=f"E.g. Delete dealer's contact, find sober friends...")
    if step:
        steps.append(step)

st.header("📅 Step 3: Set a Timeline")
start_date = st.date_input("When will you start?", help="Pick a realistic start date.")
end_date = st.date_input("When do you want to reach your goal?", help="When do you want this goal complete?")

st.header("🧍 Step 4: Who Can Support You?")
support_person = st.text_input("Name someone you trust or talk to (optional)", placeholder="E.g. counselor, parent, friend")

st.header("🧠 Step 5: Prepare for Challenges")
triggers = st.text_area("What might make this hard?", placeholder="E.g. stress, parties, friends who use")
plan_b = st.text_area("What will you do when it gets hard?", placeholder="E.g. call a friend, go for a walk, journal")

# --- Display Plan Summary ---
if st.button("📄 Show My Full Plan"):
    st.subheader("📋 Your Personalized Action Plan")
    st.markdown(f"### 🎯 Goal\n{goal}")
    if steps:
        st.markdown("### ✅ Action Steps")
        for s in steps:
            st.markdown(f"- {s}")
    st.markdown(f"### 📅 Timeline\nStart: **{start_date}** → End: **{end_date}**")
    if support_person:
        st.markdown(f"### 🤝 Support Person\nYou can reach out to: **{support_person}**")
    if triggers:
        st.markdown(f"### ⚠️ Challenges\nThings to watch out for: {triggers}")
    if plan_b:
        st.markdown(f"### 🧰 Coping Plan\nIf it gets hard: {plan_b}")

    # --- Export Plan ---
    export_text = f"""
Drug Use Action Plan
---------------------
Goal:
{goal}

Steps:
{chr(10).join(['- ' + s for s in steps])}

Timeline:
Start: {start_date}
End: {end_date}

Support:
{support_person}

Challenges:
{triggers}

Coping Plan:
{plan_b}
"""
    st.download_button("📥 Download My Plan", export_text, file_name="my_drug_use_plan.txt")

# Footer
st.markdown("---")
st.caption("This tool is for self-reflection. For emergencies or medical help, contact a professional or a helpline.")