import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Data Engineering Interview Evaluation",
    layout="wide",
    page_icon="🚀"
)

# =====================================================
# THEME TOGGLE
# =====================================================

theme = st.sidebar.toggle("🌙 Dark Mode", value=True)

# =====================================================
# COLORS BASED ON THEME
# =====================================================

if theme:

    # DARK MODE

    bg_color = "#020817"
    text_color = "white"

    section_bg = "#1E293B"
    question_bg = "#111827"

    good_bg = "#052E16"
    good_text = "#DCFCE7"

    red_bg = "#450A0A"
    red_text = "#FECACA"

    header_bg = "#1D4ED8"

else:

    # LIGHT MODE

    bg_color = "#F8FAFC"
    text_color = "#111827"

    section_bg = "#DBEAFE"
    question_bg = "white"

    good_bg = "#DCFCE7"
    good_text = "#14532D"

    red_bg = "#FEE2E2"
    red_text = "#7F1D1D"

    header_bg = "#2563EB"

# =====================================================
# GLOBAL CSS
# =====================================================

st.markdown(f"""
<style>

.stApp {{
    background-color: {bg_color};
    color: {text_color};
}}

.main-title {{
    font-size: 42px;
    font-weight: 800;
    color: {text_color};
    margin-bottom: 30px;
}}

.header-box {{
    background: {header_bg};
    color: white;
    padding: 14px;
    border-radius: 10px;
    text-align: center;
    font-weight: bold;
    font-size: 18px;
}}

.card {{
    padding: 18px;
    border-radius: 12px;
    min-height: 120px;
    font-size: 16px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.15);
}}

</style>
""", unsafe_allow_html=True)

# =====================================================
# QUESTION BANK
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

st.markdown("""
<div class="main-title">
🚀 Data Engineering Interview Evaluation
</div>
""", unsafe_allow_html=True)

# =====================================================
# TABLE HEADER
# =====================================================

h1, h2, h3, h4, h5 = st.columns([1.5, 3, 4, 4, 1])

with h1:
    st.markdown(
        '<div class="header-box">Section</div>',
        unsafe_allow_html=True
    )

with h2:
    st.markdown(
        '<div class="header-box">Question</div>',
        unsafe_allow_html=True
    )

with h3:
    st.markdown(
        '<div class="header-box">Good Signals</div>',
        unsafe_allow_html=True
    )

with h4:
    st.markdown(
        '<div class="header-box">Red Flags</div>',
        unsafe_allow_html=True
    )

with h5:
    st.markdown(
        '<div class="header-box">Score</div>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# QUESTIONS LOOP
# =====================================================

for index, item in enumerate(questions):

    col1, col2, col3, col4, col5 = st.columns([1.5, 3, 4, 4, 1])

    # SECTION

    with col1:

        st.markdown(f"""
        <div class="card"
            style="
            background:{section_bg};
            color:{text_color};
            text-align:center;
            font-weight:bold;">
            {item['section']}
        </div>
        """, unsafe_allow_html=True)

    # QUESTION

    with col2:

        st.markdown(f"""
        <div class="card"
            style="
            background:{question_bg};
            color:{text_color};
            border-left:6px solid #3B82F6;">
            <b>{item['question']}</b>
        </div>
        """, unsafe_allow_html=True)

    # GOOD SIGNALS

    with col3:

        st.markdown(f"""
        <div class="card"
            style="
            background:{good_bg};
            color:{good_text};
            border-left:6px solid #22C55E;">
            {item['good']}
        </div>
        """, unsafe_allow_html=True)

    # RED FLAGS

    with col4:

        st.markdown(f"""
        <div class="card"
            style="
            background:{red_bg};
            color:{red_text};
            border-left:6px solid #EF4444;">
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
            step=1,
            key=f"score_{index}"
        )

    st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# FINAL SCORE
# =====================================================

total_score = 0

for index in range(len(questions)):
    total_score += st.session_state[f"score_{index}"]

st.divider()

st.metric(
    label="⭐ Total Interview Score",
    value=f"{total_score} / {len(questions) * 10}"
)
