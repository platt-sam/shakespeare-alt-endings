# Shakespeare Alternate Ending Generator

This is my project for SOU Hackathon 2023. GitHub doesn't allow users to fork their own repositories.

If you would like to see other participants' projects, the main repository is https://github.com/platt-sam/souhackathon2023.

## Purpose

I wanted to create a simple to use application that allows users to generate alternate endings for Shakespeare plays.

## Process

### AI Text Generation

I used Hugging Face's transformers module to do text generation, which I was familiar with.

I found the complete scripts of several popular Shakespeare plays, and downloaded them as .txt files.

Unfortunately the input limit is 1024 characters, so I had to determine what would be the best characters to use. I decided to use the first 1024 characters of the fifth act of several popular Shakespeare plays.

### GUI (Graphical User Interface)

I used PySimpleGUI to create the GUI for this app.

## How to Use This Program

1. Clone this project onto your machine. In a terminal on your computer, enter this command:

    `git clone https://github.com/platt-sam/sam-souhackathon2023.git`

2. Check that you have Python (v 3.x) installed on your computer. In a terminal, enter the command:

    `python3 --version`

    If Python 3 is installed you should see a message like "Python 3.x". If you see a message like "command not found", you'll want to install Python 3 at https://www.python.org/downloads/

3. From inside the `sam-souhackathon2023` folder, follow the usage guide below to run the project. Please understand that it may take up to a few minutes to run this program depending on your CPU.

## Usage

usage: `python3 main.py operating_system`
> operating_system: `linux`, `mac`, or `windows`
