from django.shortcuts import render
from testapp.models import Student
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from testapp.forms import SignUpForm
# Create your views here.
def Home(request):
    return render(request,'testapp/homepage.html')

def RegistrationView(request):
    student = SignUpForm()
    if request.method == 'POST':
        student = SignUpForm(request.POST)
        if student.is_valid():
            user = student.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect("/accounts/login/")
    return render (request, 'testapp/signup_page.html', {'mykey':student})

class StudentFormView(CreateView):
    model = Student
    fields = '__all__'
    def get_success_url(self):
        return reverse('home')
class StudentListView(ListView):
    model = Student
    template_name='testapp/student_record.html'
    context_object_name='students'


class StudentDelete(DeleteView):
    model = Student
    def get_success_url(request):
        return reverse('student_record')

class StudentUpdate(UpdateView):
    model = Student
    fields="__all__"
    def get_success_url(self):
        return reverse('student_record')
