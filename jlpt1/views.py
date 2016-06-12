# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from jlpt1.form import ExamInfoForm
from django.shortcuts import redirect
import json
from jsonview.decorators import json_view
# Create your views here.

#@json_view
#def jsonResponse(request):
#    List = ['自强学堂', '渲染Json到模板']
#    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
#   # reesponse(json.dumps(name_dict), content_type='application/json')
#   #         'List': json.dumps(List),
#   #         'Dict': json.dumps(Dict)
#   #     })
#   return HttpResponse('listname':List)

@json_view
def my_view(request):
    return {
        'foo': 'bar',
    }

def home(request):
    if request.method == 'POST':
        
	form = ExamInfoForm(request.POST)
        if form.is_valid():
            exam_info = form.save()
            exam_info.save()
	return HttpResponse('Thank you')  
            #redirect('views.index') 

    else:


        form = ExamInfoForm()
    return render(request, 'index.html', {'form_info': form})


def recv_data(request):
        a=range(10) 
        jsonDate={'name':'lynn'}    
        j2=['s','s','s','s']
	#return HttpResponse(json.dumps(j2), content_type='application/json')
        return JsonResponse(a, safe=False)
