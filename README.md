# Log Storage

[![CircleCI](https://circleci.com/gh/Virtualstock/log_storage.svg?style=svg)](https://circleci.com/gh/Virtualstock/log_storage)

A django installable app that can be used as log handler to store messages 
with a database record and optional file storage.

## How to install

Add this package as requirement to your django app requirements.txt

```
# requirements.txt
log_storage==0.2
```

Add this app to your **INSTALLED_APPS** in your **settings.py**

```
# settings.py
INSTALLED_APPS = (
    'log_storage',
)
```

## Development


### How to install

Clone the project

```
git clone git@github.com:Virtualstock/log_storage.git
```

Install it

```
make setup
```

### How to run tests

```
make test
```

