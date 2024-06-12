# Questions Competition

This project provides a serverless function for fetching trivia questions from the Open Trivia Database. It handles GET requests and returns trivia questions in plain text format.

## Features

- Retrieve a specified number of trivia questions.
- Retrieve trivia questions from a specified category..

## API Endpoints

### `/questions?amount=NUMBER`

Fetches a specified number of trivia questions. If the requested number is more than 50, it returns the maximum of 50 questions.

### `/questions?category=CATEGORY_ID`

Fetches 10 trivia questions from a specified category. If the category ID is 33 or higher, it returns a special message "You have just 32 category".

### `/questions`

Fetches the default 10 trivia questions if no query parameters are provided.

## Deployed Links

- [20 Questions](https://questions-competition-htjrk5ase-abdullah-qdads-projects.vercel.app/api/questions?amount=20)
- [Max Questions](https://questions-competition-htjrk5ase-abdullah-qdads-projects.vercel.app/api/questions?amount=51)
- [Sports Category](https://questions-competition-htjrk5ase-abdullah-qdads-projects.vercel.app/api/questions?category=21)
- [Invalid Category](https://questions-competition-htjrk5ase-abdullah-qdads-projects.vercel.app/api/questions?category=33)
- [Default Questions](https://questions-competition-htjrk5ase-abdullah-qdads-projects.vercel.app/api/questions)
