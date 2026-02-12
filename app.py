import streamlit as st
import pandas as pd
import json
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("CSCI316 – DLD Transactions Dashboard")

BASE_PATH = Path("data/outputs")

# Sidebar: Run Metadata
st.sidebar.header("Run Information")

metadata_path = BASE_PATH / "metadata" / "run_info.json"

if metadata_path.exists():
    with open(metadata_path) as f:
        run_info = json.load(f)

    for k, v in run_info.items():
        st.sidebar.write(f"**{k}**: {v}")
else:
    st.sidebar.warning("No run metadata found.")

# Tabs Layout

tab1, tab2, tab3, tab4 = st.tabs(
    ["Metrics", "Predictions", "Figures", "Notebooks"]
)

# Metrics Tab

with tab1:

    st.header("Model Metrics")

    metrics_path = BASE_PATH / "metrics"

    if metrics_path.exists():
        metric_files = list(metrics_path.glob("*.csv"))

        if metric_files:
            selected_metric = st.selectbox(
                "Select Metrics File",
                metric_files
            )

            df_metrics = pd.read_csv(selected_metric)
            st.dataframe(df_metrics)

        else:
            st.warning("No metric files found.")
    else:
        st.warning("Metrics folder missing.")

    cv_path = metrics_path / "cv_results.csv"
    if cv_path.exists():
        st.subheader("Cross Validation Results")
        df_cv = pd.read_csv(cv_path)
        st.dataframe(df_cv)


# Predictions Tab

with tab2:

    st.header("Test Predictions")

    pred_path = BASE_PATH / "predictions" / "test_predictions.csv"

    if pred_path.exists():
        df_pred = pd.read_csv(pred_path)
        st.dataframe(df_pred.head(100))
    else:
        st.warning("No predictions file found.")


# Figures Tab

with tab3:

    st.header("Visualizations")

    figures_path = BASE_PATH / "figures"

    if figures_path.exists():
        figure_files = list(figures_path.glob("*"))

        for fig in figure_files:
            st.subheader(fig.stem.replace("_", " ").title())
            st.image(str(fig), use_column_width=True)
    else:
        st.warning("No figures found.")


# Notebooks Tab (HTML Version)

# Notebooks Tab (Pure Python .ipynb Renderer)
with tab4:

    st.header("Notebooks")

    notebooks_path = Path("notebooks")
    notebook_files = sorted(notebooks_path.glob("*.ipynb"))

    if notebook_files:
        selected_nb = st.selectbox(
            "Select Notebook",
            notebook_files,
            format_func=lambda x: x.name
        )

        with open(selected_nb, "r", encoding="utf-8") as f:
            notebook = json.load(f)

        for cell in notebook.get("cells", []):

            if cell["cell_type"] == "markdown":
                st.markdown("".join(cell.get("source", [])))

            elif cell["cell_type"] == "code":
                st.code("".join(cell.get("source", [])), language="python")

                # Render simple text outputs if they exist
                for output in cell.get("outputs", []):
                    if "text" in output:
                        st.text("".join(output["text"]))
                    elif "data" in output and "text/plain" in output["data"]:
                        st.text("".join(output["data"]["text/plain"]))

            st.divider()

    else:
        st.warning("No .ipynb files found.")

