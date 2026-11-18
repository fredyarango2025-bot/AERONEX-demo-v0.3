import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AERONEX™",
    page_icon="✈️",
    layout="wide"
)

# ===============================
# Datos Demo
# ===============================

initiatives = pd.DataFrame(
    [
        {
            "Code": "CAPEX-001",
            "Initiative": "Terminal Expansion",
            "Capex": 50000000,
            "Stage": 7,
            "Stage Name": "Construction",
            "Governance": "Approved",
            "Engineering": "Detailed Engineering",
            "Construction": "Civil Works",
            "Progress": 68
        },
        {
            "Code": "CAPEX-002",
            "Initiative": "Baggage Handling System",
            "Capex": 20000000,
            "Stage": 5,
            "Stage Name": "Final Engineering",
            "Governance": "Approved",
            "Engineering": "Basic Engineering",
            "Construction": "Not Started",
            "Progress": 30
        },
        {
            "Code": "CAPEX-003",
            "Initiative": "Runway Rehabilitation",
            "Capex": 15000000,
            "Stage": 9,
            "Stage Name": "Operational Readiness",
            "Governance": "Executing",
            "Engineering": "Engineering Complete",
            "Construction": "Commissioning",
            "Progress": 95
        },
        {
            "Code": "CAPEX-004",
            "Initiative": "Solar Farm",
            "Capex": 8000000,
            "Stage": 3,
            "Stage Name": "Conceptual Engineering",
            "Governance": "Evaluating",
            "Engineering": "Conceptual Design",
            "Construction": "Not Started",
            "Progress": 15
        }
    ]
)

# ===============================
# KPIs
# ===============================

total_capex = initiatives["Capex"].sum()

projects = len(initiatives)

avg_progress = initiatives["Progress"].mean()

ready_for_recognition = len(
    initiatives[
        initiatives["Stage"] >= 8
    ]
)

# ===============================
# Header
# ===============================

st.title("✈️ AERONEX™")
st.caption(
    "Airport CAPEX Governance Platform - Demo v0.3"
)

# ===============================
# KPIs
# ===============================

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Projects",
    projects
)

c2.metric(
    "CAPEX Portfolio",
    f"USD {total_capex:,.0f}"
)

c3.metric(
    "Avg Progress",
    f"{avg_progress:.1f}%"
)

c4.metric(
    "Recognition Ready",
    ready_for_recognition
)

st.divider()

# ===============================
# CAPEX Chart
# ===============================

st.subheader("CAPEX Portfolio")

fig_capex = px.bar(
    initiatives,
    x="Initiative",
    y="Capex",
    color="Stage Name"
)

st.plotly_chart(
    fig_capex,
    use_container_width=True
)

# ===============================
# Development Stages
# ===============================

st.subheader("Development Stage Distribution")

fig_stage = px.pie(
    initiatives,
    names="Stage Name"
)

st.plotly_chart(
    fig_stage,
    use_container_width=True
)

# ===============================
# Projects Table
# ===============================

st.subheader("CAPEX Portfolio")

st.dataframe(
    initiatives,
    use_container_width=True
)

# ===============================
# Recognition Engine
# ===============================

st.subheader("Recognition Engine")

eligible = initiatives[
    initiatives["Stage"] >= 8
]

st.success(
    f"{len(eligible)} project(s) eligible for CAPEX recognition."
)

st.dataframe(
    eligible[
        [
            "Code",
            "Initiative",
            "Stage Name",
            "Progress"
        ]
    ],
    use_container_width=True
)

# ===============================
# LAP / OSITRAN Stages
# ===============================

st.subheader("LAP / OSITRAN Development Framework")

st.markdown(
"""
1. Planning

2. Programming

3. Conceptual Engineering

4. Preliminary Engineering

5. Final Engineering

6. Procurement

7. Construction

8. Formal Completion

9. Operational Readiness

10. Final Acceptance
"""
)

# ===============================
# Footer
# ===============================

st.divider()

st.caption(
    "AERONEX™ Demo v0.3 | LAP + OSITRAN Governance Model"
)
