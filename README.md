# LangChain Text Transformation Pipeline

## Description

This project demonstrates a multi-stage text transformation pipeline using LangChain and OpenAI's language models. The application:

1. Generates 8-10 sentences about Linus Torvalds's contributions to software development
2. Rewrites the generated text in William Shakespeare's style
3. Formats the Shakespearean text in Markdown with specific formatting rules
4. Saves the final output to a file named "linus.md"

The pipeline showcases how to chain multiple LLM operations together for creative text transformation tasks.

## Project Dependencies

- Python 3.13+
- langchain (>=0.3.27)
- langchain-openai (>=0.3.33)
- python-dotenv (>=1.1.1)

## Environment Variables

The application requires the following environment variables:

- `GEP_API_KEY`: API key for accessing the LLMs on the Generative engine platform
- `GEP_API_URL`: Base URL for the Generative Engine API endpoint

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set up environment with uv

```bash
# Install uv if you haven't already
pip install uv

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
uv sync
```

### 4. Create a .env file

Create a `.env` file in the project root with the following content:

```
GEP_API_KEY=your_api_key_here
GEP_API_URL=your_api_url_here
```

### 5. Run the application

```bash
python main.py
```

## Output

The application will:
1. Print the generated text about Linus Torvalds
2. Print the Shakespeare-style rewritten version
3. Print the Markdown-formatted text
4. Save the final output to a file named "linus.md"
