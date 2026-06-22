LLM CLI Tool (Groq API)

A command-line interface (CLI) application that connects to a Large Language Model using the Groq API. The tool allows users to enter prompts and receive AI-generated responses directly in the terminal.

Project Structure:
llm-cli/
├── main.py
├── llm_client.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore

Setup Instructions:

1. Create virtual environment:
python -m venv .venv

2. Activate environment:
.venv\Scripts\activate  (Windows)

3. Install dependencies:
pip install -r requirements.txt

4. Create .env file:
GROQ_API_KEY=your_api_key_here

5. Run the application:
python main.py

Features:
- CLI-based LLM interaction
- Groq API integration (Llama 3 model)
- Environment variable-based configuration
- Retry logic with exponential backoff
- Basic error handling
