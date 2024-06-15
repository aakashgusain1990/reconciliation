# IDENTITY RECONCILIATION
## Setting up python environment and installing dependencies
```py
python -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```


## Run Development Server
```py
python3 run.py
```
Flask server will be up and running at http://127.0.0.1:5000/.

## Build and publish
1. Make and commit changes to main branch.
2. Github workflow will auto build and publish the image to docker hub.

## API Endpoint for Prod Server
API Endpoint: https://reconciliation.onrender.com/identify.

Request Body:
```sh
{
"email":"george@hillvalley.edu",
"phoneNumber": "717171"
}
```
