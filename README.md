An automation project using Django and Robot Framework for python.
In this project, a JSON file containing a set of commands is parsed as a POST request, upon which the commands are executed. The Robot Framework is an automation testing tool in which we can define a set of tasks to be defined, and test whether the tasks have been successfully performed.
In the 'View' component, I have defined the API endpoint which accepts the POST request and implemented the logic for extracting the commands from the incoming JSON object. Upon extraction, these commands are saved to a new robot file 'testfinal.robot'. I used the OS library which enabled us to run the file on its own. All these tasks are executed upon the API call. I tried making the POST request within Django however the response time was high, hence I used POSTMAN for API calls.
This project was completed as a given task within 7 days. It helped me learn about task automation and displays my adaptability to new technologies. 

To run this project
1] 'python manage.py runserver'(You may need to install Django)
2] Send a POST request using POSTMAN API or CURL to http://127.0.0.1:8000/testai/tests/v1/execute
