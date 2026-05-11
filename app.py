# =====================================================
# QUESTION DISPLAY
# =====================================================

questions = [

    {
        "question": "What is ETL vs ELT?",
        "good": "ETL transforms before load; ELT transforms after load (in warehouse/lake)",
        "red": "Cannot differentiate clearly"
    },

    {
        "question": "What is a data pipeline?",
        "good": "End-to-end flow: source, ingestion, transformation, storage",
        "red": "Very generic or unclear explanation"
    },

    {
        "question": "What is partitioning and why is it used?",
        "good": "Improves performance; reduces data scan; used in big data",
        "red": "No idea or vague explanation"
    },

    {
        "question": "What is schema evolution?",
        "good": "Handling changes in data structure over time",
        "red": "Cannot explain or no exposure"
    },

    {
        "question": "What is Azure Data Factory used for?",
        "good": "Orchestration, data movement, pipelines, integration",
        "red": "Calls it only ETL tool without orchestration context"
    }

]

# =====================================================
# TABLE HEADER
# =====================================================

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

# =====================================================
# QUESTIONS LOOP
# =====================================================

for index, item in enumerate(questions):

    col1, col2, col3, col4 = st.columns([3,4,4,1])

    # ==========================================
    # QUESTION
    # ==========================================

    with col1:

        st.markdown(f"""
        <div class="question-card">
            <b>{item['question']}</b>
        </div>
        """, unsafe_allow_html=True)

    # ==========================================
    # GOOD SIGNALS
    # ==========================================

    with col2:

        st.markdown(f"""
        <div class="question-card"
             style="border-left:6px solid green;">
            {item['good']}
        </div>
        """, unsafe_allow_html=True)

    # ==========================================
    # RED FLAGS
    # ==========================================

    with col3:

        st.markdown(f"""
        <div class="question-card"
             style="border-left:6px solid red;">
            {item['red']}
        </div>
        """, unsafe_allow_html=True)

    # ==========================================
    # SCORE
    # ==========================================

    with col4:

        st.number_input(
            "",
            min_value=0,
            max_value=10,
            value=0,
            key=f"score_{index}"
        )

    st.divider()
