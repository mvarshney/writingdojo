# Writing Dojo Backend

This is the backend service for the Writing Dojo application, built with FastAPI and OpenAI's GPT models.

## Features

- Topic generation for children's writing
- Writing assessment and feedback
- Progress tracking and analysis
- RESTful API endpoints

## Prerequisites

- Python 3.8+
- PostgreSQL database
- OpenAI API key

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the backend directory with the following variables:
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/writing_dojo
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
DEBUG=True
ENVIRONMENT=development
```

## Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
backend/
├── agents/                 # AI agents for different tasks
│   ├── base_agent.py      # Base agent class
│   ├── topic_agent.py     # Topic generation agent
│   ├── assessment_agent.py # Writing assessment agent
│   ├── feedback_agent.py  # Feedback generation agent
│   ├── progress_agent.py  # Progress tracking agent
│   └── orchestrator.py    # Agent coordination
├── routers/               # API routes
│   └── agents.py         # Agent-related endpoints
├── config.py             # Configuration settings
├── main.py              # FastAPI application
└── requirements.txt     # Python dependencies
```

## Development

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit them:
```bash
git add .
git commit -m "Description of your changes"
```

3. Push your changes:
```bash
git push origin feature/your-feature-name
```

4. Create a pull request on GitHub

## Testing

Run the test suite:
```bash
pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 