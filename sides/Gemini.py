import streamlit as st
import requests

def get_quiz_data(text, gemini_api_key):
  url = "https://your-gemini-endpoint/generate"  
  headers = {"Authorization": f"Bearer {gemini_api_key}"}
  payload = {
      "prompt": f"""
      You are a helpful assistant programmed to generate questions based on any text provided. For every chunk of text you receive, you're tasked with designing 5 distinct questions. Each of these questions will be accompanied by 3 possible answers: one correct answer and two incorrect ones. 

      Your output should be shaped as follows:

      1. An outer list that contains 5 inner lists.
      2. Each inner list represents a set of question and answers, and contains exactly 4 strings in this order:
      - The generated question.
      - The correct answer.
      - The first incorrect answer.
      - The second incorrect answer.

      Process the following text: {text}
      """,
      "max_tokens": 1024  # Adjust max tokens as needed
  }

  try:
      response = requests.post(url, headers=headers, json=payload)
      response.raise_for_status()
      return response.json()["generated_text"]
  except requests.exceptions.RequestException as e:
      st.error(f"An error occurred: {str(e)}")
      st.stop()
  except Exception as e:
      st.error(f"Unexpected error: {str(e)}")
      st.stop()


