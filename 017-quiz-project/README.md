# Quiz Application

Welcome to the Quiz application! This Python console-based quiz allows you to test your knowledge with a set of questions from the Open Trivia Database.

## Table of Contents

1. [Description](#description)
2. [Code Structure](#code-structure)
3. [Usage](#usage)

## Description

The Quiz application is a simple console-based program designed to quiz users on various topics. The application consists of several modules, each serving a specific purpose to ensure clean and modular code. The key modules include:

- **main.py**: The main script that initializes the quiz, processes questions, and displays the final score.

- **data.py**: Contains the question data sourced from the Open Trivia Database.

- **question_model.py**: Defines the `Question` class, representing individual quiz questions with text and correct answers.

- **quiz_brain.py**: Implements the `QuizBrain` class, managing the quiz logic, tracking the question number, and calculating the user's score.

## Code Structure

- **main.py**: Initializes the quiz by creating a list of questions and starting the quiz loop.

- **data.py**: Holds the question data in the form of a list.

- **question_model.py**: Defines the `Question` class with text and correct answer attributes.

- **quiz_brain.py**: Implements the `QuizBrain` class, which manages the quiz logic, question tracking, and user scoring.

## Usage

Run the application using the following command:

```bash
python main.py
```

Answer the questions displayed on the console by entering 'True' or 'False' when prompted. After completing the quiz, your final score will be displayed.
