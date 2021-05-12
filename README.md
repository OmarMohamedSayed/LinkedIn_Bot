![LinkedIn-Bot](https://i.imgur.com/od6HpD8.png)
[![Badges](https://img.shields.io/badge/language-Python-blue.svg)]
[![Badges](https://img.shields.io/badge/license-GPL-lightgreen.svg)]
[![Badges](https://img.shields.io/badge/version-2.1-lightgrey.svg)]
# LinkedIn_Bot
Create LinkedIn Bot to congrats people automatically,
To increasing visibility of your profile by congrats others Users 
This Bot under the name of 'I will never forget to congratulate you ' .

## Features
* Login to linkedIn
* Click to Congrats button and send congrats message to all users once

## Requirements
Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow."
* Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
	* On MacOS if you have [HomeBrew](https://brew.sh) installed you can use `brew install chromedriver`
* Firefox:	https://github.com/mozilla/geckodriver/releases
	* On MacOS if you have [HomeBrew](https://brew.sh) installed you can use `brew install geckodriver`

## Configuration and Running
Install selenium : https://selenium-python.readthedocs.io/installation.html
To run the bot go into the directory where the bot is stored and type `python Index.py`
Before you run the bot, edit the configuration portion of the script. This will include your account login information (email, password) and Driver path

### edit the a `conf.py` file for the config file to fetch from
```python
  DRIVER_PATH='EnterYourPath/geckodriver'
  EMAIL = "Your Email"
  PASSWORD = "Your Password"
```
## Output
Searching for the Login btn
Searching for the password btn
Searching for the submit
loggin success
Notifications
length of users
Success congrats people

## suggestions
If you have any suggestions open an issue and I or a contributor will gladly do our best to implement it if it aligns with the goals of the project!

