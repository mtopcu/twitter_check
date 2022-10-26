## Features

You can get all your following who doesn't follow you back on Twitter.

In this project, I wanted to work with an API having a pagination feature. To make api requests, I used python request library, and to get all the API responses in a proper way, I used python dataclass library for API testing.

PS: This project will not be working for huge accounts like including thousands of following-followers on Twitter. It is a simple trial project to get more knowledge about JSON, dataclass, API resquest-response in Python.

### Install

Before installing the project, you should get a Bearer token from your Twitter Development account and put it in the config file in the project. Then just clone the project, go to the directory of the project and run the below commands.


```sh
- python3 -m venv env
- source env/bin/activate
- pip install -r requirements.txt
- python twitter_check
```