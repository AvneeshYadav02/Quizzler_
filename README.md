# Quizzler: A Python Quiz Application

This is a GUI-based quiz application written in Python. It's designed to be a simple and fun way to answer a series of true or false questions. The application is built with tkinter for the user interface and fetches fresh questions from the Open Trivia Database API for a new experience every time you play.

Features

    Dynamic Questions: Fetches 10 true/false questions from the Open Trivia Database API for a unique quiz each time.

    Simple GUI: A clean and straightforward user interface using the tkinter library.

    Real-time Feedback: Provides instant visual feedback (green for correct, red for incorrect) after each answer.

    Score Tracking: Keeps a running tally of your correct answers throughout the quiz.

    End-of-Quiz Message: Notifies you when you've reached the end of the questions.

How to Install and Run

To get started with Quizzler, you'll need Python installed on your system.
The project uses the requests library to fetch data from the API.

    Clone the Repository (or download the project files).

    Navigate to the Project Directory in your terminal.

    Install the necessary library:
    Bash

pip install requests

Run the main script:
Bash

    python main.py

Project Structure

The project is broken down into several modular files to keep the code organized and readable.

    main.py: The entry point of the application. It initializes the question bank, quiz logic, and the user interface.

    ui.py: Handles all aspects of the graphical user interface using tkinter, including creating the window, canvas, buttons, and displaying questions and scores.

    quiz_brain.py: Manages the quiz logic, such as tracking the current question, checking answers, updating the score, and determining if there are more questions left.

    question_model.py: A simple class that acts as a blueprint for creating question objects.

    data.py: Fetches question data from the Open Trivia Database API.

Customizing the Quiz

You can easily modify the type of questions you get by editing the data.py file. The parameters dictionary controls the API request. You can change the following to get a different set of questions:

    amount: The number of questions you want.

    type: The question type (e.g., multiple for multiple-choice).

    category: A specific category ID.

You can find a full list of categories and their corresponding IDs on the Open Trivia Database website.

License

This project is open-source. Feel free to use and modify it as you see fit.
