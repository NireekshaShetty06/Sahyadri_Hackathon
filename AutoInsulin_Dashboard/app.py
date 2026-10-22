import warnings
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sklearn
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AutoInsulin Dashboard",
    page_icon="🧠",
    layout="wide"
)


# ============================================================
# FILE PATHS
# ============================================================

BASE_DIR = Path(__file__).parent

MODEL_PATH = BASE_DIR / "autinsulin_random_forest.pkl"
DATA_PATH = BASE_DIR / "feature_matrix.csv"


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    # Suppress sklearn version mismatch warning during unpickling
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            category=sklearn.exceptions.InconsistentVersionWarning
        )
        loaded_model = joblib.load(MODEL_PATH)

    # Re-serialize the model with the current sklearn version.
    # This permanently fixes the version mismatch warning on future loads.
    joblib.dump(loaded_model, MODEL_PATH)

    return loaded_model


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


# ============================================================
# LOAD MODEL AND DATA
# ============================================================

try:
    model = load_model()
    feature_matrix = load_data()

except Exception as e:
    st.error("Could not load the model or feature dataset.")
    st.error(str(e))
    st.stop()


# ============================================================
# IDENTIFY FEATURES
# ============================================================

# These columns are information about the sample,
# not ML input features.
metadata_columns = [
    "subject",
    "autonomic_state",
    "window_idx"
]

feature_columns = [
    col for col in feature_matrix.columns
    if col not in metadata_columns
]


# ============================================================
# CHECK MODEL FEATURE COUNT
# ============================================================

expected_features = getattr(
    model,
    "n_features_in_",
    len(feature_columns)
)

if len(feature_columns) != expected_features:

    st.error(
        f"""
        Feature mismatch detected.

        Dataset features: {len(feature_columns)}

        Model expects: {expected_features}

        Please make sure the correct feature_matrix.csv
        and Random Forest model are being used.
        """
    )

    st.stop()


# ============================================================
# PAGE HEADER
# ============================================================

st.title("🧠 AutoInsulin")

st.subheader("AI-Driven Physiological Stress Analysis")

st.write(
    """
    **AutoInsulin** analyzes physiological signals such as
    EDA, RR interval and temperature to identify autonomic
    physiological states.
    """
)


# ============================================================
# TOP INFORMATION CARDS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Model",
        value="Random Forest"
    )

with col2:
    st.metric(
        label="Input Features",
        value=len(feature_columns)
    )

with col3:
    st.metric(
        label="Demo Samples",
        value=len(feature_matrix)
    )


st.divider()


# ============================================================
# SAMPLE ANALYSIS
# ============================================================

st.header("🔬 Physiological Sample Analysis")

st.write(
    """
    Select a sample from the feature dataset and run the
    trained Random Forest model.
    """
)


# ============================================================
# SAMPLE SELECTION
# ============================================================

sample_number = st.selectbox(
    "Select Demo Sample",
    options=list(range(1, len(feature_matrix) + 1)),
    index=0
)

# Convert selected number into dataframe index
selected_index = sample_number - 1

selected_sample = feature_matrix.iloc[selected_index]


# ============================================================
# SAMPLE INFORMATION
# ============================================================

st.subheader("Sample Information")

info_col1, info_col2 = st.columns(2)

with info_col1:
    st.write(
        f"**Subject:** {selected_sample['subject']}"
    )

with info_col2:
    st.write(
        f"**Recorded State:** {selected_sample['autonomic_state']}"
    )


# ============================================================
# PREPARE INPUT FEATURES
# ============================================================

X_selected = selected_sample[feature_columns].to_frame().T

# Make sure all feature values are numeric
X_selected = X_selected.apply(pd.to_numeric, errors="coerce")

# Check for missing values
if X_selected.isnull().values.any():

    st.error(
        "The selected sample contains missing feature values."
    )

    st.stop()


# ============================================================
# SHOW FEATURES
# ============================================================

with st.expander(
    f"View {len(feature_columns)} Physiological Features"
):

    feature_display = pd.DataFrame({
        "Feature": feature_columns,
        "Value": X_selected.iloc[0].values
    })

    st.dataframe(
        feature_display,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# RUN RANDOM FOREST PREDICTION
# ============================================================

try:

    # -----------------------------
    # Prediction
    # -----------------------------

    # Use .values to pass a plain NumPy array, avoiding the
    # "fitted without feature names" warning when the model
    # was originally trained on unnamed arrays.
    prediction = model.predict(X_selected.values)[0]

    # -----------------------------
    # Prediction probabilities
    # -----------------------------

    probabilities = model.predict_proba(X_selected.values)[0]

    classes = model.classes_

except Exception as e:

    st.error("Prediction could not be completed.")
    st.error(str(e))
    st.stop()


# ============================================================
# AI PREDICTION
# ============================================================

st.divider()

st.header("🤖 AI Prediction")


# ============================================================
# DISPLAY MAIN PREDICTION
# ============================================================

prediction_display = str(prediction).upper()

if prediction == "sympathetic":

    st.error(
        f"Predicted Autonomic State: {prediction_display}"
    )

elif prediction == "parasympathetic":

    st.success(
        f"Predicted Autonomic State: {prediction_display}"
    )

elif prediction == "relaxed":

    st.info(
        f"Predicted Autonomic State: {prediction_display}"
    )

else:

    st.write(
        f"### Predicted Autonomic State: {prediction_display}"
    )


# ============================================================
# PROBABILITY TABLE
# ============================================================

st.subheader("Prediction Probability")

probability_data = pd.DataFrame({
    "State": classes,
    "Probability": probabilities
})

probability_data["Probability"] = (
    probability_data["Probability"] * 100
).round(2)

probability_data["Probability"] = (
    probability_data["Probability"].astype(str) + "%"
)

st.table(probability_data)


# ============================================================
# STATE EXPLANATION
# ============================================================

st.subheader("Physiological Interpretation")


if prediction == "sympathetic":

    st.write(
        """
        The model identifies a **Sympathetic** autonomic state,
        which represents a physiological state associated with
        increased stress/arousal patterns.
        """
    )

elif prediction == "parasympathetic":

    st.write(
        """
        The model identifies a **Parasympathetic** autonomic
        state, representing a physiological state associated
        with relaxation/recovery patterns.
        """
    )

elif prediction == "relaxed":

    st.write(
        """
        The model identifies a **Relaxed** autonomic state,
        indicating a lower-stress physiological pattern in
        the selected sample.
        """
    )


# ============================================================
# DEMO INFORMATION
# ============================================================

st.divider()

st.subheader("📊 Demo Information")

demo_col1, demo_col2, demo_col3 = st.columns(3)

with demo_col1:
    st.metric(
        "Selected Sample",
        sample_number
    )

with demo_col2:
    st.metric(
        "Recorded State",
        str(selected_sample["autonomic_state"]).upper()
    )

with demo_col3:
    st.metric(
        "AI Prediction",
        prediction_display
    )


# ============================================================
# DISCLAIMER
# ============================================================

st.divider()

st.caption(
    """
    Prototype / Decision-Support Demonstration

    This system demonstrates AI-based physiological state
    classification. It is not a medical diagnosis and does
    not automatically calculate or administer insulin doses.
    Clinical validation would be required before real-world
    medical use.
    """
)

st.caption(
    "AutoInsulin | Ideas for India 2026 | Sustainable & Resilient India"
)