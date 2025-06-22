@echo off
echo Starting Movie Recommender Setup...
echo ================================

if not exist "venv" (
    echo Creating virtual environment...
    "C:\Users\souri\AppData\Local\Programs\Python\Python313\python.exe" -m venv venv
    echo Virtual environment created!
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Checking and installing requirements...
pip install -r requirements.txt

cls
echo ================================
echo Movie Recommender is ready!
echo ================================
echo.
echo Starting the server...
echo The website will be available at: http://127.0.0.1:5000
echo.
echo Press Ctrl+C to stop the server when you're done
echo ================================
echo.

"C:\Users\souri\AppData\Local\Programs\Python\Python313\python.exe" app.py

deactivate
