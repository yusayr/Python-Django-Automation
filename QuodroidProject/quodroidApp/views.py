from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def execute_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tests = data.get('tests', [])
            if tests:
                first_test = tests[0]
                title = first_test.get('title', '')
                steps = first_test.get('steps', [])
                # Return a JSON response
                response_data = {
                    'message': 'Received data successfully',
                    'title': title,
                    'steps': steps
                }
                return JsonResponse(response_data, content_type='application/json',status=201)
            else:
                return JsonResponse({'error': 'No tests found'}, status=400)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)















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