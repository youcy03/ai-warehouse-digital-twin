import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Warehouse Digital Twin",
    page_icon="📦",
    layout="wide"
)


# ============================================================
# CUSTOM DESIGN
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at top left,
                rgba(124, 58, 237, 0.10),
                transparent 30%
            ),
            radial-gradient(
                circle at top right,
                rgba(6, 182, 212, 0.08),
                transparent 30%
            ),
            #090D18;

        color: #E5E7EB;
    }

    .main .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #101628 0%,
                #0B1020 100%
            );

        border-right: 1px solid rgba(255, 255, 255, 0.06);
    }

    section[data-testid="stSidebar"] * {
        color: #F8FAFC !important;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background-color: #131B2F;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
    }

    h1 {
        color: #F8FAFC !important;
        font-size: 2.7rem !important;
        font-weight: 750 !important;
        letter-spacing: -1px;
    }

    h2, h3 {
        color: #F1F5F9 !important;
        font-weight: 700 !important;
    }

    p {
        color: #AAB4C6;
    }

    .top-badge {
        display: inline-block;

        background:
            linear-gradient(
                90deg,
                rgba(124, 58, 237, 0.95),
                rgba(6, 182, 212, 0.95)
            );

        padding: 7px 14px;
        border-radius: 999px;
        color: white !important;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.4px;
        margin-bottom: 10px;

        box-shadow:
            0 5px 20px rgba(124, 58, 237, 0.22);
    }

    div[data-testid="stMetric"] {
        background:
            linear-gradient(
                145deg,
                rgba(22, 30, 52, 0.95),
                rgba(15, 22, 39, 0.95)
            );

        border:
            1px solid rgba(255, 255, 255, 0.07);

        padding: 20px;
        border-radius: 18px;

        box-shadow:
            0 10px 30px rgba(0, 0, 0, 0.23);

        min-height: 125px;
    }

    div[data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
        font-size: 13px !important;
    }

    div[data-testid="stMetricValue"] {
        color: #F8FAFC !important;
        font-size: 32px !important;
        font-weight: 750 !important;
    }

    div[data-testid="stDataFrame"] {
        border:
            1px solid rgba(255,255,255,0.07);

        border-radius: 16px;
        overflow: hidden;

        box-shadow:
            0 10px 30px rgba(0,0,0,0.18);
    }

    hr {
        border: none;
        border-top: 1px solid rgba(255,255,255,0.07);
        margin-top: 2.2rem;
        margin-bottom: 2.2rem;
    }

    [data-testid="stCaptionContainer"] {
        color: #7F8CA3 !important;
    }

    .info-card {
        background:
            linear-gradient(
                145deg,
                rgba(22, 30, 52, 0.95),
                rgba(15, 22, 39, 0.95)
            );

        border:
            1px solid rgba(255,255,255,0.07);

        padding: 22px;
        border-radius: 18px;

        box-shadow:
            0 10px 30px rgba(0,0,0,0.20);

        margin-top: 10px;
        margin-bottom: 18px;
        min-height: 120px;
    }

    .info-title {
        color: #8B5CF6 !important;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .info-value {
        color: #F8FAFC !important;
        font-size: 19px;
        font-weight: 700;
        margin-top: 8px;
    }

    .info-small {
        color: #94A3B8 !important;
        font-size: 13px;
        margin-top: 6px;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

final_decisions = pd.read_csv(
    "data/final_decisions.csv"
)

scenario_comparison = pd.read_csv(
    "data/scenario_comparison.csv"
)

recommendation_summary = pd.read_csv(
    "data/recommendation_summary.csv"
)

future_forecasts = pd.read_csv(
    "data/future_forecasts_14d.csv"
)

current_simulation = pd.read_csv(
    "data/current_policy_simulation.csv"
)


# ============================================================
# DATE CONVERSION
# ============================================================

future_forecasts["date"] = pd.to_datetime(
    future_forecasts["date"]
)

current_simulation["date"] = pd.to_datetime(
    current_simulation["date"]
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("AI Warehouse")
st.sidebar.caption("Digital Twin Control Center")

st.sidebar.write(
    "Decision-support dashboard combining machine-learning "
    "forecasting, inventory simulation and replenishment analysis."
)

st.sidebar.divider()

selected_product = st.sidebar.selectbox(
    "Select Product",
    final_decisions["product_id"].tolist()
)

st.sidebar.divider()

st.sidebar.caption(
    "14-Day Inventory Planning Horizon"
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="top-badge">AI-POWERED INVENTORY ANALYTICS</div>',
    unsafe_allow_html=True
)

st.title("AI Warehouse Digital Twin")

st.write(
    "Demand forecasting, inventory simulation and "
    "replenishment decision support in one interactive dashboard."
)


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_products = (
    final_decisions["product_id"]
    .nunique()
)

critical_products = (
    final_decisions[
        final_decisions["recommendation"]
        == "Replenish Immediately"
    ]["product_id"]
    .nunique()
)

average_service_level = (
    final_decisions["service_level"]
    .mean()
)

total_stockout = (
    final_decisions["stockout_qty"]
    .sum()
)


# ============================================================
# KPI CARDS
# ============================================================

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    "Total Products",
    total_products
)

kpi2.metric(
    "Immediate Replenishment",
    critical_products
)

kpi3.metric(
    "Average Service Level",
    f"{average_service_level:.2f}%"
)

kpi4.metric(
    "Total Stockout Units",
    f"{int(total_stockout):,}"
)

st.caption(
    "Metrics above represent the current replenishment policy "
    "under the 14-day inventory simulation."
)


# ============================================================
# SCENARIO PERFORMANCE
# ============================================================

st.divider()

st.subheader("Scenario Performance")

scenario_col1, scenario_col2 = st.columns(2)


with scenario_col1:

    st.markdown("#### Service Level Comparison")

    fig_service = px.bar(
        scenario_comparison,
        x="Scenario",
        y="Service Level (%)",
        color="Scenario",
        text="Service Level (%)",
        color_discrete_sequence=[
            "#8B5CF6",
            "#06B6D4"
        ]
    )

    fig_service.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside",
        marker_line_width=0
    )

    fig_service.update_layout(
        height=390,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),
        showlegend=False,

        xaxis=dict(
            title="",
            showgrid=False,
            color="#94A3B8"
        ),

        yaxis=dict(
            title="Service Level (%)",
            gridcolor="rgba(255,255,255,0.06)",
            color="#94A3B8"
        ),

        margin=dict(
            l=30,
            r=20,
            t=20,
            b=30
        )
    )

    st.plotly_chart(
        fig_service,
        use_container_width=True
    )


