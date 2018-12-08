from django.shortcuts import render, redirect
import random
from time import gmtime, strftime 

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
    return render(request, 'myapp/index.html')

def process_money(request):
    if request.GET['which_form'] == "farm":
        num = random.randint(10, 20)
        request.session['gold'] += num
        message = "You made " + str(num) + " gold at the farm on " + strftime("%B %d, %Y at %H:%M:%S")
        request.session['log'].insert(0, message)
    elif request.GET['which_form'] == "cave":
        num = random.randint(5, 10)
        request.session['gold'] += num
        message = "You found " + str(num) + " gold in the cave on " + strftime("%B %d, %Y at %H:%M:%S")
        request.session['log'].insert(0, message)
    elif request.GET['which_form'] == "house":
        num = random.randint(2, 5)
        request.session['gold'] += num
        message = "You found " + str(num) + " gold between your couch cushions on " + strftime("%B %d, %Y at %H:%M:%S")
        request.session['log'].insert(0, message)
    elif request.GET['which_form'] == "casino":
        num = random.randint(-50, 50)
        request.session['gold'] += num
        if num < 0:
            message = "You lost " + str(num) + " gold at the casino on " + strftime("%B %d, %Y at %H:%M:%S")
        else:
            message = "You won " + str(num) + " gold at the casino on " + strftime("%B %d, %Y at %H:%M:%S")
        request.session['log'].insert(0, message)
    print(request.session['log'])
    return redirect('/')

def start_over(request):
    request.session.clear()
    return redirect('/')