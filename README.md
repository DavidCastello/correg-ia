## correg-ia

# Flask App for Exam Correction with ChatGPT

This web application is designed to correct exams using ChatGPT. The application provides an interface where users can input the text of an exam and receive corrections.
The application is designed to handle raw text from a written exam. Use google lens to copy all text from a written exam and copy directly the text directly into the app, or copy the text directly from a text file on your computer.

<img width="467" alt="image" src="https://github.com/DavidCastello/correg-ia/assets/50247592/e2d72b1d-86c6-41f2-b27a-2b2318ae7636">

<img width="416" alt="image" src="https://github.com/DavidCastello/correg-ia/assets/50247592/b98e1b52-2004-4f5d-9118-1309b0e0825d">

<img width="405" alt="image" src="https://github.com/DavidCastello/correg-ia/assets/50247592/77ff0921-6a08-4219-976a-2805a8f435e2">

## Features

1. **Analysis of Text**: Enter the text of an exam to get an analysis.
2. **Correction**: Submit the analyzed exam in JSON format to get corrections.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone this repository:

```
git clone [repository_link]
cd [repository_directory]
```

Replace `[repository_link]` with the link to your repository and `[repository_directory]` with the name of the directory where the repository's content is stored.

2. Install the required dependencies:

```
pip install flask
pip install openai
pip install json
pip install re
pip install ast
```

## Running the Application

To run the Flask app:

```
python app.py
```

This will start the Flask development server on `http://127.0.0.1:5000/`. Open this URL in a web browser to access the application.

## Usage

1. Navigate to the main page (`http://127.0.0.1:5000/`).
2. Input the text of the exam to be analyzed.
3. Submit to get an analysis of the text in JSON format.
4. Make modifications to the JSON if needed, then submit for corrections.
