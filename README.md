# Writing Dojo

A writing application designed to help children improve their writing skills through guided practice, AI-powered feedback, and progress tracking.

## Features

- Child profile management
- Age-appropriate writing topics
- Real-time writing interface
- AI-powered assessment and feedback
- Progress tracking and analysis
- Child-friendly interface

## Tech Stack

### Frontend
- React
- TypeScript
- Tailwind CSS
- React Router

### Backend
- FastAPI
- OpenAI GPT
- PostgreSQL
- SQLAlchemy

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/writing-dojo.git
cd writing-dojo
```

2. Set up the backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up the frontend:
```bash
cd ../frontend
npm install
# or
yarn install
```

4. Configure environment variables:
   - Backend: Create `.env` file in `backend/` directory
   - Frontend: Create `.env` file in `frontend/` directory

5. Start the development servers:
   - Backend: `cd backend && uvicorn main:app --reload`
   - Frontend: `cd frontend && npm start`

## Project Structure

```
writing-dojo/
├── backend/              # FastAPI backend
│   ├── agents/          # AI agents
│   ├── routers/         # API routes
│   ├── config.py        # Configuration
│   └── main.py         # FastAPI application
├── frontend/            # React frontend
│   ├── src/
│   │   ├── components/ # React components
│   │   ├── App.tsx    # Main application
│   │   └── index.tsx  # Entry point
│   └── package.json   # Dependencies
└── README.md          # Project documentation
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

### Backend
```bash
cd backend
pytest
```

### Frontend
```bash
cd frontend
npm test
# or
yarn test
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT models
- The FastAPI and React communities for their excellent documentation and tools 