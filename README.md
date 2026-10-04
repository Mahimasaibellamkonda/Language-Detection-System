# Language Detection System

A web-based Natural Language Processing application that automatically detects the language of the given text and displays the detected language, language code, and confidence score.

## Features

* Detects the language of user-provided text
* Displays the detected language name
* Displays the language code
* Shows the detection confidence
* Simple and responsive web interface
* Built using Flask and Python
* Uses the `langdetect` NLP library

## Technologies Used

* Python
* Flask
* HTML5
* CSS3
* LangDetect

## Project Structure

```text
Language-Detection-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation

### 1. Clone or download the project

Open the project folder in your terminal.

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

## Running the Application

Run the following command:

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000
```

Open the address in a web browser.

## How It Works

1. The user enters text into the input box.
2. Flask receives the text through a POST request.
3. The `langdetect` library analyzes the text.
4. The system identifies the most likely language.
5. The language code and confidence score are calculated.
6. The result is displayed on the web page.

## Example

### Input

```text
This is a natural language processing project.
```

### Output

```text
Language: English
Language Code: en
Confidence: High
```

## Applications

Language detection can be used in:

* Multilingual websites
* Chat applications
* Translation systems
* Search engines
* Social media platforms
* Customer support systems
* Content classification
* Text preprocessing pipelines

## Purpose

This project demonstrates the practical application of Natural Language Processing for automatically identifying the language of textual data through a web-based interface.


