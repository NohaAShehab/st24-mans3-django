from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# views are functions


def hello(request): # this function should handle http request
    # this function must return with httpresponse
    # return "Hello World!"
    return HttpResponse("Hello World!")



def hi(request):
    return HttpResponse("<h1 style='color:red'>Hi</h1>")



students =[
    {"id":1, "name":"Omar", "grade":100},
    {"id": 2, "name": "Ahmed", "grade": 100},
    {"id": 3, "name": "Mohamed", "grade": 100},
    {"id": 4, "name": "Noha", "grade": 100}
]


def students_list(request):

    return HttpResponse(students)



def std_profile(request, id):
    # return HttpResponse(id)
    # print(id, type(id))
    # for std in students:
    #     if std['id'] == id:
    #         return HttpResponse(std['name'])
    # return HttpResponse("<h1 style='color:red'>Not Found</h1>")

    stds = list(filter(lambda std: std['id'] == id, students)) # list
    if stds:
        return HttpResponse(stds[0]['name'])
    return HttpResponse("<h1 style='color:red'>Not Found</h1>")