with scenario_col2:

    st.markdown("#### Stockout Comparison")

    fig_stockout = px.bar(
        scenario_comparison,
        x="Scenario",
        y="Stockout Quantity",
        color="Scenario",
        text="Stockout Quantity",
        color_discrete_sequence=[
            "#EC4899",
            "#22D3EE"
        ]
    )

    fig_stockout.update_traces(
        textposition="outside",
        marker_line_width=0
    )

    fig_stockout.update_layout(
        height=390,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),
        showlegend=False,

        xaxis=dict(
            title="",
            showgrid=False,
            color="#94A3B8"
        ),

        yaxis=dict(
            title="Stockout Units",
            gridcolor="rgba(255,255,255,0.06)",
            color="#94A3B8"
        ),

        margin=dict(
            l=30,
            r=20,
            t=20,
            b=30
        )
    )

    st.plotly_chart(
        fig_stockout,
        use_container_width=True
    )


with st.expander(
    "View Scenario Comparison Data",
    expanded=False
):

    st.dataframe(
        scenario_comparison,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PRODUCT EXPLORER
# ============================================================

st.divider()

st.subheader(
    f"Product Explorer — {selected_product}"
)

selected_row = final_decisions[
    final_decisions["product_id"]
    == selected_product
].iloc[0]


product_kpi1, product_kpi2, product_kpi3, product_kpi4 = (
    st.columns(4)
)

product_kpi1.metric(
    "Current Stock",
    int(selected_row["current_stock"])
)

product_kpi2.metric(
    "Days of Supply",
    f"{selected_row['days_of_supply']:.2f}"
)

product_kpi3.metric(
    "Service Level",
    f"{selected_row['service_level']:.2f}%"
)

product_kpi4.metric(
    "Stockout Days",
    int(selected_row["stockout_days"])
)


# ============================================================
# PRODUCT DECISION CARDS
# ============================================================

decision_col1, decision_col2, decision_col3 = st.columns(3)

with decision_col1:
    st.markdown(
        f"""<div class="info-card">
<div class="info-title">Recommendation</div>
<div class="info-value">{selected_row["recommendation"]}</div>
<div class="info-small">Final decision generated by the decision engine</div>
</div>""",
        unsafe_allow_html=True
    )

with decision_col2:
    st.markdown(
        f"""<div class="info-card">
<div class="info-title">Replenishment Priority</div>
<div class="info-value">{selected_row["replenishment_priority"]}</div>
<div class="info-small">Based on stock coverage and simulation performance</div>
</div>""",
        unsafe_allow_html=True
    )

with decision_col3:
    st.markdown(
        f"""<div class="info-card">
<div class="info-title">Recommended Reorder</div>
<div class="info-value">{int(selected_row["forecast_based_reorder_qty"])} units</div>
<div class="info-small">Forecast-informed replenishment quantity</div>
</div>""",
        unsafe_allow_html=True
    )


# ============================================================
# FILTER PRODUCT DATA
# ============================================================

product_forecast = future_forecasts[
    future_forecasts["product_id"]
    == selected_product
].copy()

product_simulation = current_simulation[
    current_simulation["product_id"]
    == selected_product
].copy()


# ============================================================
# PRODUCT CHARTS
# ============================================================

chart_col1, chart_col2 = st.columns(2)


with chart_col1:

    st.markdown("#### 14-Day Demand Forecast")

    fig_forecast = go.Figure()

    fig_forecast.add_trace(
        go.Scatter(
            x=product_forecast["date"],
            y=product_forecast["forecast_units"],

            mode="lines+markers",

            line=dict(
                width=3,
                color="#22D3EE"
            ),

            marker=dict(
                size=7,
                color="#A855F7"
            ),

            fill="tozeroy",

            fillcolor="rgba(34,211,238,0.08)"
        )
    )

    fig_forecast.update_layout(
        height=400,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),

        xaxis=dict(
            title="Date",
            gridcolor="rgba(255,255,255,0.05)"
        ),

        yaxis=dict(
            title="Forecast Units",
            gridcolor="rgba(255,255,255,0.05)"
        ),

        margin=dict(
            l=30,
            r=20,
            t=20,
            b=30
        ),

        showlegend=False
    )

    st.plotly_chart(
        fig_forecast,
        use_container_width=True
    )


