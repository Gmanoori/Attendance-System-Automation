@echo off
set REPO_OWNER=Gmanoori
set REPO_NAME=Attendance-System-Automation
set ISSUE_NUMBER=3
set GITHUB_TOKEN=<your_github_token>
set COMMENT_BODY=/login

curl -X POST https://api.github.com/repos/%REPO_OWNER%/%REPO_NAME%/issues/%ISSUE_NUMBER%/comments ^
-H "Authorization: token %GITHUB_TOKEN%" ^
-H "Content-Type: application/json" ^
-d "{\"body\":\"%COMMENT_BODY%\"}"
