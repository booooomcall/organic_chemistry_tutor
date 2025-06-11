import streamlit as st

st.title("🧠 Organic Chemistry Quiz")

questions = [
    {"q": "Which functional group is in ethanol?", "a": "Alcohol", "options": ["Ketone", "Alcohol", "Alkene"]},
    {"q": "What is the general formula for alkanes?", "a": "CnH2n+2", "options": ["CnH2n", "CnH2n+2", "CnH2n-2"]}
]

score = 0
for i, q in enumerate(questions):
    answer = st.radio(q["q"], q["options"], key=f"quiz_{i}")
    if answer == q["a"]:
        st.success("✅ Correct!")
        score += 1
    else:
        st.error(f"❌ Correct answer: {q['a']}")

st.markdown(f"### Final Score: {score}/{len(questions)}")
