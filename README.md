# READ ME

## Requirements

### [Pip](https://pip.pypa.io/en/stable/installing/)


## Set up

After cloning your app, run the following commands:

```
heroku git:remote -a <heroku-app-name>
pip install pipenv
```

Create virtual env (only first time):

```
python3 -m venv venv
```

Run virtual env:

```
source venv/bin/activate
```

Install dependencies:

```
pipenv install
```

Quit virtual env:

```
deactivate
```

