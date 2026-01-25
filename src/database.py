import sqlite3
import pandas as pd
from datetime import datetime
import os

DB_PATH = "data/credit_risk.db"

def init_db():
    """Initializes the SQLite database if it doesn't exist."""
    if not os.path.exists("data"):
        os.makedirs("data")
        
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Create logs table
    c.execute('''
        CREATE TABLE IF NOT EXISTS risk_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_text TEXT,
            predicted_label TEXT,
            confidence_score REAL,
            user_feedback TEXT,
            timestamp DATETIME
        )
    ''')
    conn.commit()
    conn.close()

def log_prediction(text: str, label: str, score: float, feedback: str = None):
    """Logs a prediction and optional feedback to the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO risk_logs (input_text, predicted_label, confidence_score, user_feedback, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (text, label, score, feedback, datetime.now()))
    conn.commit()
    conn.close()

def get_logs_as_dataframe():
    """Retrieves all logs as a pandas DataFrame."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM risk_logs ORDER BY timestamp DESC", conn)
    conn.close()
    return df
