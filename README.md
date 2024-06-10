# Python / Django setup
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

# Testing:
# run the following command in /stanley_ascend
# this will run this test file apis/tests.py
python manage.py test

# For manual testing: Create test objects with django shell
python manage.py shell
# Run the server
python manage.py runserver
Go to http://127.0.0.1:8000/
# execute desired API calls
use apis/tests.py for reference 

# Design decisions and areas for future improvement:
The majaority of the app logic currently lives in the view layer. This can be extracted to a service layer to keep the view layer thin and only responsible for formatting the data.

Customer model is a separate model to avoid tracking by name since there will likely be conflicts as names aren't unique. It will also allow us to attribute multiple policies to one
