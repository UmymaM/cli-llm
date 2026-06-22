from dotenv import load_dotenv
import os
from groq import Groq
import requests

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")

