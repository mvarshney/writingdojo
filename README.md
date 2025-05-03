# Writing Dojo

A writing assistant application that helps children improve their writing skills through AI-powered feedback and guidance.

## Features

- Multiple AI agents for different aspects of writing assistance:
  - Grading Agent: Evaluates writing samples
  - Topic Suggest Agent: Recommends writing topics
  - Coach Agent: Tracks progress and suggests improvements
- Age-appropriate feedback and guidance
- Progress tracking and visualization
- Multiple writing modes (creative, essay, story)

## Project Structure

```
writing-dojo/
├── frontend/           # React application
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── utils/
│   └── package.json
├── backend/           # Python backend with AutoGen
│   ├── agents/
│   ├── memory/
│   ├── models/
│   └── requirements.txt
└── README.md
```

## Setup Instructions

### Backend Setup

1. Create and activate a virtual environment:
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file with:
   ```
   OPENAI_API_KEY=your_api_key
   ```

### Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm start
   ```

## Development

- Backend API: FastAPI
- Frontend: React with TypeScript and Tailwind CSS
- Database: SQLite
- AI Framework: AutoGen

## License

MIT 