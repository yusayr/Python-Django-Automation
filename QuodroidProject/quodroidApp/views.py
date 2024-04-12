from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

@csrf_exempt
def execute_test(request):
    if request.method == 'POST' or request.method == 'GET':
        # Parse the JSON data from the request body
        data = {
            "tests": [
                {
                    "title": "Open google.com",
                    "steps": [
                        "Open Browser browser='chrome'",
                        "Go To url='https://google.com'"
                    ]
                }
            ]
        }

        # Iterate over the 'tests' list correctly
        for test in data['tests']:
            title = test.get("title","")
            robot_code = "***Settings***\n" +"Library\t" "SeleniumLibrary\n"+ "***Test Cases***\n" 
            robot_code += title + "\n"
            steps = test.get('steps',[])

            for step in steps:
                words = step.split()
                command = " ".join(words[:2])
                parameter = " ".join(words[2:])
                modified_step = "\t" + command + "\t" + parameter.replace("'", "") + "\n"
                robot_code += modified_step

            # Write the robot_code to a file
            with open('testfinal.robot', 'w') as file:
                file.write(robot_code)

            # Make a POST request to the same URL
            # response = requests.post('http://127.0.0.1:8000/testai/tests/v1/execute', data=data)

            # print(response.text)

            with open('testfinal.robot', 'w') as file:
                file.write(robot_code)

            # Execute the Robot Framework test
            os.system('robot testfinal.robot')

        return HttpResponse(robot_code, content_type='text/plain')
    else:
        return HttpResponse('Invalid Object', status=405, content_type='application/json')
















# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

# @csrf_exempt
# def execute_test(request):
#     if request.method == 'POST':
#         # Parse the JSON data from the request body
#         data = json.loads(request.body)
        
#         tests = data.get('tests', [])
        
#         robot_code = ""
#         for test in tests:
#             title = test.get("title","")
#             robot_code += title + "\n"
#             steps = test.get('steps',[])

#             for step in steps:
#                 words = step.split()
#                 command = " ".join(words[:2])
#                 parameter = " ".join(words[2:])
#                 modified_step = "\t" + command + "\t" + parameter + "\n"
#                 robot_code += modified_step
        
#         return HttpResponse(robot_code, content_type='application/json')
#     else:
#         return HttpResponse('Method not allowed', status=405, content_type='application/json')