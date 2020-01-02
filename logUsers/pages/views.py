from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import PersonLog
from django.contrib.auth.decorators import login_required, user_passes_test
import datetime
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            raw_pass = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_pass)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'pages/signup.html', {'form': form})

@login_required
def home(request):
    #LOG TIME
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated == True:
            time = datetime.datetime.now()
            # print("TIMMMMMMEEEEEEEEEEEEEEEEEEEE")
            # print(time)
            #time = timezone.now()
            objects = PersonLog.objects.filter(personId=user.id)
            if (objects.count() > 0):
                #lastObj = objects.latest('timeIn')
                lastObj = objects.last()
                print("1TIME IN ")
                print(lastObj.timeIn)
                print("1TIME OUT ")
                print(lastObj.timeOut)
                if (lastObj.timeOut is None):
                    print("2TIME IN ")
                    print(lastObj.timeIn)
                    print("2TIME OUT ")
                    print(lastObj.timeOut)

                    lastObj.timeOut = time

                    print("3TIME IN ")
                    print(lastObj.timeIn)
                    print("3TIME OUT ")
                    print(lastObj.timeOut)

                    #lastObj.save()     <-- this changed timeIn to match timeOUt
                    lastObj.save(update_fields=['timeOut'])
                    
                    print("4TIME IN ")
                    print(lastObj.timeIn)
                    print("4TIME OUT ")
                    print(lastObj.timeOut)
                else:
                    # personObj = User.objects.get(id=user.id)
                    # p = PersonLog(personId=personObj)
                    # print("TIMMMMMMEEEEEEEEEEEEEEEEEE")
                    # print(time)

                    p = PersonLog(timeIn=time, personId=user.id)

                    print("ATIME IN ")
                    print(p.timeIn)
                    print("ATIME OUT ")
                    print(p.timeOut)

                    p.save()

                    print("BTIME IN ")
                    print(p.timeIn)
                    print("BTIME OUT ")
                    print(p.timeOut)

                    x = PersonLog.objects.filter(personId=user.id).last()

                    print("CTIME IN ")
                    print(x.timeIn)
                    print("CTIME OUT ")
                    print(x.timeOut)
            else:
                # personObj = Person.objects.get(id=user.id)
                # p = PersonLog(timeIn=time, personId=user.id)
                personObj = User.objects.get(id=user.id)
                p = PersonLog(personId=personObj.id)
                p.save()
            return redirect('home')
    #HOME
    context = {
        "person": User.objects.get(id=request.user.id),
        #get_object_or_404(Person, personId=request.user.id),
        "log": PersonLog.objects.filter(personId=request.user.id)
    }
    return render(request, "pages/home.html", context)

@login_required
def view_profile(request):
    return render(request, "pages/profile.html", {'user': request.user})

@login_required
def edit_profile(request):
    user = request.user
    form = EditProfileForm(
        data=request.POST,
        user=request.user,
        instance=request.user,
    )

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('view-profile')
        else:
            form = EditProfileForm(
                data=request.POST,
                user=request.user,
                instance=request.user,
            )
    return render(request, 'pages/edit_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('view-profile')
        else:
            return redirect('change-password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pages/change_password.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def people_list(request):
    queryset = User.objects.all()
    return render(request, "pages/people_list.html", {"people_list": queryset})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def person_log(request, id=id):
    context = {
        "person": User.objects.get(id=id),
        "logs": PersonLog.objects.filter(id=id)
    }
    return render(request, "pages/person_log.html", context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def all_logs(request):
    context = {
        "logs": PersonLog.objects.all(),
        "people": User.objects.all(),
    }
    return render(request, "pages/all_logs.html", context)
