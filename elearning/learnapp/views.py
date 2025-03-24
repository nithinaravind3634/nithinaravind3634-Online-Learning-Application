from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    return render(request, "index.html")


def loginindex(request):
    return render(request, "loginindex.html")



def teacherlogin(request):
    if request.method == "POST":
        teacherusername = request.POST.get("teacherusername")
        teacherpassword = request.POST.get("teacherpassword")
        
        data = teachermodel.objects.all()
        for i in data:
            if i.teacherusername == teacherusername and i.teacherpassword == teacherpassword:
                request.session["teacher_id"] = i.id
                request.session["teacher_username"] = i.teacherusername
                request.session["teacher_email"] = i.teacheremail
                request.session["teacher_phone"] = i.teacherphone
                request.session["is_authenticated"] = True  

                return render(request, "teacherindex.html", {
                    "teacherusername": i.teacherusername,
                    "teacheremail": i.teacheremail,
                    "teacherphone": i.teacherphone,
                    "id": i.id
                })
        
        return render(request, "teacherlogin.html",{"alert_message": "User not found"})
    return render(request, "teacherlogin.html")





def studentlogin(request):
    if request.method == "POST":
        studentusername = request.POST.get("studentusername")
        studentpassword = request.POST.get("studentpassword")
        data = studentmodel.objects.all()
        for i in data:
            if i.studentusername == studentusername and i.studentpassword == studentpassword:
                request.session["student_id"] = i.id
                request.session["student_username"] = i.studentusername
                request.session["student_email"] = i.studentemail
                request.session["student_phone"] = i.studentphone
                request.session["is_authenticated"] = True  
                return render(request, "studentindex.html", {
                    "studentusername": i.studentusername,
                    "studentemail": i.studentemail,
                    "studentphone": i.studentphone,
                    "id": i.id
                })
        
        return render(request, "studentlogin.html",{"alert_message": "User not found"})
    return render(request, "studentlogin.html")





def studentregister(request):
    if request.method == "POST":
        f = studentform(request.POST)
        if f.is_valid():
            studentusername = f.cleaned_data["studentusername"]
            studentemail = f.cleaned_data["studentemail"]
            studentphone = f.cleaned_data["studentphone"]
            studentpassword = f.cleaned_data["studentpassword"]
            studentcpassword = f.cleaned_data["studentcpassword"]
            if studentpassword == studentcpassword:
                m = studentmodel(studentusername=studentusername, studentemail=studentemail, studentphone=studentphone, studentpassword=studentpassword)
                m.save()
                return redirect(studentlogin)
            else:
                return render(request, "studentregister.html",{"alert_message": "Password and Confirm Password do not match"})
        else:
            return render(request, "studentregister.html",{"alert_message": "Enter Valid data"})
    return render(request, "studentregister.html")





def teacherregister(request):
    if request.method == "POST":
        f = teacherform(request.POST)
        if f.is_valid():
            teacherusername = f.cleaned_data["teacherusername"]
            teacheremail = f.cleaned_data["teacheremail"]
            teacherphone = f.cleaned_data["teacherphone"]
            teacherpassword = f.cleaned_data["teacherpassword"]
            teachercpassword = f.cleaned_data["teachercpassword"]

            # Check if username already exists
            if teachermodel.objects.filter(teacherusername=teacherusername).exists():
                return render(request, "teacherregister.html",{"alert_message": "Username Already Exists"})

            if teacherpassword == teachercpassword:
                m = teachermodel(
                    teacherusername=teacherusername,
                    teacheremail=teacheremail,
                    teacherphone=teacherphone,
                    teacherpassword=teacherpassword
                )
                m.save()
                return redirect(teacherlogin)
            else:
                return render(request, "teacherregister.html",{"alert_message": "Password and Confirm Password do not match"})
        else:
            return render(request, "teacherregister.html",{"alert_message": "Enter Valid data"})
    return render(request, "teacherregister.html")





def postvideo(request, username):
    if not request.session.get("is_authenticated"):
        return redirect(loginindex)
    if request.method == 'POST':
        teachername = request.POST.get('teachername')
        videotopic = request.POST.get('videotopic')
        videodescription = request.POST.get('videodescription')
        videoupload = request.FILES.get('videoupload')

        # Save the posted job in the database
        postvideo = postvideomodel(
            teachername=teachername,
            videotopic=videotopic,
            videodescription=videodescription,
            videoupload=videoupload
        )
        postvideo.save()
        return render(request, "postvideo.html",{"alert_message": "Posted successfully","username":username})
    return render(request, "postvideo.html",{"username":username})





def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect(loginindex)


def postfile(request, username):
    if not request.session.get("is_authenticated"):
        return redirect(loginindex)
    if request.method == 'POST':
        teachername = request.POST.get('teachername')
        filetopic = request.POST.get('filetopic')
        filedescription = request.POST.get('filedescription')
        fileupload = request.FILES.get('fileupload')
        filethumbnail=request.FILES.get('filethumbnail')

        # Save the posted job in the database
        postfile = postfilemodel(
            teachername=teachername,
            filetopic=filetopic,
            filedescription=filedescription,
            fileupload=fileupload,
            filethumbnail=filethumbnail

        )
        postfile.save()
        return render(request, "postfile.html",{"alert_message": "Posted successfully","username":username})
    return render(request, "postfile.html",{"username":username})


