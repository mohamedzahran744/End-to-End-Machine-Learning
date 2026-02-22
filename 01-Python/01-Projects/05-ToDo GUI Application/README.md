# ToDo App

A simple and lightweight task management application built with Python's Tkinter library.

## Description

This ToDo App provides a clean graphical interface for managing your daily tasks. You can easily add new tasks, view them in a numbered list, and delete completed tasks by their number.

## Features

- **Add Tasks**: Enter and submit tasks to your to-do list
- **View Tasks**: All tasks are displayed in a numbered list format
- **Delete Tasks**: Remove tasks by specifying their task number
- **Error Handling**: Built-in validation for empty inputs and invalid operations
- **Simple UI**: Clean, intuitive interface with a light green theme

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Ensure Python 3.x is installed on your system
2. Download the `todo_app.py` file
3. No additional packages need to be installed (Tkinter is included with Python)

## Usage

Run the application using:

```bash
python todo_app.py
```

### How to Use

1. **Adding a Task**:
   - Type your task in the "Enter Your Task" field
   - Click the "Submit" button
   - Your task will appear in the list with a number

2. **Deleting a Task**:
   - Enter the task number you want to delete in the "Delete Task Number" field
   - Click the "Delete" button
   - The task will be removed and remaining tasks will be renumbered

3. **Exiting**:
   - Click the "Exit" button to close the application

## Interface Layout

- **Task Entry Field**: Input box for new tasks
- **Submit Button**: Adds the entered task to the list
- **Task Display Area**: Shows all tasks with their numbers
- **Delete Task Number Field**: Input box for specifying which task to delete
- **Delete Button**: Removes the specified task
- **Exit Button**: Closes the application

## Error Messages

- **Input Error**: Displayed when trying to submit an empty task
- **No Task**: Shown when attempting to delete from an empty list
- **Input Error**: Appears when the delete field is empty

## Technical Details

- **GUI Framework**: Tkinter
- **Window Size**: 250x300 pixels
- **Background Color**: Light green
- **Font**: Lucida 13 for text area

## Code Structure

- `inputError()`: Validates task input
- `clear_taskNumberField()`: Clears the task number field
- `clear_taskField()`: Clears the task entry field
- `insertTask()`: Adds a new task to the list
- `delete()`: Removes a specified task from the list

## License

This is a basic educational project and is free to use and modify.