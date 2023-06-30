from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import CustomUser, Admin_mine, Admin_mine_Feedback,Admine_mine_Notification
from django.contrib import messages


def super_admin(request):
    return render(request, 'dashboard_admin/index.html')


@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_student')

        else:
            user = CustomUser(first_name=first_name, last_name=last_name, email=email, profile_pic=profile_pic,
                              username=username, user_type=2)
            user.set_password(password)
            user.save()

            staff = Admin_mine(
                admin=user,
                address=address,
                gender=gender
            )
            staff.save()
            messages.success(request, 'aha zur')
            return redirect('add_staff')
    return render(request, 'help_admin/add_staff.html')


@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Admin_mine.objects.all()
    context = {
        'staff': staff
    }
    return render(request, 'help_admin/view_staff.html', context)


@login_required(login_url='/')
def EDIT_STAFF(request, id):
    staff = Admin_mine.objects.get(id=id)
    context = {
        'staff': staff
    }

    return render(request, 'help_admin/edit_staff.html', context)


@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic

        user.save()

        staff = Admin_mine.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()
        messages.success(request, 'Staff i Successfully Update')
        return redirect('view_staff')

    return render(request, 'help_admin/edit_staff.html')


@login_required(login_url='/')
def DELETE_STAFF(request, admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request, "oka zo'r uchirdiz a! mazzami ?")
    return redirect('view_staff')


@login_required(login_url='/')
def STAFF_FEEDBACK(request):
    feedback = Admin_mine_Feedback.objects.all()
    feedback_history = Admin_mine_Feedback.objects.all().order_by('-id')[0:5]
    context = {
        'feedback': feedback,
        'feedback_history': feedback_history
    }
    return render(request, 'help_admin/staff_feedback.html', context)


@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_id')
        feedback = Admin_mine_Feedback.objects.get(id=feedback_id)
        feedback.feedback_replay = feedback_reply
        feedback.status = 1
        feedback.save()

        return redirect('staff_feedback_reply')


@login_required(login_url='/')
def STAFF_SEND_NOTIFICATION(request):
    staff = Admin_mine.objects.all()
    see_notification = Admine_mine_Notification.objects.all().order_by('-id')[0:5]
    context = {
        'staff': staff,
        'see_notification': see_notification
    }
    return render(request, 'help_admin/staff_notification.html', context)


@login_required(login_url='/')
def SAVE_STAFF_NOTIFICATION(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Admin_mine.objects.get(admin=staff_id)
        notification = Admine_mine_Notification(
            staff_id=staff,
            message=message,
        )
        notification.save()
        messages.success(request, "zo'r yuborildi-da")
    return redirect('staff_send_notification')