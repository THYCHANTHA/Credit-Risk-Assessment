# Credit Risk Assessment System

This is a project I developed to help financial institutions assess loan risks using AI. It is a full-stack web application built with Streamlit and uses Deep Learning to analyze text.

## What this project does

This system allows loan officers to enter a description of a loan application (in **Khmer** or **English**) and automatically determines if the applicant is **Low Risk**, **Medium Risk**, or **High Risk**.

It uses a Zero-Shot Classification model (`xlm-roberta-large-xnli`) which works great for multiple languages.

## Main Features

*   **Works with Khmer & English**: I implemented a special function to detect Khmer text and map keywords (like "bamonul" -> "debt") so the AI understands the context better.
*   **AI Analysis**: It predicts the risk level without needing a huge training dataset.
*   **Batch Processing**: You can upload a CSV file containing diverse customer data, and the system will analyze all of them at once.
*   **Visualizations**: It shows the results in clear charts and progress bars.
*   **Risk Simulator**: I added a slider tool to simulate how different factors (like loan amount or urgency) affect the risk score.
*   **Database Logging**: All predictions and user feedback (Agree/Disagree) are saved to a local SQLite database so we can improve the model later.

## How I built it

I used the following technologies:
*   **Python**: The core language.
*   **Streamlit**: To build the user interface.
*   **Hugging Face**: For the pre-trained AI model.
*   **Plotly**: To create the interactive charts.
*   **SQLite**: For data storage.

## How to run the project

1.  **Clone this repository**:
    ```bash
    git clone https://github.com/THYCHANTHA/Credit-Risk-Assessment.git
    cd Credit-Risk-Assessment
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app**:
    ```bash
    streamlit run app.py
    ```

## File Structure

*   `app.py`: The main file to start the application.
*   `src/`: Contains the logic for the Classifier, Database, and UI styles.
*   `requirements.txt`: List of libraries needed.

---
This project was built for educational and practical purposes to demonstrate how AI can be applied in the Banking sector.
