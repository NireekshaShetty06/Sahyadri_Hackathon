# AI-Assisted Glycemic Risk Screening Using Wearable Physiological Signals

**Hackathon Project — Problem Statement PS 3.1**

An AI-assisted screening research prototype that explores how wearable physiological signals can support preliminary glycemic-risk assessment and help identify individuals who may require further clinical evaluation.

## 👥 Team Members

- Snigdha S Shetty
- Preethika
- Nireeksha Shetty
- Sinchana M Bhat

## 📌 Project Overview

Early identification of individuals who may have abnormal blood glucose levels is important for timely assessment and appropriate healthcare intervention. However, wearable devices that collect physiological signals do not directly measure blood glucose levels.

Our project builds on physiological signal processing and machine learning to investigate how multiple wearable signals, combined with appropriate clinical reference data, could support preliminary glycemic-risk screening.

The system is designed with a focus on explainability, data quality, responsible AI, and a simple interface for presenting results.

**Important:** This project is intended for research and screening support. It does not replace laboratory glucose testing, professional medical judgment, or clinical diagnosis.

## 🎯 Problem Statement

**PS 3.1 — AI-Assisted Screening Tool for a Single Common Condition at PHC Level**

Primary healthcare centres need accessible tools that can help identify individuals who may require further assessment. Our proposed solution explores the potential use of wearable physiological signals and machine learning to support this process for glucose-related abnormalities.

The central research question is:

*Can wearable physiological signals provide useful additional information for glycemic-risk screening when evaluated against appropriate clinical reference measurements?*

## 💡 Proposed Solution

The project follows a modular approach consisting of the following components.

### 1. Physiological Data Processing

The system works with wearable physiological signals, where available:

- Electrodermal activity (EDA)
- Heart rate and heart-rate variability (HR/HRV)
- Blood-volume pulse (BVP)
- Skin temperature
- Physical activity and movement

These signals can be processed to assess data quality and extract useful numerical features.

### 2. Signal Preprocessing and Feature Extraction

The processing pipeline can include:

- Data-quality checks and missing-value handling
- Noise filtering and preprocessing
- Signal segmentation into analysis windows
- Statistical and time-domain feature extraction
- Frequency-domain analysis, including FFT-based features where appropriate
- Alignment of physiological measurements with relevant reference data

The exact processing methods depend on the available dataset and sampling characteristics.

### 3. Existing Physiological-State Classification

The existing research foundation uses machine learning to classify physiological states into:

- Sympathetic
- Relaxed
- Parasympathetic

The project documentation reports an AUC of 0.94 for this existing classification task under Leave-One-Subject-Out validation.

This reported result applies to physiological-state classification only. It must not be interpreted as evidence of glucose prediction or diabetes detection.

### 4. Proposed Glycemic-Risk Screening

A separate glycemic-risk model is proposed to investigate whether physiological features can support the identification of individuals who may need further glucose assessment.

Developing and validating this model requires:

- A clearly defined screening target
- An appropriate dataset containing clinical glucose reference measurements
- Correct alignment of physiological signals with clinical labels
- Subject-independent model evaluation
- Clinically relevant performance metrics
- Appropriate review of limitations and uncertainty

Glycemic-risk screening performance should only be reported after the separate model has been trained and evaluated using suitable data.

### 5. Screening Dashboard

The proposed dashboard is intended to present information in a clear and understandable format for primary healthcare personnel.

Potential dashboard components include:

- Patient or session identification using a pseudonymous identifier
- Signal-quality status
- Physiological-state classification output
- Relevant supporting features and measurements
- Glycemic-screening status, when a validated model is available
- Data-quality warnings and model limitations
- Guidance to follow approved clinical assessment procedures

The interface should display an inconclusive or unavailable status when the data are insufficient or a validated prediction is not available.

## 🏗️ System Architecture

The proposed system follows a modular architecture:

1. **Data input:** Receive authorised wearable recordings and relevant reference data.
2. **Data-quality assessment:** Check missing samples, invalid values, sensor errors, and timestamps.
3. **Signal preprocessing:** Prepare usable physiological signals for analysis.
4. **Feature extraction:** Calculate appropriate statistical and frequency-domain features.
5. **Physiological-state classifier:** Generate the existing physiological-state classification.
6. **Glycemic-risk model:** A separate proposed component requiring appropriate clinical labels and independent validation.
7. **Dashboard:** Present available results, supporting information, limitations, and appropriate next steps.

## 🛠️ Suggested Technology Stack

The following technologies are suitable for the proposed architecture. The exact stack should reflect the tools actually implemented in the repository.

| Component | Technology |
|---|---|
| Programming language | Python |
| Data analysis | NumPy, pandas |
| Signal processing | SciPy |
| Machine learning | scikit-learn |
| Visualisation | Matplotlib or Plotly |
| Backend API | Flask or FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Data storage | SQLite for a local prototype |
| Version control | Git and GitHub |

