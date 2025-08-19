## Attendance System Automation with GitHub Actions
This repository contains an automated attendance tracking system implemented using GitHub Actions. The system logs user login and logout times as markdown entries in a version-controlled attendance file, enabling simple yet effective attendance tracking directly within a GitHub repository.

## Features
- Automated recording of login and logout timestamps for users.

- Stores attendance data as markdown tables (attendance.md), easily readable and maintainable.

- Uses GitHub Actions workflows to automate updates on each login/logout event.

- Calculates and records work hours based on login/logout times.

- Maintains a clean history of attendance records in the repository with automated commits and pushes.

- Easily extensible and customizable for different attendance tracking needs.

## How It Works
- User login triggers a GitHub Actions workflow that records the login timestamp along with the user’s name and current date.

- User logout triggers the workflow to read the stored login timestamp, calculate work hours (difference between logout and login), and append the full attendance entry to attendance.md.

- The system manages a temporary file in the repository to persist login time between runs.

- Attendance records are committed and pushed to the repository automatically, keeping all history versioned and accessible.

## Getting Started
- To use or customize this attendance system:

- Clone the repository to your GitHub account.

- Configure the workflow triggers and commands (login and logout) according to your usage environment.

- Adjust the time format, user identification method, or markdown structure in the workflows as needed.

- Use the provided scripts and workflow YAML files in .github/workflows/ for automation.

## Technologies Used
- GitHub Actions (workflows and jobs)

- Bash scripting for automation and time calculations

- Git for version control and automated commits

- Markdown for attendance record formatting

## Example Attendance Entry
|User	|Date	|Log-In |Time	|Log-Out |Time	|Work Hours|
|-----|------|------|------|-------|-------|---------|
|JohnDoe	|2025-08-19|	09:00|	17:00|	08:00|

## Contributing
- Contributions and improvements are welcome! Feel free to open issues or pull requests to enhance the system.

**Author**
Ganesh
