
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.contrib.auth  import authenticate,  login, logout
from .utils import get_turn_info
from django.contrib import messages
from django.contrib.auth.models import User
import re
import random
from chat.models import   *
# Create your views here.
   
def peer1(request):
    # get numb turn info
    context = get_turn_info()

    return render(request, 'chat/peer1.html', context=context)

def ulogout(request):
    logout(request)
    # try:
    #     del request.session['Utype']
    # except KeyError:
    #     pass
    return redirect('/')
def home(request):
    # print(request)
    user = User.objects.get(username=request.user.username)
    is_vendor = Vender.objects.filter(user=user)
    if(is_vendor.count() == 0):
        is_vendor = False
    else:
        is_vendor = True
    print(is_vendor)
    # print('ok',User.objects.get(username=request.user.username))

    if request.method == "POST"and "btn-joinroom" in request.POST:
        # print("btn-joinroom")
        id = random.randint(111111,999999)
        return redirect('/?id='+str(id))
    if request.method == "POST"and "btn-roomid" in request.POST:
        # print("btn-roomid")
        id = request.POST["meetingid"]
        return redirect('/?id='+id)
    context = get_turn_info()
    context['vender'] = is_vendor 
    print(context)
    return render(request, 'chat/singup.html', context=context)

def singup(request):
    # get numb turn info

    if request.method == "POST":
        # Get the post parameters
        username = request.POST['uname']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        # email = 'emai@gmail.com'
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        checkemail = User.objects.filter(email=email)
        checkuser = User.objects.filter(username=username)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if len(checkemail)>0:
            messages.error(request, "Email is already exits.")
            return render(request, 'chat/singup.html')
        if len(checkuser)>0:
            messages.error(request, "User Name is already exits.")
            return render(request, 'chat/singup.html')
        
        muser = User.objects.all()
        for itme in muser:
            if(itme.email==email):
                messages.error(request, "Email is already exits.")
                return render(request, 'chat/singup.html')
                # break

        # try:
        #     uemail = User.objects.get(email=request.POST['email'])

        # except User.DoesNotExist as e:
        #     messages.error(request, "Email is already exits.")
            

        if len(username) > 10:
            messages.error(request, " Your user name must be under 10 characters")
            return render(request, 'chat/singup.html')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return render(request, 'chat/singup.html')
        if password != cpassword:
            messages.error(request, " Passwords do not match")
            return render(request, 'chat/singup.html')
        
        if(re.search(regex,email)):   
           print("Valid Email")   
        else:   
           messages.error(request, " invalid email")
           return render(request, 'chat/singup.html') 
         
        # Create the user
        user = User.objects.create_user(username, email, password)
        print(user)
        # user_type = request.POST['user_type']
        # if user_type == "Company":
        #     company_name =request.POST['companyName']
        #     userType = Extend(user_type = user_type , user=user, company_name=company_name)
        # else:
        #     userType = Extend(user_type = user_type , user=user)
        # userType.save()
        user.save()
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        
        messages.success(request, "You have succesfully Registerd.")
        return redirect('/')

    context = get_turn_info()

    return render(request, 'chat/singup.html', context=context)

def peer2(request):
    # get numb turn info
    context = get_turn_info()

    return render(request, 'chat/peer2.html', context=context)

def peer(request):


    if request.method == "POST":
    # Get the post parameters
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)  
        if user is not None:  
            # print(user) 
            login(request  , user) 
            
            # print(is_vendor[0].is_vendor)
            return redirect('/home')
               
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('/')
    
    # get numb turn info
    context = get_turn_info()
    # context+= user
    print('context: ', context)

    return render(request, 'chat/peer.html', context=context)
def peer11(request,id):
    # get numb turn info
    # print(id)
    
    context = get_turn_info()
    print('context: ', context)

    return render(request, 'chat/peer.html', context=context)
def peer12(request):
    # get numb turn info
    # print(id)
    context = get_turn_info()
    print('context: ', context)
 
    return render(request, 'chat/peer.html', context=context)