## 📂 Project Structure

The following is an illustrative structure for organising the project. Actual filenames and directories may differ in the current repository.

```text
Auto-Insulin/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── preprocessing.py
│   ├── feature_extraction.py
│   ├── state_classifier.py
│   ├── glycemic_screening.py
│   └── inference.py
├── app/
│   ├── main.py
│   ├── templates/
│   └── static/
├── models/
├── tests/
├── docs/
├── requirements.txt
└── README.md
```

## 🧪 Model Evaluation and Validation

Reliable evaluation is essential for a healthcare-related machine-learning system.

The proposed evaluation process includes:

- Separating training, validation, and test subjects where appropriate
- Preventing data leakage between training and testing
- Evaluating the model on held-out subjects
- Measuring sensitivity, specificity, precision, and predictive values
- Reviewing ROC-AUC and PR-AUC when appropriate
- Examining calibration and confusion matrices
- Documenting dataset limitations and uncertainty

Evaluation metrics must be calculated from actual experiments and reported with their corresponding target, dataset, and validation method.

The existing physiological-state classification result and any future glycemic-risk screening results must be reported separately.

## 🔒 Privacy, Safety, and Responsible AI

Because the project concerns health-related information, responsible handling of data is essential.

- Use authorised datasets and recordings.
- Avoid committing identifiable patient data, credentials, or private keys to GitHub.
- Use pseudonymous identifiers wherever possible.
- Document data sources, licensing, and permitted use.
- Provide an inconclusive output when the input data are insufficient.
- Explain the limitations of the model to users.
- Do not present unvalidated outputs as established clinical predictions.
- Do not recommend or automatically adjust insulin doses.
- Require appropriate clinical evaluation before any real-world healthcare use.

## 🌍 Expected Impact

The project aims to investigate whether wearable physiological information can complement established screening workflows.

Potential benefits include:

- Supporting structured preliminary screening research
- Making physiological measurements easier to review
- Helping identify situations where further clinical assessment may be appropriate
- Providing a foundation for future research into multimodal physiological analysis
- Exploring accessible decision-support interfaces for primary healthcare settings

These are intended benefits, not demonstrated clinical outcomes. Actual effectiveness must be established through appropriate validation.

## 🚧 Current Limitations and Future Scope

### Limitations

- Wearable physiological signals do not directly establish blood glucose levels.
- Physiological-state classification is not equivalent to glycemic-risk screening.
- A suitable clinical reference dataset is required to train and evaluate a separate glucose-related screening model.
- Performance may vary across participants, devices, populations, and recording conditions.
- The project must not be treated as a clinically validated diagnostic system without appropriate evidence.

### Future Scope

- Obtain and evaluate suitable clinically labelled datasets.
- Develop a separate glycemic-risk screening model.
- Perform subject-independent evaluation and calibration.
- Investigate robustness across devices and participant groups.
- Improve dashboard explainability and data-quality reporting.
- Evaluate the workflow under appropriate clinical and ethical oversight.
- Explore insulin-requirement prediction only as a separate research direction if suitable treatment-related data and rigorous validation become available.

## ▶️ Installation and Execution

The exact commands depend on the dependencies and entry point implemented in the repository.

For a Python-based project, a typical setup is:

1. Clone the repository.

   ```bash
   git clone https://github.com/Preeleo/Auto-Insulin.git
   cd Auto-Insulin
   ```

2. Create a virtual environment.

   ```bash
   python -m venv .venv
   ```

3. Activate the environment.

   **Windows PowerShell:**

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   **Linux/macOS:**

   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies, if `requirements.txt` is present.

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application using the actual entry point documented in the repository.

   For example, if the project uses Flask and its entry point is `app.py`:

   ```bash
   python app.py
   ```

   Replace this command with the correct command for the implemented application.

## 🏁 Hackathon Deliverables

The intended deliverables are:

- A working demonstration of the existing physiological-signal processing pipeline
- An existing physiological-state classification workflow
- Documentation of the screening target and dataset requirements
- A clear architecture for the proposed glycemic-risk model
- A dashboard that distinguishes available results from unavailable capabilities
- Relevant testing, evaluation, and limitations documentation

Only components that have actually been implemented and verified should be described as completed deliverables.

## 📚 Conclusion

Auto-Insulin explores the potential of wearable physiological signals and machine learning to support research into preliminary glycemic-risk screening.

The project builds on physiological-state classification and proposes a separate screening model that would require suitable clinical reference data, independent validation, and appropriate clinical oversight.

Our objective is to develop a transparent and responsible prototype that demonstrates the potential of AI-assisted screening while clearly communicating its current capabilities and limitations.

---

**Team:** Snigdha S Shetty, Preethika, Nireeksha Shetty, and Sinchana M Bhat

**Repository:** https://github.com/Preeleo/Auto-Insulin
