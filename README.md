# IFSC REST API

This API runs on Python 3.6. Make sure you have Python 3.6 and pip installed.


# Production URL

The API is hosted on Heroku:

		https://fyle-bank-api.herokuapp.com/api/v1/banks/
    
# URLs and Features

The API has 3 features:

1. Get all the banks
            
            URL: https://fyle-bank-api.herokuapp.com/api/v1/banks/
    
    This will return a paginated JSON Data of Banks all over India.

2. Get Bank details using IFSC Code
      
            URL: https://fyle-bank-api.herokuapp.com/api/v1/banks/<IFSC Code>/
            
            example: https://fyle-bank-api.herokuapp.com/api/v1/banks/SBIN0000139/
            
    will return


                {
                    "id": 81725,
                    "ifsc": "SBIN0000139",
                    "bank_id": 1,
                    "branch": "NAINI",
                    "address": "MIRZAPUR ROAD, NAINI, ALLAHABAD, UTTAR PRADESH, PIN 211008",
                    "city": "ALLAHABAD",
                    "district": "ALLAHABAD",
                    "state": "UTTAR PRADESH",
                    "bank_name": "STATE BANK OF INDIA"
                }

3. Get Branches using city name and bank name
    
            URL: https://fyle-bank-api.herokuapp.com/api/v1/branches/?city=<city name>&bank_name=<bank name>
            
            example: https://fyle-bank-api.herokuapp.com/api/v1/branches/?city=allahabad&bank_name=state bank of india
            
will return a list of JSON Objects with all the branches in the city


# Clone the Repository

Open the terminal and run the command:

		git clone https://github.com/Shwetabhk/IFSC_REST_API.git

# Create a virtual environment

open your working directory in the terminal and run the following commands:

		pip install virtualenv

		python -m virtualenv Bank

		source sirius/bin/activate


# Install the requirements

Open the cloned folder in the terminal(virtual environment) and run the following commands:

		pip install -r requirements.txt



# Create the config file:

The Config file is where all the secrets related to this API go, eg: credentials, Database details, API keys, file_paths, etc.

Create a file config.py in the base directory which contains manage.py and add following code:

          class Secrets:
            AWS_ACCESS_KEY_ID = "Your AWS KEY"
            AWS_SECRET_ACCESS_KEY = "Your AWS Secret Access Key"


# Migrating the database

Run the following commands to make changes in the database:

		python manage.py makemigrations

		python manage.py migrate


# Run the server

		python manage.py runserver




	
