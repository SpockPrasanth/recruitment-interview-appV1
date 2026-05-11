import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Miracle Interview Evaluation Portal",
    layout="wide",
    page_icon="Ⓜ️"
)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("⚙ Settings")

role_options = {
    "🛠 Data Engineer": "Data Engineer",
    "📊 BI Engineer": "BI Engineer",
    "🏗 Architect": "Architect"
}

selected_display = st.sidebar.selectbox(
    "Select Interview Role",
    list(role_options.keys())
)

selected_role = role_options[selected_display]

theme = st.sidebar.toggle(
    "🌙 Dark Mode",
    value=True
)

# =====================================================
# ROLE ICONS
# =====================================================

role_icons = {
    "Data Engineer": "🛠",
    "BI Engineer": "📊",
    "Architect": "🏗"
}

# =====================================================
# THEME COLORS
# =====================================================

if theme:

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
    font-size: 34px;
    font-weight: 700;
    color: {text_color};
    margin-bottom: 8px;
}}

.sub-title {{
    font-size: 16px;
    color: #94A3B8;
    margin-bottom: 25px;
}}

.header-box {{
    background: {header_bg};
    color: white;
    padding: 12px;
    border-radius: 8px;
    text-align: center;
    font-weight: bold;
    font-size: 16px;
}}

.card {{
    padding: 12px;
    border-radius: 10px;
    min-height: 90px;
    font-size: 14px;
    box-shadow: 0px 1px 5px rgba(0,0,0,0.12);
}}

