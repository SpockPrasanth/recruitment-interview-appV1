import streamlit as st

st.set_page_config(layout="wide")

questions = [

    {
        "question": "What is ETL vs ELT?",
        "good": "ETL transforms before load; ELT transforms after load",
        "red": "Cannot differentiate clearly"
    },

    {
        "question": "What is a data pipeline?",
        "good": "End-to-end data flow explanation",
        "red": "Very generic answer"
    }

]

# ==========================================
# HEADER
# ==========================================

header1, header2, header3, header4 = st.columns([3,4,4,1])

with header1:
    st.markdown("### Question")

with header2:
    st.markdown("### Good Signals")

with header3:
    st.markdown("### Red Flags")

with header4:
    st.markdown("### Score")

st.divider()

# ==========================================
# DATA ROWS
# ==========================================

for index, item in enumerate(questions):

    col1, col2, col3, col4 = st.columns([3,4,4,1])

    with col1:
        st.info(item["question"])

    with col2:
        st.success(item["good"])

    with col3:
        st.error(item["red"])

    with col4:
        st.number_input(
            "",
            min_value=0,
            max_value=10,
            key=index
        )
