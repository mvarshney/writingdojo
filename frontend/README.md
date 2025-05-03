# Writing Dojo Frontend

This is the frontend application for the Writing Dojo, built with React, TypeScript, and Tailwind CSS.

## Features

- Child profile management
- Writing session interface
- Progress tracking
- Real-time word count
- Timer functionality
- Assessment display

## Prerequisites

- Node.js 16+
- npm or yarn

## Installation

1. Install dependencies:
```bash
npm install
# or
yarn install
```

2. Create a `.env` file in the frontend directory with the following variables:
```
REACT_APP_API_URL=http://localhost:8000
```

## Running the Application

Start the development server:
```bash
npm start
# or
yarn start
```

The application will be available at `http://localhost:3000`

## Project Structure

```
frontend/
├── public/              # Static files
├── src/
│   ├── components/     # React components
│   │   ├── TopBar.tsx  # Navigation and child selection
│   │   ├── WritingSession.tsx  # Main writing interface
│   │   ├── WritingEditor.tsx   # Text editor component
│   │   ├── Timer.tsx           # Timer component
│   │   ├── TopicDisplay.tsx    # Topic display component
│   │   └── AssessmentDisplay.tsx # Assessment display component
│   ├── App.tsx        # Main application component
│   └── index.tsx      # Application entry point
├── package.json       # Dependencies and scripts
└── tsconfig.json     # TypeScript configuration
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
npm test
# or
yarn test
```

## Building for Production

Create a production build:
```bash
npm run build
# or
yarn build
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
