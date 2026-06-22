import requests
from config import GROQ_API_KEY
from groq import Groq
import os
import time

def call_llm(prompt,max_retries=3):
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set. Please check your .env file.")
    client=Groq(api_key=GROQ_API_KEY,)
    for attempt in range(1,max_retries+1):
        try:
            chat_completion=client.chat.completions.create(
                messages=[
                    {
                        "role":"system",
                        "content":"You are a helpful assistant that provides concise and accurate answers to user queries."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=500,
                stream=False
            )
            response=chat_completion.choices[0].message.content
            if not response:
                raise ValueError("Received empty response from LLM.")
            return chat_completion.choices[0].message.content
        except Exception as e:
            error_str=str(e).lower()
            is_rate_limit="rate limit" in error_str or "too many requests" in error_str or "429" in error_str
            if attempt < max_retries:
                if is_rate_limit:
                    wait_time=5**attempt
                    print(f"Rate limit hit. Retrying in {wait_time}seconds.")
                else: 
                    wait_time=2**attempt
                    print(f"Error occurred: {e}. Retrying in {wait_time} seconds.")
                    
                time.sleep(wait_time)   
            else:
                return "Error: Unable to get a response from the LLM after multiple attempts. Please try again later."