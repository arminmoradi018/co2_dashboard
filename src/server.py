from shiny import render, ui
import plotly.express as px
from data_loader import co2_data

def server(input, output, session):
    @output
    @render.ui
    def time_series_plot():
        """
        Render line chart of CO2 emissions for selected country
        with rolling mean applied.
        """
        country_data = co2_data[co2_data["country"] == input.country()]
        window = input.window()
        country_data = country_data.sort_values("year")
        country_data["co2_smoothed"] = country_data["co2"].rolling(window=window, center=True).mean()
        
        fig = px.line(
            country_data,
            x="year",
            y=["co2", "co2_smoothed"],
            labels={
                "year": "Year",
                "value": "CO2 [million t] ",
                "variable": "Metric"
            },
            title=f"CO2 Emissions -- {input.country()}",
            color_discrete_map={
                "co2": "blue",
                "co2_smoothed": "red"
            }
        )
        fig.update_layout(
            hovermode="x unified",
            legend_title_text="",
            plot_bgcolor="white",
            margin=dict(t=40)
        )
        fig.for_each_trace(lambda t: t.update(name="Actual" if t.name == "co2" else f"{window}-year-mean"))
        
        return ui.HTML(fig.to_html(full_html=False))

    @output
    @render.ui
    def world_map_plot():
        """
        Render choropleth map of global CO2 emissions for selected year.
        """
        year_data = co2_data[co2_data["year"] == input.year()]
        fig = px.choropleth(
            year_data,
            locations="iso_code",
            color="co2",
            hover_name="country",
            hover_data={"iso_code": True, "co2": ":.3f"},
            color_continuous_scale="Reds",
            labels={"co2": "CO2 [million t]"},
            title=f"CO2 emissions worldwide {input.year()}"
        )
        fig.update_layout(
            margin=dict(t=40),
            coloraxis_colorbar_title_text="CO2[million t]"
        )
        
        return ui.HTML(fig.to_html(full_html=False))