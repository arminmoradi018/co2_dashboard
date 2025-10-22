from shiny import ui
from data_loader import co2_data, countries




app_ui = ui.page_fluid(
    ui.panel_title("Global CO₂ Emissions Dashboard", window_title="CO2 Dashboard"),
    
    ui.navset_pill(
        
        ui.nav_panel(
            "Country - CO2 Time Series",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_select(
                        id="country",
                        label="Select Country",
                        choices=countries,
                        selected="Austria"
                    ),
                    ui.input_slider(
                        id="window",
                        label="Rolling mean years",
                        min=1,
                        max=20,
                        value=5
                    ),
                    width=300
                ),
                ui.output_ui("time_series_plot")
            )
        ),
        
        ui.nav_panel(
            "World Map - CO2 Emissions per Country",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_slider(
                        id="year",
                        label="Year",
                        min=int(co2_data["year"].min()),
                        max=int(co2_data["year"].max()),
                        value=2020
                    ),
                    width=300
                ),
                ui.output_ui("world_map_plot")
            )
        )
    )
)