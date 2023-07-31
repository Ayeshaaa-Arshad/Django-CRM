from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from website.forms import SignUpForm,RecordForm
from website.models import Record
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class HomeView(View):
    template_name='home.html'
    def get(self,request):
        records = Record.objects.all()
        return render(request, self.template_name, {'records': records})
    def post(self,request):
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged In")
            return redirect('home')
        else:
            messages.success(request, "Failed to log In")
            return redirect('home')

class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Logged out")
        return redirect('home')

class RegisterView(View):
    template_name='register.html'
    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.validated_data['username']
            password = form.validated_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successfully Registered")
            return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})
    def get(self,request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

class RecordView(LoginRequiredMixin, View):
    template_name='record.html'
    @classmethod
    def get_record(cls,pk):
        try:
            return Record.objects.get(id=pk)
        except:
            return None
    def get(self,request,pk):
        rec= RecordView.get_record(pk)
        if rec:
            return render(request, self.template_name, {'user_record': rec})
        else:
            messages.success(request,"No Record Found !!!")
            return redirect('home')

    def handle_no_permission(self):
        # Custom error message when user is not logged in
        messages.error(self.request, "You need to log in to access this page.")
        return redirect('home')

class DeleteRecordView(LoginRequiredMixin,View):
    def del_record(self,pk):
        try:
            return Record.objects.filter(id=pk).delete()
        except Record.DoesNotExist:
            return None
    def get(self,request,pk):
        status=self.del_record(pk)
        if status[0]>0:
            messages.success(request,"Record Deleted Successfully !!!")
            return redirect('home')
        else:
            messages.success(request,"Record Not Found !!!")
            return redirect('home')
    def handle_no_permission(self):
        messages.error(self.request, "You need to log in to Delete the record.")
        return redirect('home')

class AddRecordView(LoginRequiredMixin,View):
    template_name='add_record.html'
    def post(self,request):
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            add_record = form.save()
            messages.success(request, "Record Added...")
            return redirect('home')
        else:
            messages.success(request,"Invalid -- Fill the form Again!!")
            form = RecordForm()
            return render(request, self.template_name, {'form': form})
    def get(self,request):
        form = RecordForm()
        return render(request, self.template_name, {'form': form})

class UpdateRecordView(LoginRequiredMixin,View):
    template_name='update_record.html'
    def post(self,request,pk):
        current_record=RecordView.get_record(pk)
        if current_record:
            form = RecordForm(request.POST or None, request.FILES or None, instance=current_record)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Has Been Updated!")
                return redirect('home')
            return render(request, self.template_name, {'form': form})
        else:
            messages.success(request, "No Record Found!")
            return redirect('home')

    def get(self,request,pk):
        current_record = RecordView.get_record(pk)
        if current_record:
            form = RecordForm(request.POST or None, request.FILES or None, instance=current_record)
            return render(request, self.template_name, {'form': form})
        else :
            messages.success(request, "No Record Found!")
            return redirect('home')

    def handle_no_permission(self):
        messages.error(self.request, "You need to log in to Update the record.")
        return redirect('home')
