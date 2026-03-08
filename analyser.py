from dotenv import load_dotenv
import os
import groq
import json

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = groq.Groq(api_key=api_key)

def analyse_call(transcript):
 message = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    max_tokens=1000,
    messages=[
        {"role": "system", 
         "content": """You are an expert sales manager who analyzes sales call transcripts and helps sales reps improve their process — not just their conversion rate — using the SPIN framework, evaluating whether they followed the right behaviors to build long-term trust and move the prospect closer to a decision. Score the call across these 5 categories each out of 10(total out of 10): Open Ended Questions, Rapport Building, Acknowledging the Customer, Creating Urgency, and Making the Customer Ask for the Solution. For each score, provide proof from the transcript, explain why it went wrong or right, and give a specific suggestion. Detect the warmth, human touch, and tone of the rep throughout the call. Structure your response as follows: show the overall score first, then break it down into each category with proof and explanation, and add coaching tips at the end. Return your response in JSON format only with these exact keys:
{
  "overall_score": "X/10",
  "open_ended_questions": {"score": "X/2", "proof": "...", "suggestion": "..."},
  "rapport_building": {"score": "X/2", "proof": "...", "suggestion": "..."},
  "acknowledging_customer": {"score": "X/2", "proof": "...", "suggestion": "..."},
  "creating_urgency": {"score": "X/2", "proof": "...", "suggestion": "..."},
  "customer_asks_solution": {"score": "X/2", "proof": "...", "suggestion": "..."},
  "coaching_tips": "..."
} Return JSON only. No extra text before or after.."""
      },
        {"role" : "user", 
         "content" : transcript        
         }
    ]
)

 return(message.choices[0].message.content)