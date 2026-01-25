import streamlit as st
import pandas as pd
import plotly.express as px
import time

# Custom Modules
from src import ui, utils, classifier, database

# --- Page Config ---
st.set_page_config(
    page_title="Credit Risk AI Analysis",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Initialization ---
ui.apply_custom_styles()
database.init_db()

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2666/2666505.png", width=60)
    st.markdown("### Configuration")
    
    st.markdown("#### 📂 Data Import")
    uploaded_file = st.file_uploader("Upload Batch CSV", type=["csv"])
    
    st.markdown("#### 🏷️ Candidate Labels")
    default_labels = "low risk, medium risk, high risk"
    labels_input = st.text_area("Edit Labels (comma separated)", default_labels, height=100)
    candidate_labels = [label.strip() for label in labels_input.split(',')]
    
    st.markdown("---")
    st.markdown("#### 🎚️ Risk Simulator")
    sim_loan_amount = st.slider("Loan Amount ($)", 500, 50000, 5000)
    sim_debts = st.slider("Overdue Debts", 0, 10, 0)
    sim_urgency = st.slider("Urgency Level", 1, 10, 5)
    
    # Calculate simulated risk (Euclidean heuristic)
    sim_risk_score = (sim_debts * 10 + sim_urgency * 5 + (sim_loan_amount/2000)) / 100
    sim_risk_score = min(sim_risk_score, 1.0)
    
    st.markdown(f"**Simulated Score:** `{sim_risk_score:.2f}`")
    st.progress(sim_risk_score)
    
    st.info("Adjust sliders to see how traditional metrics impact risk factors.")

# --- Main Content ---
ui.render_header()

# Load Model
with st.spinner("Initializing AI Core..."):
    model = classifier.load_zero_shot_model()

if not model:
    st.error("System Error: AI Model could not be loaded. Please check server logs.")
    st.stop()

# Tabs
tab1, tab2, tab3 = st.tabs(["📝 Single Application", "📊 Batch Processing", "📜 Global Logs"])

# === TAB 1: Single Application ===
with tab1:
    col_input, col_output = st.columns([1, 1.2], gap="large")
    
    with col_input:
        st.markdown('<div class="glass-container">', unsafe_allow_html=True)
        st.subheader("Application Details")
        st.markdown("Enter the loan application text below. The system supports mixed **Khmer** and **English** input.")
        user_input = st.text_area("Narrative Input", height=200, placeholder="Example: ខ្ញុំត្រូវការកម្ចីបន្ទាន់ដើម្បីបង់បំណុល... (I need a loan urgently to pay debt)")
        
        if st.button("Analyze Risk Profile", use_container_width=True):
            if not user_input:
                st.warning("Please enter some text to analyze.")
            else:
                with st.spinner("Processing semantics..."):
                    # 1. Enhance
                    enhanced_text, highlighted_html, is_khmer = utils.map_keywords_khmer(user_input)
                    # 2. Predict
                    result = classifier.predict_risk(enhanced_text, candidate_labels, model)
                    
                    # Store in session state for result persistence across reruns (if needed for feedback)
                    st.session_state['last_result'] = result
                    st.session_state['last_input'] = user_input
                    st.session_state['is_khmer'] = is_khmer
                    st.session_state['highlighted_html'] = highlighted_html

    with col_output:
        if 'last_result' in st.session_state:
            result = st.session_state['last_result']
            is_khmer = st.session_state['is_khmer']
            highlighted_html = st.session_state['highlighted_html']
            
            st.markdown('<div class="glass-container">', unsafe_allow_html=True)
            st.subheader("Risk Analysis Report")
            
            # Highlighted Text Display
            st.markdown("**Semantic Extraction:**")
            st.markdown(f"<div style='background:rgba(255,255,255,0.05); padding:15px; border-radius:10px; margin-bottom:15px; line-height:1.6;'>{highlighted_html}</div>", unsafe_allow_html=True)
            if is_khmer:
                st.caption("ℹ️ Khmer tokens mapped to English financial concepts for enhanced precision.")
            
            st.divider()
            
            # Risk Breakdown
            top_label = result['labels'][0]
            top_score = result['scores'][0]
            
            # Dynamic Color for top result
            color = "green"
            if "high" in top_label.lower(): color = "red"
            elif "medium" in top_label.lower(): color = "orange"
            
            st.markdown(f"### Classification: <span style='color:{color}'>{top_label.upper()}</span>", unsafe_allow_html=True)
            
            # Progress Bars
            for lbl, score in zip(result['labels'], result['scores']):
                st.write(f"**{lbl.title()}** ({score*100:.1f}%)")
                st.progress(score)
            
            st.divider()
            
            # Feedback
            st.markdown("**Validation:**")
            fb_c1, fb_c2 = st.columns(2)
            if fb_c1.button("✅ Confirm"):
                database.log_prediction(st.session_state['last_input'], top_label, top_score, "agree")
                st.toast("Feedback recorded successfully!", icon="💾")
            if fb_c2.button("❌ Reject"):
                database.log_prediction(st.session_state['last_input'], top_label, top_score, "disagree")
                st.toast("Feedback recorded logged for review.", icon="⚠️")
                
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            # Placeholder
            st.info("👈 Enter application details to generate a report.")

# === TAB 2: Batch Processing ===
with tab2:
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    st.subheader("Bulk Analysis")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head(), use_container_width=True)
        
        txt_column = st.selectbox("Select Text Column for Analysis", df.columns)
        
        if st.button("Start Batch Processing"):
            results = []
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            total = len(df)
            for i, text in enumerate(df[txt_column]):
                text_str = str(text)
                # Enhance & Predict
                e_text, _, _ = utils.map_keywords_khmer(text_str)
                res = classifier.predict_risk(e_text, candidate_labels, model)
                
                top_res = res['labels'][0]
                top_score = res['scores'][0]
                
                results.append({
                    'Original Text': text_str,
                    'Predicted Risk': top_res,
                    'Confidence': top_score
                })
                
                # Update progress
                progress = (i + 1) / total
                progress_bar.progress(progress)
                status_text.text(f"Processing row {i+1}/{total}...")
                
                # Log to DB automatically for batch? Optional, maybe skip to save space.
                # database.log_prediction(text_str, top_res, top_score, "batch")
            
            res_df = pd.DataFrame(results)
            st.success("Batch processing complete!")
            
            # Analytics
            c1, c2 = st.columns(2)
            with c1:
                fig_pie = px.pie(res_df, names='Predicted Risk', title='Risk Distribution', hole=0.4)
                fig_pie.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
                st.plotly_chart(fig_pie, use_container_width=True)
            with c2:
                fig_bar = px.histogram(res_df, x='Predicted Risk', y='Confidence', histfunc='avg', title='Avg Confidence by Category')
                fig_bar.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")
                st.plotly_chart(fig_bar, use_container_width=True)
            
            st.dataframe(res_df, use_container_width=True)
            
            csv = res_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Download Report",
                csv,
                "risk_assessment_batch_results.csv",
                "text/csv",
                key='download-csv'
            )
            
    else:
        st.info("Upload a CSV file containing loan applications to proceed.")
        
    st.markdown('</div>', unsafe_allow_html=True)