with chart_col2:

    st.markdown("#### Inventory Evolution")

    fig_inventory = go.Figure()

    fig_inventory.add_trace(
        go.Scatter(
            x=product_simulation["date"],
            y=product_simulation["ending_stock"],

            mode="lines+markers",

            line=dict(
                width=3,
                color="#8B5CF6"
            ),

            marker=dict(
                size=7,
                color="#EC4899"
            ),

            fill="tozeroy",

            fillcolor="rgba(139,92,246,0.08)"
        )
    )

    fig_inventory.update_layout(
        height=400,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),

        xaxis=dict(
            title="Date",
            gridcolor="rgba(255,255,255,0.05)"
        ),

        yaxis=dict(
            title="Ending Stock",
            gridcolor="rgba(255,255,255,0.05)"
        ),

        margin=dict(
            l=30,
            r=20,
            t=20,
            b=30
        ),

        showlegend=False
    )

    st.plotly_chart(
        fig_inventory,
        use_container_width=True
    )


# ============================================================
# DECISION ENGINE OVERVIEW
# ============================================================

st.divider()

st.subheader("Decision Engine Overview")

decision_chart_col, priority_table_col = (
    st.columns([1, 1.4])
)


with decision_chart_col:

    st.markdown(
        "#### Recommendation Distribution"
    )

    fig_recommendations = px.pie(
        recommendation_summary,
        names="recommendation",
        values="product_count",
        hole=0.60,

        color_discrete_sequence=[
            "#8B5CF6",
            "#22D3EE",
            "#EC4899",
            "#3B82F6",
            "#22C55E"
        ]
    )

    fig_recommendations.update_layout(
        height=430,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),

        legend=dict(
            orientation="h",
            y=-0.15
        )
    )

    st.plotly_chart(
        fig_recommendations,
        use_container_width=True
    )


with priority_table_col:

    st.markdown(
        "#### Highest Priority Products"
    )

    top_products = final_decisions.head(5)

    top_priority_table = top_products[
        [
            "product_id",
            "replenishment_priority",
            "service_level",
            "stockout_days",
            "forecast_based_reorder_qty",
            "recommendation"
        ]
    ].copy()

    top_priority_table = (
        top_priority_table
        .rename(
            columns={
                "product_id":
                    "Product",

                "replenishment_priority":
                    "Priority",

                "service_level":
                    "Service Level (%)",

                "stockout_days":
                    "Stockout Days",

                "forecast_based_reorder_qty":
                    "Reorder Qty",

                "recommendation":
                    "Recommendation"
            }
        )
    )

    st.dataframe(
        top_priority_table,
        use_container_width=True,
        hide_index=True,
        height=380
    )


# ============================================================
# FINAL PRODUCT RECOMMENDATIONS
# ============================================================

st.divider()

st.subheader("Final Product Recommendations")

recommendations_table = final_decisions[
    [
        "product_id",
        "current_stock",
        "days_of_supply",
        "service_level",
        "stockout_days",
        "forecast_based_reorder_qty",
        "replenishment_priority",
        "recommendation"
    ]
].copy()

recommendations_table = (
    recommendations_table
    .rename(
        columns={
            "product_id":
                "Product",

            "current_stock":
                "Current Stock",

            "days_of_supply":
                "Days of Supply",

            "service_level":
                "Service Level (%)",

            "stockout_days":
                "Stockout Days",

            "forecast_based_reorder_qty":
                "Reorder Qty",

            "replenishment_priority":
                "Priority",

            "recommendation":
                "Recommendation"
        }
    )
)

st.dataframe(
    recommendations_table,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Warehouse Digital Twin • "
    "ML Demand Forecasting • "
    "Inventory Simulation • "
    "Decision Support"
)