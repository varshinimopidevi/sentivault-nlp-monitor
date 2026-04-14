import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from analyzer import analyze_sentiment

# 1. Page Configuration for a Software Dashboard
st.set_page_config(page_title="AI Service Monitor", layout="wide")

st.title("🖥️ AI Sentiment Service: System Monitor")
st.markdown("---")

# 2. Initialize System Logs (Simulating a Database in memory)
if 'system_logs' not in st.session_state:
    st.session_state.system_logs = []

# 3. Main Interface - Sidebar
with st.sidebar:
    st.header("⚙️ Service Status")
    st.success("NLP Engine: Online")
    st.info("Version: v2.1.0 (Local-VADER)")
    if st.button("🗑️ Clear System Logs"):
        st.session_state.system_logs = []
        st.rerun()

# 4. Main Layout: Two Columns
col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("🧪 Live API Tester")
    user_input = st.text_input("Send a payload to AI Engine:", placeholder="Type something...")
    
    if st.button("🚀 Execute Request"):
        if user_input:
            # Execute AI Logic
            label, score = analyze_sentiment(user_input)
            
            # Create a Log Entry (Developer Skill: Data Structuring)
            log_entry = {
                "Timestamp": datetime.now().strftime("%H:%M:%S"),
                "Payload": user_input,
                "Verdict": label,
                "Confidence": score,
                "Latency": "12ms" # Simulated
            }
            # Save to logs
            st.session_state.system_logs.append(log_entry)
            
            st.code(f"Response: {{'verdict': '{label}', 'confidence': {score}}}")
        else:
            st.warning("Empty payload detected.")

with col_right:
    st.subheader("📈 Model Performance Metrics")
    if st.session_state.system_logs:
        df = pd.DataFrame(st.session_state.system_logs)
        
        # Pie Chart: Service Distribution (Dev Skill: UI/UX visualization)
        fig = px.pie(df, names='Verdict', hole=0.5, 
                     color='Verdict',
                     color_discrete_map={'POSITIVE':'#28a745', 'NEGATIVE':'#dc3545', 'NEUTRAL':'#ffc107'},
                     title="Request Result Distribution")
        st.plotly_chart(fig,width="stretch")
    else:
        st.write("No system activity recorded yet.")

# 5. The "Developer" Part: System Request Logs Table
st.markdown("---")
st.subheader("📄 System Request Logs (Audit Trail)")

if st.session_state.system_logs:
    df_logs = pd.DataFrame(st.session_state.system_logs)
    # Using st.dataframe makes a searchable, sortable table
    st.dataframe(df_logs, width="stretch")
    
    # Download Button for Logs (Simulating an Export Feature)
    csv = df_logs.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Export Logs to CSV", data=csv, file_name="system_logs.csv", mime="text/csv")
else:
    st.info("System idle. Send a request to generate logs.")

st.sidebar.markdown("### Built by Varshini Mopidevi")