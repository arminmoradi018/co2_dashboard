import pytest
import pandas as pd
from bs4 import BeautifulSoup
import plotly.express as px
from src import data_loader


# ---------- 1. Test: Data Loading ----------
def test_data_loads_correctly():
    """Ensure CO₂ dataset loads properly and contains essential columns."""
    df = data_loader.load_data()
    assert isinstance(df, pd.DataFrame), "load_data() must return a DataFrame"
    assert not df.empty, "DataFrame is empty — dataset might be unavailable"
    expected_cols = {"country", "iso_code", "year", "co2"}
    assert expected_cols.issubset(df.columns), f"Missing columns: {expected_cols - set(df.columns)}"


# ---------- 2. Test: Data Caching ----------
def test_data_is_cached():
    """Verify that get_co2_data() uses caching (same object returned twice)."""
    first = data_loader.get_co2_data()
    second = data_loader.get_co2_data()
    assert first is second, "Caching failed — new DataFrame loaded each time"


# ---------- 3. Test: Visualization Sanity ----------
def test_plotly_html_output_valid():
    """Check that generated Plotly chart renders valid HTML."""
    df = data_loader.co2_data[data_loader.co2_data["country"] == "Austria"].sort_values("year")
    fig = px.line(df, x="year", y="co2", title="CO₂ Austria")
    html = fig.to_html(full_html=False)
    soup = BeautifulSoup(html, "html.parser")
    assert soup.find("div") is not None, "Plotly HTML missing <div> container"


# ---------- 4. Test: World Map Data ----------
def test_country_filtering_and_year_bounds():
    """Ensure country filtering and year range are valid."""
    df = data_loader.co2_data
    germany = df[df["country"] == "Germany"]
    assert not germany.empty, "No data found for Germany"
    assert germany["country"].nunique() == 1, "Multiple countries found in filter"
    min_year, max_year = df["year"].min(), df["year"].max()
    assert 1700 <= min_year < max_year <= 2100, "Year range out of expected bounds"