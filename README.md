# VineyardApp

## This app was created as a part of the Vineyard Pest Deterrence System MQP completed in 2021 by Kenneth Desrosiers and Sophie Antoniou.

### How to get started (make sure you already have Python installed!!):

#### note: make sure to download PyCharm if you don't already have it. A free Community version can be found here: https://www.jetbrains.com/pycharm/

#### 1. clone the repository
#### 2. in the terminal or command line, navigate to the 'src' folder of the project
#### note: it's best to perform the following after setting up a virtual environment. This will contain all of the packages within the project. Not mandatory but recommended. More info can be found here: https://docs.python.org/3/tutorial/venv.html
#### 3. run `pip install -r requirements.txt` to install the required packages
#### 4. navigate to the 'src/res' folder
#### 5. run `pyrcc5 -o resources.py resources.qrc` to build the dependencies for the resources (sounds, images)

#### note: You will also need to create API keys to use fetch the current weather. Also needed is a MongoDB free cluster to store database detection information. These will need to be saved a file called 'api_keys.py', which is to be placed inside the 'src' folder. the format of this file is as follows:
ipAPIKey = "{IP api key}"

weatherAPIKey = "{weather api key}"

mongodb = "{Database access string}"

#### good luck :)
