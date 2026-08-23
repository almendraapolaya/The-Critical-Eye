# 👁️ The Critical Eye: Unmasking Misinformation with NLP & Analytics 📊

> **Can machine learning spot fake news faster than a human editor?**  
> *The Critical Eye* is an end-to-end data engineering and Machine Learning pipeline built to analyze over **116,000 news articles**, spot deceptive writing patterns, and deliver real-time visual insights to combat digital misinformation.

---

## 🎯 The Core Highlights ✨
* ⚡ **95.59% Classification Accuracy:** Powered by TF-IDF vectorization and machine learning models.
* 📊 **116K+ Articles Processed:** Blending multiple raw news datasets into a clean, normalized PostgreSQL pipeline.
* 💡 **Key Data Insight:** Fake news articles heavily cluster at significantly **shorter word counts** compared to authentic journalism.

---

## 🛠️ The Data Pipeline & Tech Stack

* **Data Engineering:** Python (`Pandas`, `NumPy`), `SQLAlchemy`, `PostgreSQL`
* **Natural Language Processing & ML:** `scikit-learn` (TF-IDF Vectorization, Logistic Regression)
* **Visual Intelligence:** Tableau Public Interactive Dashboard

---

## 📊 Interactive Dashboard

Check out the full interactive dashboard on **[Tableau Public](https://public.tableau.com/)** *(https://public.tableau.com/views/TheCriticalEye-ExecutiveAnalytics/The_Critical_Eye_Executive_Overview?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)*.

**Key Dashboard Features:**
1. **Dataset Class Balance:** Proves the baseline data split for unbiased training.
2. **Model Performance Matrix (Confusion Matrix):** Visualizes the 95.59% precision hits vs. false positives.
3. **Word Count Distribution:** Highlights length density patterns across authentic vs. deceptive media.

---

## 🚀 Quickstart Guide

To run this pipeline locally:

```bash
# 1. Clone the repository
git clone [https://github.com/almendraapolaya/The-Critical-Eye.git](https://github.com/almendraapolaya/The-Critical-Eye.git)
cd The-Critical-Eye

# 2. Set up your environment variables (.env)
# Create a .env file with your PostgreSQL connection string:
# DATABASE_URL=postgresql://user:password@localhost:5432/news_db

# 3. Ingest raw datasets into PostgreSQL
python src/db_import.py

# 4. Run exploratory analysis & model training
jupyter notebook notebooks/01_exploratory_analysis.ipynb