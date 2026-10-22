# AutoInsulin — Intelligent Insulin Management

> Turning physiological and treatment-related signals into early, evidence-based insights for personalized diabetes management.

---

## 👥 Team Techno Baaz

**Institution:** NMAM Institute of Technology

### Team Members

1. **Nireeksha Shetty**
2. **Snigdha S Shetty**
3. **Preethika**
4. **Rudresh**

---

# 🩺 About AutoInsulin

**AutoInsulin** is a research and innovation prototype that explores the use of wearable physiological signals and machine learning to support intelligent and personalized diabetes management.

The system analyzes physiological signals and classifies the user's autonomic state into three categories:

- **Sympathetic**
- **Relaxed**
- **Parasympathetic**

These physiological states can provide additional context about autonomic activity and stress-related physiological patterns.

The long-term vision of AutoInsulin is to combine physiological signals with glucose patterns, insulin-use information, refill history, treatment history, and patient-specific patterns to provide evidence-based decision support for diabetes care.

The system is designed to identify meaningful patterns rather than making assumptions about a patient's condition.

> **Important:** AutoInsulin is a research prototype. It does not automatically calculate, prescribe, or administer insulin doses and is not intended for clinical use.

---

# 🚨 Problem Statement

Diabetes management is a continuous process, but clinical assessment is often performed at specific intervals.

Between clinical visits, changes in physiological state, daily routines, stress, physical activity, and treatment patterns may occur without being captured in a structured way.

A single physiological change may not be significant.

However, multiple changes appearing across different physiological signals may provide useful information about an individual's current physiological condition.

The challenge is to process these signals and convert them into meaningful information that can support healthcare professionals and future intelligent diabetes-management systems.

### Problem We Address

> **How can wearable physiological signals be processed using machine learning to identify autonomic-state patterns and provide useful insights for personalized diabetes-management support?**

---

# 💡 Proposed Solution

AutoInsulin uses a machine-learning-based physiological analysis pipeline.

The system takes physiological time-series signals as input, processes them, extracts meaningful features, and uses a machine-learning model to classify the user's autonomic state.

### Overall Pipeline

```text
Wearable Physiological Signals
            ↓
      Signal Processing
            ↓
      30-Second Windowing
            ↓
      Feature Extraction
            ↓
      Machine Learning
            ↓
    Autonomic State Prediction
            ↓
    Prediction Probability
            ↓
       Dashboard Insight
