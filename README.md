# 💳 Dynamic Credit Risk Assessment AI

A professional, full-stack AI application for assessing loan credit risk using multilingual zero-shot classification (Khmer 🇰🇭 / English 🇺🇸).

Built with **Streamlit**, **Hugging Face Transformers**, and **Plotly**.

---

## 🚀 Features

*   **Multilingual Analysis**: Native support for Khmer and English input.
*   **Zero-Shot Classification**: Uses `joeddav/xlm-roberta-large-xnli` to classify risk without specific training data.
*   **Khmer Keyword Enhancement**: Automatically maps financial Khmer terms to English concepts to improve AI context understanding.
*   **Batch Processing**: Upload CSV files for bulk risk assessment with visualization.
*   **Real-time Risk Simulator**: Adjust loan parameters (amount, urgency) to see risk scoring logic.
*   **Feedback Loop**: SQLite database integration to log predictions and user feedback ("Agree"/"Disagree") for future model fine-tuning.
*   **Premium UI**: Glassmorphism design with responsiveness and dark mode.

## 🛠️ Tech Stack

*   **Frontend/Backend**: Streamlit (Python)
*   **AI Model**: XLM-RoBERTa (Zero-Shot Classification)
*   **Database**: SQLite (built-in logging)
*   **Visualization**: Plotly Express
*   **Text Processing**: Regex & Custom Mapping

## 📂 Project Structure

```
Credit-Risk-Assessment/
├── app.py                 # Main application entry point
├── requirements.txt       # Python dependencies
├── src/                   # Source code modules
│   ├── classifier.py      # AI Model logic & caching
│   ├── database.py        # SQLite database handling
│   ├── ui.py              # Custom CSS & UI components
│   └── utils.py           # Text processing & Khmer mapping
├── data/                  # Database storage (auto-generated)
└── README.md              # Documentation
```

## ⚡ Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/THYCHANTHA/Credit-Risk-Assessment.git
    cd Credit-Risk-Assessment
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application**:
    ```bash
    streamlit run app.py
    ```

## 🧪 Usage

1.  **Single Application**: Type a loan request in the text box (e.g., "I need money urgently for debt"). The AI will highlight keywords and estimate risk.
2.  **Batch Processing**: Go to the "Batch Processing" tab, upload a CSV, and select the text column to analyze multiple rows at once.
3.  **Global Logs**: View the history of all predictions and user feedback in the "Global Logs" tab.

## 📝 License

This project is open-source.
