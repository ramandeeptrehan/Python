# Cohort (August 2023)
pip install -r requirements.txt

## We will use Python and FastAPI framework

## For a Mac user, Python install packages are located locally at:
/Users/<userName>/Library/Python/3.9/lib/python/site-packages

## To run the server
python3 -m uvicorn main:app --reload

NOTES:
The command uvicorn main:app refers to:

main: the file main.py (the Python "module").
app: the object created inside of main.py with the line app = FastAPI().
--reload: make the server restart after code changes. Only do this for development.