# Student Performance AI System (Personalized Learning Data Analytics Platform)

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analytics-150458.svg)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Pipelines-F7931E.svg)](https://scikit-learn.org/)

An end-to-end educational analytics platform designed to ingest learner interaction metrics, predict future academic outcomes, perform risk stratification, and generate personalized intervention strategies.

---

## 📌 System Architecture & Pipeline Workflow

```text
  ┌────────────────────────┐       ┌───────────────────────┐       ┌───────────────────────┐
  │ Interaction Dataset    │ ───►  │ Modular Feature Engine│ ───►  │ Predictive & Risk     │
  │ (CSV/User Inputs)      │       │ (Pre-processing)      │       │ Modeling (Scikit-Learn)│
  └────────────────────────┘       └───────────────────────┘       └───────────────────────┘
                                                                               │
  ┌────────────────────────┐       ┌───────────────────────┐                   │
  │ Streamlit Analytics UI │ ◄───  │ Personalized Dynamic  │ ◄─────────────────┘
  │ Dashboard              │       │ Study Plan Engine     │     (Advisory Insights)
  └────────────────────────┘       └───────────────────────┘
