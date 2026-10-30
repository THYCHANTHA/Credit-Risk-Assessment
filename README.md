# Credit Risk Assessment System

A Streamlit application that reads a short loan-application description written in **Khmer or English** and classifies the applicant as **low, medium or high risk** using a multilingual zero-shot language model. It was built as an educational demonstration of applying NLP in a banking setting.

## Introduction

Loan officers often work with free-text notes. This project explores whether a pretrained multilingual natural-language-inference model can turn such a note into a risk category without any labelled training data, and adds a small Khmer-aware step so that Khmer financial vocabulary is understood by the model.

## Problem statement

Classify the credit risk described in free text (Khmer, English or mixed) into low, medium or high, and let a human reviewer confirm or reject each result.

## Objectives

- Classify application narratives with a zero-shot model (no task-specific training data).
- Support Khmer input by mapping key Khmer financial terms to English context.
- Support one-off and batch (CSV) analysis, with charts.
- Record reviewer feedback in a local database.

## Main features

| Feature | Details |
|---|---|
| Single application | Enter text, get a classification and a confidence bar for each candidate label; Khmer keywords are highlighted |
| Batch processing | Upload a CSV, choose the text column, classify every row, view a pie and bar chart, download the results |
| Editable labels | Candidate labels default to `low risk, medium risk, high risk` and can be changed in the sidebar |
| Reviewer feedback | **Confirm** / **Reject** buttons store the input, predicted label, score and feedback in a local SQLite database |
| Logs tab | Table of stored feedback records and an agreement-rate metric |
| Risk simulator | Sidebar sliders (loan amount, overdue debts, urgency) that compute a simple score from a **fixed formula**; it is independent of the language model |

## Technologies

| Area | Tools |
|---|---|
| Interface | Streamlit |
| Model | Hugging Face Transformers, PyTorch; model `joeddav/xlm-roberta-large-xnli` (zero-shot classification) |
| Charts and data | Plotly, pandas |
| Storage | SQLite |
| Tokenizer dependency | SentencePiece |

## Architecture

```
app.py (Streamlit UI, three tabs)
  |- src/utils.py       Khmer detection and keyword mapping (9 financial terms -> English)
  |- src/classifier.py  loads the zero-shot pipeline (cached; GPU if available) and predicts
  |- src/database.py    SQLite logging in data/credit_risk.db
  `- src/ui.py          custom CSS styling
```

For Khmer input, each recognised term is kept and followed by its English meaning in brackets (for example `បំណុល (debt)`), and the enriched text is passed to the model.

## Folder structure

```
Credit-Risk-Assessment/
├── app.py            # Streamlit application
├── requirements.txt
├── src/
│   ├── classifier.py
│   ├── database.py
│   ├── ui.py
│   └── utils.py
└── data/             # created for the local SQLite database (git-ignored)
```

## Installation

```bash
git clone https://github.com/THYCHANTHA/Credit-Risk-Assessment.git
cd Credit-Risk-Assessment
pip install -r requirements.txt
```

The model is downloaded from Hugging Face on first run, which needs internet access and a large download.

## Usage

```bash
streamlit run app.py
```

For batch analysis, upload any CSV and pick the column that contains the application text.

## Existing results

**None.** The repository contains no labelled dataset, no evaluation and no accuracy figures, so no performance claim is made here.

## Limitations

- **Not validated.** The classification comes from a general-purpose zero-shot model and has not been evaluated against real loan outcomes. It should not be used for actual lending decisions.
- The Khmer keyword mapping covers only nine terms.
- The risk simulator uses an arbitrary hand-written formula, not a trained or validated model.
- Predictions are logged only when a reviewer clicks Confirm or Reject; batch results are not logged (that line is commented out in `app.py`).
- Logged text may contain sensitive applicant narratives; the local database file is git-ignored and should be protected.
- The page loads an icon and fonts from external URLs at runtime.
- No tests and no screenshots are included.

## References and acknowledgements

- Zero-shot classification with the [`joeddav/xlm-roberta-large-xnli`](https://huggingface.co/joeddav/xlm-roberta-large-xnli) model on Hugging Face.
- [Streamlit](https://streamlit.io), [Plotly](https://plotly.com/python/), [Transformers](https://github.com/huggingface/transformers).
