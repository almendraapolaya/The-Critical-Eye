# 👁️ The Critical Eye: Detecting Misinformation with NLP & Analytics 📊

> **Can a model learn to tell real political news from fake news, and how far can we trust its score?**
> *The Critical Eye* is an end-to-end data project: two public news datasets are loaded into PostgreSQL, cleaned, checked for data leakage and duplicates, converted to TF-IDF features, classified with Logistic Regression, and presented in a Tableau dashboard.

<p align="center">
  <a href="https://public.tableau.com/views/TheCriticalEye-ExecutiveAnalytics/TheCriticalEyeFakeNewsClassification?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link">
    <img src="https://img.shields.io/badge/View_Live_Dashboard-Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white" alt="Live Tableau Dashboard">
  </a>
</p>

---

## 🎯 Key Results

* **93.97% accuracy on a held-out test set** of 12,624 articles the model never saw during training. A model that always guessed "real" would score 55.1%.
* **63,119 unique articles** after combining two public datasets and removing about 53,000 exact duplicates.
* **Two sources of inflated accuracy found and fixed:** publisher tags (such as "WASHINGTON (Reuters) –") that gave away the label, and duplicate articles that could appear in both the training and the test set. An earlier version that still had both problems scored 95.59%, so the lower score here is the more honest one.
* **Length alone does not separate real from fake news:** average length is 587 words for real and 521 for fake articles, and the two distributions overlap heavily.

---

##  Presentation

[![Presentation Deck](https://img.shields.io/badge/Presentation-Gamma_Slides-blue?style=for-the-badge&logo=gamma)](https://gamma.app/docs/The-Critical-Eye-Unmasking-Misinformation-with-NLP-Visual-Analyti-47csh31oz6brrm5)

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)

---

## 🔄 How It Works

1. **Data:** two public datasets, ISOT (44,898 articles) and WELFake (72,134 articles; 71,537 after dropping rows with a missing title or text). Labels: 0 = real, 1 = fake.
2. **Storage:** `src/db_import.py` loads the raw CSV files into PostgreSQL with Pandas and SQLAlchemy, and the notebook queries them with SQL.
3. **Cleaning:** a regular expression removes the publisher tag at the start of real articles in both datasets (about 21,100 tagged articles in each, all labeled real). Title and body are combined into one text column.
4. **Duplicates:** 53,316 of the 116,435 combined articles were exact copies (the datasets overlap, and each has internal repeats). One copy of each was kept, leaving 63,119 articles: 34,790 real and 28,329 fake.
5. **Features:** TF-IDF with the 10,000 most informative words and English stop-words removed. The vectorizer is fitted on the training set only.
6. **Model:** Logistic Regression on a stratified 80/20 train/test split (50,495 training and 12,624 test articles).
7. **Evaluation:** accuracy, precision, recall and a confusion matrix, computed on the test set only.
8. **Dashboard:** the model's predictions are exported to a CSV (without the article text) and visualized in Tableau Public.

---

## 📈 Model Performance (held-out test set, 12,624 articles)

| | Precision | Recall | F1-score | Articles |
|---|---|---|---|---|
| Real (0) | 0.94 | 0.95 | 0.95 | 6,958 |
| Fake (1) | 0.94 | 0.93 | 0.93 | 5,666 |

**Confusion matrix**

| | Predicted real | Predicted fake |
|---|---|---|
| **Actual real** | 6,621 | 337 |
| **Actual fake** | 424 | 5,242 |

Overall accuracy: **93.97%**. Baseline (always predict the most common class): 55.1%.

---

## 📊 Interactive Dashboard

Explore the dashboard on Tableau Public using the button at the top of this page.

1. **Dataset Class Balance:** 34,790 real vs. 28,329 fake articles after removing duplicates.
2. **Model Performance:** the confusion matrix for the held-out test set only.
3. **Article Length:** real and fake articles have similar length distributions, so length is not a useful shortcut.

---

## ⚠️ Limitations

* **Domain bias:** both datasets are mainly political and world news. In a quick test, the model flagged enthusiastic wording in science and astronomy headlines as deceptive.
* **Style, not truth:** the model detects writing patterns, not facts. It may still be learning source-specific style, for example the neutral tone of wire-service reporting.
* **Labels come from the source of an article,** not from a fact-check of every claim.
* **Duplicates were removed by exact text match,** so near-duplicates (the same article with a different title) may remain.
* **Confidence is modest on new text:** a recent real news article was classified correctly, but with about 80% confidence.

## 🔭 Next Steps

* Train on one dataset and test on the other to measure how well the model generalizes.
* Inspect the words with the largest model weights to check for remaining shortcuts.
* Add other domains (sports, entertainment, science) to the training data.
* Try a contextual model such as BERT, and serve the model through a FastAPI endpoint in Docker.

---

## 🚀 Quickstart

The raw datasets are not stored in this repository. Download them from their original sources (both on Kaggle) and place the files in a `data/` folder:

* **ISOT Fake News Dataset:** `True.csv` and `Fake.csv` ([download page](https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets))
* **WELFake:** `WELFake_Dataset.csv` ([download page](https://www.kaggle.com/datasets/studymart/welfake-dataset-for-fake-news))

```bash
# 1. Clone the repository
git clone https://github.com/almendraapolaya/The-Critical-Eye.git
cd The-Critical-Eye

# 2. Create a PostgreSQL database called critical_eye_db, then create a .env file in the project root containing:
# DB_PASSWORD=your_postgres_password

# 3. Load the raw datasets into PostgreSQL
python src/db_import.py

# 4. Run the analysis and model training
jupyter notebook notebooks/01_exploratory_analysis.ipynb
```

The notebook expects PostgreSQL on `localhost:5432` with the user `postgres`.

## 📁 Repository Structure

```
The-Critical-Eye/
├── notebooks/01_exploratory_analysis.ipynb   # cleaning, duplicates, features, model, export
├── src/db_import.py                          # loads the raw CSV files into PostgreSQL
├── data/                                     # raw and exported CSVs (not tracked by git)
└── README.md
```