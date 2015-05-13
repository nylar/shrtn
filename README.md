# Shrtn

[![Build Status](https://travis-ci.org/nylar/shrtn.svg?branch=master)](https://travis-ci.org/nylar/shrtn)
[![Coverage Status](https://coveralls.io/repos/nylar/shrtn/badge.svg?branch=master)](https://coveralls.io/r/nylar/shrtn?branch=master)
[![License](https://img.shields.io/badge/license-CC0-blue.svg)](LICENSE)

A Django link shortener.

## Installation

Grab the code.
```shell
git clone git@github.com:nylar/shrtn.git
cd shrtn
```

Install the requirements.
```shell
pip install -r requirements.txt
```

Setup the database.
```shell
python manage.py syncdb --noinput
python manage.py migrate --noinput
```

To run the local server
```shell
python manage.py runserver
```

To run the tests (with code coverage).
```shell
py.test --cov links --cov-report term-missing
```