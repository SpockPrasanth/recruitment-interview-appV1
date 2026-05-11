import streamlit as st

st.set_page_config(layout="wide")

# =====================================================
# DATA ENGINEERING QUESTION BANK
# =====================================================

questions = [

    {
        "section": "Fundamentals",
        "question": "What is ETL vs ELT?",
        "good": "ETL transforms before load; ELT transforms after load (warehouse/lake).",
        "red": "Cannot differentiate clearly."
    },

    {
        "section": "Fundamentals",
        "question": "What is a data pipeline?",
        "good": "End-to-end flow: source, ingestion, transformation, storage.",
        "red": "Very generic or unclear explanation."
    },

    {
        "section": "Data Engineering",
        "question": "What is partitioning and why is it used?",
        "good": "Improves performance; reduces data scan; used in big data.",
        "red": "No idea or vague explanation."
    },

    {
        "section": "Data Engineering",
        "question": "What is schema evolution?",
        "good": "Handling changes in data structure over time.",
        "red": "Cannot explain or no exposure."
    },

    {
        "section": "ADF",
        "question": "What is Azure Data Factory used for?",
        "good": "Orchestration, data movement, pipelines, integration.",
        "red": "Calls it only ETL tool without orchestration context."
    },

    {
        "section": "ADF",
        "question": "Difference between pipeline and data flow?",
        "good": "Pipeline = orchestration; Data Flow = transformation logic.",
        "red": "Confuses both."
    },

    {
        "section": "ADF",
        "question": "What are triggers in ADF?",
        "good": "Schedule/event-based execution of pipelines.",
        "red": "No idea or incorrect explanation."
    },

    {
        "section": "PySpark",
        "question": "What is PySpark and where is it used?",
        "good": "Distributed data processing using Spark; big data transformations.",
        "red": "Confuses with Python scripting only."
    },

    {
        "section": "PySpark",
        "question": "Difference between RDD, DataFrame, Dataset?",
        "good": "DataFrame preferred; structured and optimized.",
        "red": "No understanding of differences."
    },

    {
        "section": "PySpark",
        "question": "How do you optimize Spark jobs?",
        "good": "Partitioning, caching, broadcast joins, avoiding shuffles.",
        "red": "Generic answers without specifics."
    },

    {
        "section": "Architecture",
        "question": "Explain Medallion Architecture",
        "good": "Bronze raw, Silver cleaned, Gold curated.",
        "red": "Cannot explain layers."
    },

    {
        "section": "Architecture",
        "question": "What is a Lakehouse?",
        "good": "Combines data lake + warehouse capabilities.",
        "red": "No clarity or confusion."
    },

    {
        "section": "Experience",
        "question": "Explain one pipeline you built",
        "good": "Clear flow with tools, transformations, challenges.",
        "red": "Generic or unclear role."
    },

    {
        "section": "Experience",
        "question": "Biggest issue faced and resolution?",
        "good": "Performance/data quality issue with clear solution.",
        "red": "No real example."
    },

    {
        "section": "Behavioral",
        "question": "Worked with different teams or stakeholders?",
        "good": "Collaboration, communication, alignment.",
        "red": "Blames others or unclear."
    },

    {
        "section": "Behavioral",
        "question": "Handled production failure?",
        "good": "Debugging, root cause analysis, fix.",
        "red": "No ownership or vague."
    },

    {
        "section": "Timeline",
        "question": "Walk through experience timeline",
        "good": "Clear, consistent explanation.",
        "red": "Gaps or inconsistencies."
    },

    {
        "section": "Timeline",
        "question": "Any career gaps?",
        "good": "Transparent explanation.",
        "red": "Hidden or inconsistent answers."
    }

]

# =====================================================
# TITLE
# =====================================================

st.title("🚀 Data Engineering Interview Evaluation")

# =====================================================
# TABLE HEADER
# =====================================================

h1, h2, h3, h4, h5 = st.columns([1.5, 3, 4, 4, 1])

with h1:
    st.markdown("### Section")

with h2:
    st.markdown("### Question")

with h3:
    st.markdown("### Good Signals")

with h4:
    st.markdown("### Red Flags")

with h5:
    st.markdown("### Score")

st.divider()

# =====================================================
# QUESTIONS
# =====================================================

for index, item in enumerate(questions):

    col1, col2, col3, col4, col5 = st.columns([1.5, 3, 4, 4, 1])

    # SECTION
    with col1:
        st.markdown(f"""
        <div style="
            background:#EAF2FF;
            padding:15px;
            border-radius:8px;
            font-weight:bold;
            text-align:center;">
            {item['section']}
        </div>
        """, unsafe_allow_html=True)

    # QUESTION
    with col2:
        st.markdown(f"""
        <div style="
            background:white;
            padding:15px;
            border-radius:8px;
            border-left:5px solid #0D5EA6;
            min-height:120px;">
            <b>{item['question']}</b>
        </div>
        """, unsafe_allow_html=True)

    # GOOD SIGNALS
    with col3:
        st.markdown(f"""
        <div style="
            background:#F0FFF4;
            padding:15px;
            border-radius:8px;
            border-left:5px solid green;
            min-height:120px;">
            {item['good']}
        </div>
        """, unsafe_allow_html=True)

    # RED FLAGS
    with col4:
        st.markdown(f"""
        <div style="
            background:#FFF5F5;
            padding:15px;
            border-radius:8px;
            border-left:5px solid red;
            min-height:120px;">
            {item['red']}
        </div>
        """, unsafe_allow_html=True)

    # SCORE
    with col5:
        st.number_input(
            "",
            min_value=0,
            max_value=10,
            value=0,
            key=f"score_{index}"
        )

    st.divider()
