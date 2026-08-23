# 👁️ The Critical Eye: Unmasking Misinformation with NLP & Analytics 📊

> **Can machine learning spot fake news faster than a human editor?**  
> *The Critical Eye* is an end-to-end data engineering and Machine Learning pipeline built to analyze over **116,000 news articles**, spot deceptive writing patterns, and deliver real-time visual insights to combat digital misinformation.

<p center>
  <a href="https://public.tableau.com/views/TheCriticalEye-ExecutiveAnalytics/The_Critical_Eye_Executive_Overview?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link">
    <img src="https://img.shields.io/badge/View_Live_Dashboard-Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white" alt="Live Tableau Dashboard">
  </a>
</p>

---

## 🎯 The Core Highlights
* ⚡ **95.59% Classification Accuracy:** Powered by TF-IDF vectorization and machine learning models.
* 📊 **116K+ Articles Processed:** Blending multiple raw news datasets into a clean, normalized PostgreSQL pipeline.
* 💡 **Key Data Insight:** Fake news articles heavily cluster at significantly **shorter word counts** compared to authentic journalism.

---

## 🛠️ Data Pipeline & Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)

---

## 📊 Interactive Analytics Dashboard

Click the button above to explore the live interactive dashboard on Tableau Public.

**Key Visual Insights:**
1. **Dataset Class Balance:** Displays the balanced data split powering unbiased training.
2. **Model Performance Matrix:** Visualizes the 95.59% precision hits vs. false positives.
3. **Word Count Distribution:** Highlights length density patterns across authentic vs. deceptive media.

---

## 🚀 Quickstart Guide

To run this pipeline locally:

```bash
# 1. Clone the repository
git clone https://github.com/almendraapolaya/The-Critical-Eye.git

# 2. Set up environment variables (.env)
# DATABASE_URL=postgresql://user:password@localhost:5432/news_db

# 3. Ingest raw datasets into PostgreSQL
python src/db_import.py

# 4. Run exploratory analysis & model training
jupyter notebook notebooks/01_exploratory_analysis.ipynb