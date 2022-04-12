from django.shortcuts import render
import requests
from subprocess import run,PIPE
import sys
import re
import subprocess
def button(request):
    return render(request,'home.html')
    
def output(request):
    
    data=requests.get("https://www.google.com")
    print(data.text)
    data=data.text
    return render(request,'home.html',{'data':data})

def external(request):
    inp=request.POST.get('param')
    out=run([sys.executable,'F:\\FastSearch_Final\\fastS.py',inp],shell=False,stdout=subprocess.PIPE)
    #fout=strip_ansi(out)
    #op=externalOP(out)
    print(out)

    return render(request,'op.html',{'data1':out.stdout})

