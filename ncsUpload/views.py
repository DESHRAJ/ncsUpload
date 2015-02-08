from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import *
from django.conf import settings
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.template.loader import get_template
from django.template import Context
from ncsUpload.settings import * 
import csv
import os

def home(request):
	''' This view is describes the working of the whole script for
	uploading the file and then tranferring it to the backend and 
	finally working with teh file handling in python that changes 
	the content of csv file into the sql queries. '''
	if request.POST:
		f = request.FILES["files"]
		if f.name[-4:] != ".csv":
			return HttpResponse("<h2>The file format is not correct </h2>")
		else:
			a = ""
			doc = open(os.path.join(PROJECT_ROOT, "docs/"+f.name), 'wb+')
			for chunk in f.chunks():
				doc.write(chunk)
			doc.close()
			a = a + "INSERT INTO `questions` (`id`, `question`, `a`, `b`, `c`, `d`, `ans`) VALUES" + "\n"
			f = open(os.path.join(PROJECT_ROOT, "docs/"+f.name))
			i = 1
			r = csv.reader(f)
			for row in r :
				a= a +"("+str(i)+","+"'"+str(row[0])+"'"+","+"'"+str(row[1])+"'"+","+"'"+str(row[2])+"'"+","+"'"+str(row[3])+"'"+","+"'"+str(row[4])+"'"+","+"'"+str(row[5])+"'"+"),"+"\n"
				i = i+1
			return HttpResponse(a[:-2])
	return render_to_response('index.html',context_instance = RequestContext(request))