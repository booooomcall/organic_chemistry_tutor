import streamlit as st
import json

st.title("🧬 Functional Groups")

with open("data/functional_groups.json") as f:
    groups = json.load(f)

for group in groups:
    with st.expander(group["name"]):
        st.markdown(f"**Group:** `{group['symbol']}`")
        st.markdown(f"**Example:** {group['example']}")
        st.caption(group['description'])