</style>
""", unsafe_allow_html=True)

# =====================================================
# QUESTION BANK
# =====================================================

question_bank = {

    # =================================================
    # DATA ENGINEER
    # =================================================

    "Data Engineer": [

        {
            "section": "Fundamentals",
            "question": "What is ETL vs ELT?",
            "good": "ETL transforms before load; ELT transforms after load.",
            "red": "Cannot differentiate clearly."
        },

        {
            "section": "Fundamentals",
            "question": "What is a data pipeline?",
            "good": "End-to-end flow explanation.",
            "red": "Very generic answer."
        },

        {
            "section": "Data Engineering",
            "question": "What is partitioning and why is it used?",
            "good": "Improves performance and reduces data scan.",
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
            "good": "Orchestration, data movement, pipelines.",
            "red": "Only calls it ETL tool."
        },

        {
            "section": "ADF",
            "question": "Difference between pipeline and data flow?",
            "good": "Pipeline orchestrates; Data Flow transforms.",
            "red": "Confuses both."
        },

        {
            "section": "ADF",
            "question": "What are triggers in ADF?",
            "good": "Schedule/event-based execution.",
            "red": "No idea."
        },

        {
            "section": "PySpark",
            "question": "What is PySpark?",
            "good": "Distributed processing using Spark.",
            "red": "Confuses with Python scripting."
        },

        {
            "section": "PySpark",
            "question": "Difference between RDD and DataFrame?",
            "good": "DataFrames optimized and structured.",
            "red": "No understanding."
        },

        {
            "section": "Architecture",
            "question": "Explain Medallion Architecture",
            "good": "Bronze, Silver, Gold layers.",
            "red": "Cannot explain layers."
        },

        {
            "section": "Experience",
            "question": "Explain one pipeline you built",
            "good": "Clear architecture and transformations.",
            "red": "Very generic explanation."
        }

    ],

    # =================================================
    # BI ENGINEER
    # =================================================

    "BI Engineer": [

        {
            "section": "Power BI",
            "question": "Import vs DirectQuery?",
            "good": "Import stores data; DirectQuery queries live.",
            "red": "Cannot explain performance."
        },

        {
            "section": "DAX",
            "question": "What is CALCULATE in DAX?",
            "good": "Modifies filter context.",
            "red": "Cannot explain."
        },

        {
            "section": "DAX",
            "question": "Measure vs Calculated Column?",
            "good": "Measure dynamic; column stored physically.",
            "red": "Confuses both."
        },

        {
            "section": "Modeling",
            "question": "What is Star Schema?",
            "good": "Fact and dimension model.",
            "red": "No understanding."
        },

        {
            "section": "Power Query",
            "question": "What is Query Folding?",
            "good": "Pushes transformations to source.",
            "red": "No optimization understanding."
        },

        {
            "section": "Visualization",
            "question": "How do you optimize Power BI reports?",
            "good": "Optimize DAX and reduce visuals.",
            "red": "Only talks UI."
        },

        {
            "section": "Experience",
            "question": "Explain a dashboard you built",
            "good": "Business impact and KPIs.",
            "red": "Only talks visuals."
        }

    ],

    # =================================================
    # ARCHITECT
    # =================================================

    "Architect": [

        {
            "section": "Architecture",
            "question": "Design end-to-end data platform",
            "good": "Mentions ingestion, storage, governance.",
            "red": "Only lists tools."
        },

        {
            "section": "Architecture",
            "question": "When NOT to use Medallion?",
            "good": "Small datasets and real-time trade-offs.",
            "red": "Always use it."
        },

        {
            "section": "Architecture",
            "question": "Batch vs Streaming?",
            "good": "Latency and use-case driven.",
            "red": "No criteria."
        },

        {
            "section": "Cloud",
            "question": "Compare Fabric, Databricks, Synapse",
            "good": "Explains use cases and strengths.",
            "red": "Only lists tools."
        },

        {
            "section": "Orchestration",
            "question": "How do you design resilient pipelines?",
            "good": "Retries, logging, monitoring.",
            "red": "No failure handling."
        },

        {
            "section": "Modeling",
            "question": "Difference between OLTP and OLAP?",
            "good": "Transactional vs analytical.",
            "red": "Cannot explain."
        },

        {
            "section": "Power BI",
            "question": "How does Power BI fit architecture?",
            "good": "Consumes curated Gold layer.",
            "red": "No clarity."
        },

        {
            "section": "Experience",
            "question": "Explain one architecture designed",
            "good": "Ownership and trade-offs.",
            "red": "Generic explanation."
        }

    ]

}

# =====================================================
# ROLE QUESTIONS
# =====================================================

questions = question_bank[selected_role]

# =====================================================
# TITLE
# =====================================================

st.markdown(f"""
<div class="main-title">
{role_icons[selected_role]} {selected_role} Miracle Interview Evaluation
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">
Professional Interview Assessment Portal
</div>
""", unsafe_allow_html=True)

# =====================================================
# TABLE HEADER
# =====================================================

h1, h2, h3, h4, h5 = st.columns([1.2, 3, 4, 4, 1])

headers = [
    "Section",
    "Question",
    "Good Signals",
    "Red Flags",
    "Score"
]

for col, header in zip([h1, h2, h3, h4, h5], headers):

    with col:
        st.markdown(
            f'<div class="header-box">{header}</div>',
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# QUESTIONS LOOP
# =====================================================

for index, item in enumerate(questions):

    col1, col2, col3, col4, col5 = st.columns([1.2, 3, 4, 4, 1])

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

    with col2:

        st.markdown(f"""
        <div class="card"
            style="
            background:{question_bg};
            color:{text_color};
            border-left:5px solid #3B82F6;">
            <b>{item['question']}</b>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown(f"""
        <div class="card"
            style="
            background:{good_bg};
            color:{good_text};
            border-left:5px solid #22C55E;">
            {item['good']}
        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.markdown(f"""
        <div class="card"
            style="
            background:{red_bg};
            color:{red_text};
            border-left:5px solid #EF4444;">
            {item['red']}
        </div>
        """, unsafe_allow_html=True)

    with col5:

        st.number_input(
            "",
            min_value=0,
            max_value=10,
            value=0,
            step=1,
            key=f"{selected_role}_score_{index}"
        )

    st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# TOTAL SCORE
# =====================================================

total_score = 0

for index in range(len(questions)):

    total_score += st.session_state[
        f"{selected_role}_score_{index}"
    ]

max_score = len(questions) * 10

percentage = round((total_score / max_score) * 100)

# =====================================================
# FINAL RESULT
# =====================================================

if percentage < 60:

    result = "❌ Reject"

elif percentage <= 80:

    result = "🟡 Average Candidate"

else:

    result = "✅ Strong Candidate - Present to Data Team"

# =====================================================
# DISPLAY METRICS
# =====================================================

st.divider()

m1, m2, m3 = st.columns(3)

with m1:

    st.metric(
        "⭐ Total Score",
        f"{total_score} / {max_score}"
    )

with m2:

    st.metric(
        "📊 Percentage",
        f"{percentage}%"
    )

with m3:

    st.metric(
        "🎯 Final Result",
        result
    )
