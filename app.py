import json
import streamlit as st
from analyser import analyse_call
import pandas as pd
from io import BytesIO

def get_score_label(score_string):
    score = int(score_string.split("/")[0])
    if score >= 8:
        return "🟢 Good"
    elif score >= 6:
        return "🟡 Average"
    else:
        return "🔴 Needs Work"

st.title("Sales Call Analyzer")
if "transcript" not in st.session_state:
    st.session_state.transcript = ""

with st.sidebar:
    st.markdown("## How to Use")
    st.markdown("""
    1. Paste your sales call transcript in the text area or use the sample transcript.
    2. Click "Analyze Call" to get a detailed analysis based on the SPIN framework.
    3. Review the overall score, category breakdowns, and coaching tips.
    4. Download the analysis report as an Excel file for further review or sharing.
    """)
    st.markdown("---")
    st.markdown("### Scoring Guide")
    st.markdown("""
                 - 🟢 **Good** — 80% and above
                 - 🟡 **Average** — 60% to 79%
                 - 🔴 **Needs Work** — below 60%
                 """)
    st.markdown("---")
    st.markdown("### Framework Overview")
    st.markdown("Scored using the **SPIN Selling** framework, which evaluates the following categories:")

sample_button = st.button("Use sample Transcript")
analyze_button = st.button("Analyze Call")
clear_button = st.button("Clear ")
        
if sample_button:
        st.session_state.transcript = """Rep: Hi, is this Sarah? Great, this is James from TechFlow Solutions. I'm calling because we help businesses like yours manage their customer relationships more effectively. I wanted to take 2 minutes of your time to tell you about our product.
Customer: Sure, I have a few minutes.
Rep: Perfect. So TechFlow is a CRM platform with over 50 features including automation, reporting, pipeline tracking, email integration and—
Customer: We actually already use a CRM.
Rep: Oh okay, but ours is better. We have more features and better pricing. Can I ask what CRM you use?
Customer: We use HubSpot but honestly the team doesn't really use it consistently.
Rep: Right, well our onboarding is very simple. So what size is your sales team?
Customer: About 12 people.
Rep: Great, so with 12 people you'd be on our Business Plan at $299 a month. It includes everything I mentioned plus dedicated support.
Customer: That sounds expensive. We're already paying for HubSpot.
Rep: I understand but think of the ROI. Our customers see 30% more productivity. Can we schedule a demo?
Customer: I'm not sure, let me think about it.
Rep: I can do Tuesday or Wednesday this week, which works better?
Customer: Maybe Tuesday but I really need to think about it.
Rep: Great I'll book Tuesday at 2pm. You won't regret it!
"""

if clear_button:
    st.session_state.transcript = ""
    
transcript = st.text_area("Enter your Transcript here", value=st.session_state.transcript)

if analyze_button:
    if transcript=="":
        st.error("Please enter a transcript to analyze.")
    else:
       with st.spinner('Analysing your call...'):
        result=analyse_call(transcript)
    # Convert the JSON string to a Python dictionary
        data = json.loads(result) 
 #Overall score KPI card
        st.markdown("## Call Analysis Results")
        st.metric("Overall Score", data["overall_score"], delta=get_score_label(data["overall_score"]))

 
 # % category KPI cards in 2 rows
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Open Ended Questions", data["open_ended_questions"]["score"],delta=get_score_label(data["open_ended_questions"]["score"]))

        with col2:
            st.metric("Rapport Building", data["rapport_building"]["score"],delta=get_score_label(data["rapport_building"]["score"]))

        with col3:
            st.metric("Acknowledging Customer", data["acknowledging_customer"]["score"],delta=get_score_label(data["acknowledging_customer"]["score"]))
            
        col4,col5 = st.columns(2)
        with col4:
            st.metric("Creating Urgency", data["creating_urgency"]["score"],delta=get_score_label(data["creating_urgency"]["score"]))

        with col5:
            st.metric("Customer Asks for Solution", data["customer_asks_solution"]["score"],delta=get_score_label(data["customer_asks_solution"]["score"]))
            
            # Detailed breakdown for each category with proof and suggestions
        st.markdown("### 📋 Detailed Breakdown")
            
        st.markdown("**Open Ended Questions**")
        st.write("📌 Proof:", data["open_ended_questions"]["proof"])
        st.write("💡 Suggestion:", data["open_ended_questions"]["suggestion"])
        st.markdown("---")
        
        st.markdown("**Rapport Building**")
        st.write("📌 Proof:", data["rapport_building"]["proof"])
        st.write("💡 Suggestion:", data["rapport_building"]["suggestion"])
        st.markdown("---")

        
        st.markdown("**Acknowledging Customer**")
        st.write("📌 Proof:", data["acknowledging_customer"]["proof"])
        st.write("💡 Suggestion:", data["acknowledging_customer"]["suggestion"])
        st.markdown("---")    
    
        
        st.markdown("**Creating Urgency**")
        st.write("📌 Proof:", data["creating_urgency"]["proof"])
        st.write("💡 Suggestion:", data["creating_urgency"]["suggestion"])
        st.markdown("---")
          
        st.markdown("**Customer Asks for Solution**")
        st.write("📌 Proof:", data["customer_asks_solution"]["proof"])
        st.write("💡 Suggestion:", data["customer_asks_solution"]["suggestion"])
        st.markdown("---")

        st.markdown("### 💡 coaching tips")
        st.write(data["coaching_tips"])
        
        # Create dataframe
        df = pd.DataFrame([
        {"Category": "Open Ended Questions", "score": data["open_ended_questions"]["score"], "Proof": data["open_ended_questions"]["proof"], "Suggestion": data["open_ended_questions"]["suggestion"]},
        {"Category": "Rapport Building", "score": data["rapport_building"]["score"], "Proof": data["rapport_building"]["proof"], "Suggestion": data["rapport_building"]["suggestion"]},
        {"Category": "Acknowledging Customer", "Score": data["acknowledging_customer"]["score"], "Proof": data["acknowledging_customer"]["proof"], "Suggestion": data["acknowledging_customer"]["suggestion"]},
        {"Category": "Creating Urgency", "Score": data["creating_urgency"]["score"], "Proof": data["creating_urgency"]["proof"], "Suggestion": data["creating_urgency"]["suggestion"]},
        {"Category": "Customer Asks Solution", "Score": data["customer_asks_solution"]["score"], "Proof": data["customer_asks_solution"]["proof"], "Suggestion": data["customer_asks_solution"]["suggestion"]},
        {"Category": "OVERALL", "Score": data["overall_score"], "Proof": "", "Suggestion": ""}
        ])

        # Export to Excel
        buffer = BytesIO()
        df.to_excel(buffer, index=False)
        buffer.seek(0)

        st.download_button(
        label="📥 Download Excel Report",
        data=buffer,
        file_name="sales_call_analysis.xlsx",
        mime="application/vnd.ms-excel"
        )


   