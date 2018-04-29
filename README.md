# READ ME


## About
Personal Project
This project will create single files for consolidacion per leader for the master file. The goal is that the configuration of the files is always the same and any change can be reflected in all files, so I don´t have to change them one by one everytime a new feature is available.

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

To install new python packages:

```
pipenv install <packageName>
```
