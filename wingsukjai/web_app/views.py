from django.shortcuts import render
from web_app.forms import NewRunnerForm
from web_app.models import runner

# Create your views here.

def index(request):
    return render(request,'web_app/index.html')

def info(request):
    return render(request,'web_app/info.html')

def register(request):
    form = NewRunnerForm()

    if request.method == "POST":
        form = NewRunnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'web_app/register.html',{'form':form})

def thanku(request):
    return render(request,'web_app/thanku.html')

def check(request):

    if request.method == "POST":
        number = request.POST['your_number']
        checking_runner = runner.objects.filter(mobile = number)
        runner_dict = {'checking':checking_runner}
        return render(request,'web_app/check.html', context = runner_dict)

    else:
        print("ERROR FORM INVALID")

    return render(request,'web_app/check.html')
