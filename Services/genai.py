from google import genai
import streamlit as st
from pydantic import BaseModel
from typing import Literal
from typing import Annotated
from typing import List
from google.genai import types
import ast
from annotated_types import Len
import time

class QuestionGenertaionResponseConfig(BaseModel):
    question: str
    options: Annotated[list[str], Len(min_length=4, max_length=4)]
    correct_option: Literal["A", "B", "C", "D"]
    explanation: str

try:
    CLIENT = genai.Client(api_key=st.secrets['GEMINI_API_KEY'])
except:
    st.error("Error connecting to Gemini", icon="🚨")

SYSTEM_INSTRUCTIONS = """You are a question generator for a quiz application that is intended to evaluate knowledge on a person on a perticular topic. You will be given a topic, difficulty level and a list of previously asked questions. Your job is to follow the below steps and generate questions, options and explanations for the application

Instructions:
- You are a master of the provided topic, and this quiz application is to test profeciency of students in this topic.
- Based on the difficulty_level, generate an interesting question along with options and an explanation.
- Make sure that no question is repeated from the list_of_questions provided. 
- You are required to generate content only in the below format:
    question: str
    options: [option1: str, option2: str, option3: str, option4: str]
    correct_option: ["A", "B", "C", "D"]
    explanation: str
- Make sure that you do not deviate from the topic, and generate good, meaningful and sensible questions that could be used to evaluate knowledge on the topic."""

def generate_question():
    time.sleep(1.5)
    response = CLIENT.models.generate_content(
        model="gemini-2.0-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTIONS,
            temperature=1,
            response_schema=QuestionGenertaionResponseConfig,
            response_mime_type="application/json"
        ),
        contents=f"""topic: {st.session_state.selected_topic}
        current_difficulty_level: {st.session_state.difficulty_level}
        list_of_questions: {st.session_state.data['question'].to_list()}""",
    )
    return ast.literal_eval(response.text)