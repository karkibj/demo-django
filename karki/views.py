from django.http import HttpResponse
from django.shortcuts import render

def response(request):
    return HttpResponse("Hey welcome to the page")

def gallery(request):
    # datafile={
    #     'jerseynumber':[10,11,7]

    # }

    return render(request,"index.html")
def courses(request):
    return HttpResponse("AVailable  courses")

def contact(request):
    try:
        if request.method=='GET':
            value=0
            n1=int(request.GET.get('num1'))
            n2=int(request.GET.get('num2'))
            value=(n1+n2)
            
    except:
       pass


    return render(request,"contact.html",{'output':value})

def courseDetails(request,courseid):
    return HttpResponse(courseid)


def Homepage(request):
    #creating dictinoary in order to pass the data to html page
    # data={
    #     'title':'PythonDeveloper',
    #     'about':'Hey this is karkibj the most creative learner',
    #     'skills': ['communication skill','leadership skill','Programming skills'],

    #     'friends':[{'name':'subin pradhan','contact':'987654321','relationstatus':'Pidit'},
    #                {'name':'Nischal sitikhu', 'contact':'981234567','relationstatus':'Hariyali'}
                  
                  
    #             ]


    # }



    return render(request,"index.html",)