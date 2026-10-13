
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load the dataset
df = pd.read_csv("data/spacex_launch_dash.csv")

# Check the expected columns:
# Launch Site, class, Payload Mass (kg)

app = Dash(__name__)

launch_sites = sorted(df["Launch Site"].dropna().unique())

app.layout = html.Div([
    html.H1(
        "SpaceX Launch Records Dashboard",
        style={"textAlign": "center"}
    ),

    html.Label("Select Launch Site:"),

    dcc.Dropdown(
        id="site-dropdown",
        options=[
            {"label": "All Sites", "value": "ALL"}
        ] + [
            {"label": site, "value": site}
            for site in launch_sites
        ],
        value="ALL",
        clearable=False
    ),

    dcc.Graph(id="success-pie-chart"),

    html.Label("Select Payload Range (kg):"),

    dcc.RangeSlider(
        id="payload-slider",
        min=0,
        max=int(df["Payload Mass (kg)"].max() // 1000 * 1000 + 1000),
        step=100,
        value=[
            0,
            int(df["Payload Mass (kg)"].max() // 1000 * 1000 + 1000)
        ],
        marks=None,
        tooltip={"placement": "bottom", "always_visible": True}
    ),

    dcc.Graph(id="success-payload-scatter-chart")
])


@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value")
)
def update_pie_chart(selected_site):
    if selected_site == "ALL":
        successful = df[df["class"] == 1]
        counts = successful.groupby("Launch Site").size()
        fig = px.pie(
            values=counts.values,
            names=counts.index,
            title="Total Successful Launches by Site"
        )
    else:
        site_df = df[df["Launch Site"] == selected_site]
        counts = (
            site_df["class"]
            .value_counts()
            .reindex([0, 1], fill_value=0)
        )
        fig = px.pie(
            values=counts.values,
            names=["Failure", "Success"],
            title=f"Launch Outcomes: {selected_site}"
        )

    return fig


@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    Input("site-dropdown", "value"),
    Input("payload-slider", "value")
)
def update_scatter_chart(selected_site, payload_range):
    filtered = df[
        df["Payload Mass (kg)"].between(
            payload_range[0], payload_range[1]
        )
    ]

    if selected_site != "ALL":
        filtered = filtered[
            filtered["Launch Site"] == selected_site
        ]

    fig = px.scatter(
        filtered,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category"
        if "Booster Version Category" in filtered.columns
        else None,
        hover_data=["Launch Site"],
        title="Payload Mass vs. Landing Success",
        labels={"class": "Landing Success (0 = Failure, 1 = Success)"}
    )

    fig.update_yaxes(tickvals=[0, 1])
    return fig


if __name__ == "__main__":
    app.run(debug=True)
