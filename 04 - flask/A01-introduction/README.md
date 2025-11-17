# Python Flask introduction
Flask first use

<br />
<br />

## Commands to begin
```bash
1. python -m venv .venv
```
```bash
2. source .venv/Scripts/activate
```
```bash
3. pip install flask
```
```diff
+ 4. Create app.py with code inside it

 from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
```
```bash
5. python app.py
```

<br />

## Flask useful commands
```bash
pip freeze - to lists all python packages installed in the current environment with their exact versions
```
```bash
pip freeze > requirments.txt - to lists all python packages currently installed in your active virtual environment
```
```bash
pip install -r requirments.txt - to recreates the environment from the requirements file
```
```bash
deactivate - to leave virtual environment
```

## Information

**Why is virtual environment (venv) good?**
<br />
<br />
It keeps dependencies separate from other projects and the system python, making it easier to manage packages, avoid version conflicts, and reproduce the environment on other machines

<br />

`python -m venv .venv - this make virtual environment (.venv)`
<br />

`source .venv/Scripts/activate - this activate virtual environment`
<br />

`python app.py - this run app.py file`
<br />

<br />

**On app.py**

`host='0.0.0.0', port=5555, debug=True`
* all optional
* host - tells flask to listen on all network interfaces, so the app is accessible from other devices on the same network, not just localhost
* port - sets the network port the flask app will run on. Default is 5000
* debug - automatically reloads the server when you change code, shows detailed error messages in the browser if something goes wrong
<br />

``` diff
- DO NOT USE DEBUG TRUE IN PRODUCTION BECAUSE IT CAN EXPOSE SENSITIVE INFORMATION -
```
