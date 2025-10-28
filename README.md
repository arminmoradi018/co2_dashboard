# 🌍 CO₂ Dashboard

An **interactive Shiny for Python dashboard** visualizing global CO₂ emissions across time and geography.  
This project provides dynamic map-based and time-series visualizations powered by **Plotly**, **Pandas**, and **Shiny for Python** — all designed for intuitive, data-driven exploration.

[![Tests](https://github.com/arminmoradi018/co2_dashboard/actions/workflows/ci.yml/badge.svg)](https://github.com/arminmoradi018/co2_dashboard/actions/workflows/ci.yml)

---

## 🚀 Features

- 🗺️ **Global CO₂ Emissions Map** — Visualize emissions by country and year
- 📈 **Country Time-Series Trends** — Interactive plots of emissions over time
- ⚙️ **Adjustable Rolling Average** — Smooth noisy time-series data easily
- ⚡ **Automatic Data Loading & Caching** — Fast and efficient app startup
- 🧪 **Fully Tested** — Comprehensive test suite with **Pytest**
- 🤖 **Continuous Integration (CI)** — Automated testing via **GitHub Actions**
- 🧼 **HTML Validation** — Ensures robust UI using BeautifulSoup-based tests

---

## 🧠 Tech Stack

| Category        | Tools                                          |
| --------------- | ---------------------------------------------- |
| Framework       | [Shiny for Python](https://shiny.posit.co/py/) |
| Data Processing | Pandas                                         |
| Visualization   | Plotly                                         |
| Testing         | Pytest, BeautifulSoup                          |
| CI/CD           | GitHub Actions                                 |

---

## 🌐 Data Source

All data is sourced from [Our World in Data – CO₂ dataset](https://ourworldindata.org/co2-and-greenhouse-gas-emissions).  
The app automatically loads the latest version from:
[co2-data](https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv)

---
```bash
## 🧩 Project Structure

co2_dashboard/
│
├── src/
│ ├── **init**.py
│ ├── app.py
│ ├── data_loader.py
│ ├── server.py
│ └── ui.py
├── test/
│ ├── **init**.py
│ └── test_app.py
├── .github/workflows/ci.yml
├── .gitignore
├── LICENSE
├── pytest.ini
├── requirements.txt
└── README.md
```
---

## 🧪 Run Locally

```bash
# 1️⃣ Clone the repository
git clone https://github.com/arminmoradi018/co2_dashboard.git
cd co2_dashboard

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the Shiny app
shiny run --reload --launch-browser src/app.py

```

---

## 🧪 Testing

This project includes a **Pytest-based test suite** verifying key functionality:

1. **Data Loading** – Ensures the CO₂ dataset loads correctly and includes essential columns.
2. **Data Caching** – Confirms `get_co2_data()` returns cached results for efficiency.
3. **Visualization Validation** – Checks that Plotly-generated charts produce valid HTML (via BeautifulSoup).
4. **World Map Data Integrity** – Validates country filtering and logical year ranges (1700–2100).

All tests currently **pass successfully** both locally and in CI.

### 🧰 Running Tests Locally

To run all tests locally, simply execute:

```bash
pytest -v

```

---

## 🤖 Continuous Integration (CI)

This project uses **GitHub Actions** for continuous integration.  
Every time you **push** a commit or open a **pull request**, all automated tests are executed in a clean environment to ensure code quality and stability.

---

### 🧱 Workflow Configuration

The CI workflow is defined in the following file:
.github/workflows/ci.yml

It performs the following steps:

1. **Checkout the repository** – downloads the latest version of the code.
2. **Set up Python** – installs Python 3.11.
3. **Install dependencies** – installs required packages from `requirements.txt`.
4. **Run tests** – executes all Pytest tests located in the `test/` directory.

---

### 🧩 Example Workflow File

```yaml
name: Tests

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest

      - name: Run tests
        run: pytest
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

---

## 👤 Author

**Armin Moradi**
🎓 AI student (3rd semester) at JKU Linz
📘 This project was developed as an assignment of one of my second-semester courses in Artificial Intelligence.
📫 Arminmoradi018@gmail.com
