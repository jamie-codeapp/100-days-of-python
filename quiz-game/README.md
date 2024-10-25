# Quiz Game

A simple command-line quiz game that asks True/False questions about geography. The game reads from a set of questions, asks the user to answer, provides feedback, and displays the final score.

## Project Structure

This project includes the following files:

-   **data.py**: Contains a list of dictionaries, each with details for a geography question (type, difficulty, category, question text, correct answer, and incorrect answers).

-   **question_model.py**: Defines a `Question` class to represent a question with its text and answer.

-   **quiz_brain.py**: Defines a `QuizBrain` class that manages the quiz logic:

    -   Tracks the current question number and score.
    -   Provides methods to present the next question (`next_question()`), check if there are remaining questions (`still_has_questions()`), and validate the user's answer (`check_answer()`).

-   **main.py**: The main script that initializes and runs the quiz:
    -   Imports questions from `data.py` and uses `Question` instances for each.
    -   Initializes the `QuizBrain` with these questions and begins the quiz.
    -   Displays the user’s final score once all questions are answered.

## How to Run

1. Ensure you have Python installed on your machine.
2. Download or clone the repository.
3. Navigate to the directory containing `main.py`.
4. Run the following command:

    ```
    python main.py
    ```

5. Follow the prompts to answer each question.

## Example

```
Q.1: Nova Scotia is on the east coast of Canada. (True/False): True
You got it right!
The correct answer was: True.
Your current score is: 1/1
```

## Requirements

Python 3.x