# === TAB 3: Global Logs ===
with tab3:
    st.markdown("### 📜 System Logs & Feedback History")
    
    if st.button("Refresh Logs"):
        # Just reruns the script to fetch new data
        pass
        
    log_df = database.get_logs_as_dataframe()
    
    if not log_df.empty:
        # Metrics
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Predictions", len(log_df))
        agreement_rate = len(log_df[log_df['user_feedback'] == 'agree']) / len(log_df) * 100 if len(log_df) > 0 else 0
        m2.metric("Agreement Rate", f"{agreement_rate:.1f}%")
        m3.metric("Last Activity", pd.to_datetime(log_df['timestamp']).max().strftime('%H:%M:%S'))
        
        st.dataframe(
            log_df,
            column_config={
                "timestamp": st.column_config.DatetimeColumn("Time", format="D MMM, HH:mm"),
                "confidence_score": st.column_config.ProgressColumn("Confidence", min_value=0, max_value=1, format="%.2f"),
            },
            use_container_width=True
        )
    else:
        st.info("No logs available yet. Make some predictions!")

# --- Footer ---
st.markdown("""
<br><br>
<div style="text-align: center; color: #666; font-size: 0.8rem;">
    © 2026 Credit Risk AI System. All rights reserved.<br>
    Powered by <b>XLM-RoBERTa</b> & <b>Streamlit</b>
</div>
""", unsafe_allow_html=True)
