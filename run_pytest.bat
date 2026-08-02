@echo off
REM Run pytest through the virtualenv Python interpreter to avoid Device Guard blocking pytest.exe
"%~dp0\.venv\Scripts\python.exe" -m pytest %*
