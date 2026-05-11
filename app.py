import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Miracle Interview Evaluation Portal",
    layout="wide",
    page_icon="🚀"
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
    margin-bottom: 10px;
}}

.sub-title {{
    font-size: 18px;
    color: #94A3B8;
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
            "section": "ADF",
            "question": "What is Azure Data Factory used for?",
            "good": "Orchestration, pipelines, integration.",
            "red": "Only calls it ETL tool."
        },

        {
            "section": "PySpark",
            "question": "What is PySpark?",
            "good": "Distributed processing using Spark.",
            "red": "Confuses with Python scripting."
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
            "question": "What is the difference between Import and DirectQuery?",
            "good": "Import stores data in model; DirectQuery queries source live.",
            "red": "Cannot explain performance implications."
        },

        {
            "section": "DAX",
            "question": "What is CALCULATE in DAX?",
            "good": "Modifies filter context.",
            "red": "Cannot explain context transition."
        },

        {
            "section": "DAX",
            "question": "Difference between Measure and Calculated Column?",
            "good": "Measure calculated dynamically; column stored physically.",
            "red": "Confuses both."
        },

        {
            "section": "Modeling",
            "question": "What is Star Schema?",
            "good": "Fact and dimension model for analytics.",
            "red": "No modeling understanding."
        },

        {
            "section": "Power Query",
            "question": "What is Query Folding?",
            "good": "Pushes transformations to source system.",
            "red": "No understanding of optimization."
        },

        {
            "section": "Visualization",
            "question": "How do you optimize Power BI reports?",
            "good": "Reduce visuals, optimize DAX, star schema, aggregations.",
            "red": "Only talks about UI formatting."
        },

        {
            "section": "Experience",
            "question": "Explain a dashboard you built",
            "good": "Business problem, KPIs, data sources, impact.",
            "red": "Only talks about charts."
        }

    ],

    # =================================================
    # ARCHITECT
    # =================================================

    "Architect": [

        {
            "section": "Architecture",
            "question": "Design an end-to-end data platform for reporting",
            "good": "Mentions ingestion, transformation, serving, governance.",
            "red": "Only lists tools."
        },

        {
            "section": "Architecture",
            "question": "When would you NOT use Medallion architecture?",
            "good": "Small datasets, real-time simplicity trade-offs.",
            "red": "Says always use it."
        },

        {
            "section": "Architecture",
            "question": "How do you decide between batch vs streaming?",
            "good": "Latency, cost, use-case decision.",
            "red": "No criteria."
        },

        {
            "section": "Cloud",
            "question": "Compare Fabric, Databricks, Synapse",
            "good": "Explains strengths and use cases.",
            "red": "Only lists tools."
        },

        {
            "section": "Orchestration",
            "question": "How do you design resilient pipelines?",
            "good": "Retries, monitoring, idempotency.",
            "red": "No failure handling."
        },

        {
            "section": "Modeling",
            "question": "Difference between OLTP and OLAP?",
            "good": "Transactional vs analytical.",
            "red": "Cannot explain clearly."
        },

        {
            "section": "Power BI",
            "question": "How does Power BI fit into architecture?",
            "good": "Consumes curated Gold layer.",
            "red": "No integration clarity."
        },

        {
            "section": "Experience",
            "question": "Explain one architecture you designed",
            "good": "Ownership, trade-offs, challenges.",
            "red": "Very generic explanation."
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

h1, h2, h3, h4, h5 = st.columns([1.5, 3, 4, 4, 1])

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

st.divider()

st.metric(
    label=f"⭐ {selected_role} Interview Score",
    value=f"{total_score} / {len(questions) * 10}"
)
