import streamlit as st

st.title("📖 IUPAC Naming")

examples = {
    "CH3COOH": "Ethanoic Acid – A two-carbon carboxylic acid.",
    "C2H5OH": "Ethanol – A two-carbon alcohol.",
    "CH3CH2CH3": "Propane – A three-carbon alkane.",
    "CH3CH=CH2": "Propene – A three-carbon alkene."
}

compound = st.text_input("Enter a compound formula (e.g., CH3COOH):")
if compound:
    st.info(examples.get(compound.strip(), "Compound not found. Try a simpler formula."))
