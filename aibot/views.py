from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from bot.main import chat

# Create your views here.

def index(request):

	q = ''
	if request.method=='POST' and request.is_ajax:
		response_data = {}
		q = request.POST.get('textfield')
		#querys = Query(data=q)
		#querys.save()

		response_data['req'] = q
		response_data['resp'] = chat(q)

		return HttpResponse(json.dumps(response_data), content_type = 'index')

	query_objs = Query.objects.all()

	return render(request, 'index.html',{'query_objs':query_objs})


