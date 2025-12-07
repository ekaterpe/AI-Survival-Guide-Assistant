# AI-Survival-Guide-Assistant
An AI-powered helper designed for first-year and international students at Metropolia UAS. It is intended to support students during their initial time at the university, helping them navigate the large amount of information and adapt to the Finnish education system, which can be especially challenging for international students.

## Overview

Metropolia Student Assistant is a lightweight Flask application enhanced with an AI model that helps students navigate schedules, campus services, study rules, and everyday university tasks.

#### The tool is especially useful for:

- first-year students, who often struggle to find reliable information across multiple platforms.

- international and exchange students, who are unfamiliar with the Finnish education system, traditions, and campus culture.

## Features
- AI-powered search across the local knowledge base
- Document similarity search using SentenceTransformer embeddings
- Answer generation via OpenAI (gpt-4o-mini)
- Friendly, easy-to-understand responses for international students
- Simple file-based knowledge structure (one topic = one text file)

## How It Works
The app loads all .txt files from the `knowledge_base/` directory.
Each document is converted into an embedding vector.
When a student asks a question, the system finds the most relevant document.
The AI model generates an answer based on that document’s content.

## Future Improvements
- Multi-language answers
- Relevance scoring and improved ranking
- Admin panel for managing knowledge base files
- Integration with Metropolia systems (Tuudo, OMA, Moodle, calendars)
  
## Running the App
#### Create a .env file with your OpenAI API key:

`OPENAI_API_KEY = "your_key"`

Install dependencies: 
`pip install -r requirements.txt`

Start the server: 
`python app.py`
