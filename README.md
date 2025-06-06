# AI_Agent
AI Agent for Intelligent Task Automation

# AI Agent with Google Gemini (LangChain)

This is a simple AI assistant built with [LangChain](https://github.com/langchain-ai/langchain), using the [Google Gemini](https://ai.google.dev/) (Generative Language API) as the backend LLM. The assistant can answer questions and tell random jokes using a custom tool.

## Features

- Conversational AI powered by Google Gemini (`gemini-pro`)
- Custom tool for telling random jokes
- Command-line interface

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

It is recommended to use a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

**Required packages:**
- `langchain`
- `langchain-google-genai`
- `langgraph`
- `python-dotenv`

### 3. Get a Google Generative Language API Key

- Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
- Create an API key

### 4. Set up your environment variables

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your-api-key-here
```

### 5. Run the assistant

```bash
python main.py
```

## Usage

- Type your questions or requests in the terminal.
- Type `exit` to quit.

## Model Selection

This project uses the `gemini-pro` model, which is recommended for text-only chat with the Generative Language API key.

If you want to use multimodal (text+image) capabilities, change the model to `gemini-pro-vision` in `main.py`:

```python
model = ChatGoogleGenerativeAI(model="gemini-pro-vision", temperature=0)
```

## Example

```
Welcome! I'm your AI assistant. How can I help you today? Type 'exit' to quit.
You: Tell me a joke
Fetching a random joke...
Assistant: Why did the scarecrow win an award? Because he was outstanding in his field!
```

## License

MIT License

---

**Note:**  
This project is for educational purposes. Make sure to keep your API key secure and do not share it publicly.
