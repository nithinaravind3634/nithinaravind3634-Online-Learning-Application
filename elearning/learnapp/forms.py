from django import forms

class teacherform(forms.Form):
    teacherusername=forms.CharField(max_length=20)
    teacheremail=forms.EmailField()
    teacherphone=forms.CharField(max_length=10)
    teacherpassword=forms.CharField(max_length=20)
    teachercpassword=forms.CharField(max_length=20)


class studentform(forms.Form):
    studentusername=forms.CharField(max_length=20)
    studentemail=forms.EmailField()
    studentphone=forms.CharField(max_length=10)
    studentpassword=forms.CharField(max_length=20)
    studentcpassword=forms.CharField(max_length=20)