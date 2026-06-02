# Folder Analyzer

A Python desktop application that analyzes folders and displays useful information about their contents.

## Features

* Browse and select folders using a graphical interface
* Count total files
* Count total folders
* Calculate total folder size
* Display files sorted by size
* Convert file sizes into human-readable units (B, KB, MB, GB, TB)
* Display file type statistics

## Technologies Used

* Python
* Tkinter
* os module

## How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project directory

```bash
cd folder-analyzer
```

3. Run the application

```bash
python gui.py
```

## Current Output

The application displays:

* Selected folder path
* Number of folders
* Number of files
* Total size
* Files sorted by size
* File type counts

## Project Structure

```text
folder-analyzer/
├── main.py        # Analysis logic
├── gui.py         # Tkinter interface
├── README.md
└── .gitignore
```

## Future Improvements

* Scrollable file list
* Better GUI layout
* Oldest and newest file analysis
* Duplicate file detection
* Export results to a text file
* CustomTkinter interface

