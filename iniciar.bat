@echo off
set "venv_name=venv"

if not exist %venv_name% (
    python -m venv %venv_name%
    
    if %errorlevel% neq 0 (
        echo Failed to create virtual environment.
        exit /b %errorlevel%
    )

    call %venv_name%\Scripts\activate.bat

    if %errorlevel% neq 0 (
        echo Failed to activate virtual environment.
        exit /b %errorlevel%
    )

    pip install -r requirements.txt

    if %errorlevel% neq 0 (
        echo Failed to install dependencies.
        exit /b %errorlevel%
    )

    echo Virtual environment created and activated.
) else (
    call %venv_name%\Scripts\activate.bat
    echo Dependency virtual environment activated.
)