def uiux(request):
    if not request.session.get("is_authenticated"):
        return redirect(loginindex)
    x=postvideomodel.objects.filter(videotopic="ui/ux")
    y=postfilemodel.objects.filter(filetopic="ui/ux")


    return render(request,"uiux.html",{"x":x,"y":y})


def uiux(request):
    if not request.session.get("is_authenticated"):
        return redirect(loginindex)
    x=postvideomodel.objects.filter(videotopic="ui/ux")
    y=postfilemodel.objects.filter(filetopic="ui/ux")


    return render(request,"uiux.html",{"x":x,"y":y})


def python(request):
    if not request.session.get("is_authenticated"):
        return redirect(loginindex)
    x=postvideomodel.objects.filter(videotopic="python")
    y=postfilemodel.objects.filter(filetopic="python")


    return render(request,"python.html",{"x":x,"y":y})


def angular(request):
    if not request.session.get("is_authenticated"):
        return redirect(loginindex)
    x=postvideomodel.objects.filter(videotopic="angular")
    y=postfilemodel.objects.filter(filetopic="angular")


    return render(request,"angular.html",{"x":x,"y":y})


def reactjs(request):
    if not request.session.get("is_authenticated"):
        return redirect(loginindex)
    x=postvideomodel.objects.filter(videotopic="reactjs")
    y=postfilemodel.objects.filter(filetopic="reactjs")


    return render(request,"reactjs.html",{"x":x,"y":y})


def nodejs(request):
    if not request.session.get("is_authenticated"):
        return redirect(loginindex)
    x=postvideomodel.objects.filter(videotopic="nodejs")
    y=postfilemodel.objects.filter(filetopic="nodejs")


    return render(request,"nodejs.html",{"x":x,"y":y})


def django(request):
    if not request.session.get("is_authenticated"):
        return redirect(loginindex)
    x=postvideomodel.objects.filter(videotopic="django")
    y=postfilemodel.objects.filter(filetopic="django")


    return render(request,"django.html",{"x":x,"y":y})







def postresponse(request,teachername,videotopic,videodescription):
    if request.method == 'POST':
        username = request.POST.get('username')
        response = request.POST.get('response')
        teachername = request.POST.get('teachername')
        videotopic = request.POST.get('videotopic')
        videodescription = request.POST.get('videodescription')

        # Save the posted job in the database
        applyresponse = responsemodel(
            username=username,
            response=response,
            teachername=teachername,
            videotopic =videotopic ,
            videodescription=videodescription
        )
        applyresponse.save()
        return render(request, "postresponse.html", {"alert_message": "submitted successfully","teachername":teachername,"videotopic":videotopic,"videodescription":videodescription})


    return render(request,"postresponse.html",{"teachername":teachername,"videotopic":videotopic,"videodescription":videodescription})



def viewresponse(request,username):
    if not request.session.get("is_authenticated"):
        return redirect(loginindex)
    response= responsemodel.objects.filter(teachername=username)
    return render(request,'viewresponse.html',{'response':response})


def myuploads(request, username):
    if not request.session.get("is_authenticated"):
        return redirect(loginindex)

    # Fetch data from both models
    video_posts = postvideomodel.objects.filter(teachername=username)
    file_posts = postfilemodel.objects.filter(teachername=username)

    # Initialize lists for video and file data
    videotopic = []
    videodescription = []
    video_url = []
    video_id = []

    filetopic = []
    filedescription = []
    file_url = []
    file_thumbnail = []
    file_id = []

    # Extract video data
    for i in video_posts:
        videotopic.append(i.videotopic)
        videodescription.append(i.videodescription)
        video_url.append(i.videoupload.url if i.videoupload else None)
        video_id.append(i.id)

   
    for i in file_posts:
        filetopic.append(i.filetopic)
        filedescription.append(i.filedescription)
        file_url.append(i.fileupload.url if i.fileupload else None)
        file_thumbnail.append(i.filethumbnail.url if i.filethumbnail else None)
        file_id.append(i.id)

   
    video_data = zip(videotopic, videodescription, video_url, video_id)
    file_data = zip(filetopic, filedescription, file_url, file_thumbnail, file_id)

   
    return render(request, 'myuploads.html', {"video_data": video_data, "file_data": file_data})




def delitem(request, id):
    if not request.session.get("is_authenticated"):
        return redirect(loginindex)

    message = "Item not found"  # Default message

    try:
        video_post = postvideomodel.objects.get(id=id)
        video_post.delete()
        message = "Post deleted"
    except postvideomodel.DoesNotExist:
        pass 

    try:
        file_post = postfilemodel.objects.get(id=id)
        file_post.delete()
        message = "Post deleted"
    except postfilemodel.DoesNotExist:
        pass 

    return HttpResponse(f"""
        <script>
            alert("{message}");
            window.location.href = document.referrer || '/';  // Redirect back
        </script>
    """)