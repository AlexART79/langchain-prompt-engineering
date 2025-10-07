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
python 01-linus.py
```

## Prompts and outputs

### 1. Initial text generation prompt:
```
"""
You are a professional and experienced tech blog text writer. 
Write a 8-10 sentences text on specified topic:
-------
{topic}
-------
Answer:
"""
```

### Result:
```
Linus Torvalds, a Finnish software engineer, is widely recognized as the mastermind 
behind the creation of the Linux kernel, a project that has profoundly influenced software 
development and technology innovation. Born in 1969, Torvalds initiated the Linux project in 1991, 
aiming to create a free and open-source operating system. 
His contributions extend beyond just the kernel; he has been instrumental in fostering a 
collaborative development environment that has led to the creation of numerous open-source projects. 
Torvalds's work has not only democratized access to technology but has also set a precedent for 
community-driven software development. His leadership and vision have inspired countless 
developers worldwide, making Linux a cornerstone of modern computing. 
Torvalds's influence is evident in various sectors, from personal computing to cloud infrastructure, 
and his commitment to open-source principles continues to drive innovation and collaboration in the 
tech industry.

```

### 2. Shakespeare prompt:
```
"""
You are a professional and experienced text rewriter, specialized in rewriting given text in William Shakespeare style. 
Lines should be short, resembling old school Shakespeare poetry formatting, like in example below.

Example:
Torvalds's labors have likewise wielded great 
Influence upon the practices of software licensing, 
advocating for the GNU General Public License (GPL). 
...

Rewrite given passage accordingly:
-------
{text}
-------
Answer:
"""
```

### Result:
```
Linus Torvalds, Finnish engineer rare,
Creator of Linux kernel, a project so fair.
Born in '69, in '91 he did start,
A free, open-source OS, his noble art.

Not just kernel, his vision did spread,
A collaborative realm where many tread.
Open-source projects, by his hand, took flight,
Technology's gate, now open to all.

Democratized tech, by his hand it was wrought,
Community-driven, a new path he sought.
His guidance, his sight, to developers did gleam,
Linux, a pillar in computing's dream.

From personal devices to clouds in the sky,
His influence, vast, in tech industry.
Open-source principles, his steadfast creed,
Innovation and teamwork, by his deeds freed.
```

### 3. MD formatter prompt:
```
"""
You are a professional text formatting assistant. Format given text in Markdown. 
Add title as 3rd leve heading.
Highlight names in bold (like **John Doe**, **Sarah**, etc).
Highlight tech product or brand names in italic (like *Microsoft*, *Git* etc).
DO NOT include "```markdown" and "```" marks in the final answer!
-------
{text}
-------
Answer:
"""
```

### Result:
```markdown
### Linus Torvalds, Finnish Engineer

**Linus Torvalds**, Finnish engineer rare,
Creator of *Linux* kernel, a project so fair.
Born in '69, in '91 he did start,
A free, open-source OS, his noble art.

Not just kernel, his vision did spread,
A collaborative realm where many tread.
Open-source projects, by his hand, took flight,
Technology's gate, now open to all.

Democratized tech, by his hand it was wrought,
Community-driven, a new path he sought.
His guidance, his sight, to developers did gleam,
*Linux*, a pillar in computing's dream.

From personal devices to clouds in the sky,
His influence, vast, in tech industry.
Open-source principles, his steadfast creed,
Innovation and teamwork, by his deeds freed.
```
