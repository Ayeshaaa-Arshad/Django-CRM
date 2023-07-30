from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from website.forms import SignUpForm,RecordForm
from website.models import Record
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Function Based Home View
# def home(request):
#     records=Record.objects.all()
#
#     if request.method=='POST':
#         username=request.POST['username']
#         password = request.POST['password']
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             messages.success(request,"Successfully logged In")
#             return redirect('home')
#         else:
#             messages.success(request, "Failed to log In")
#             return redirect('home')
#     else:
#         return render(request,'home.html',{'records':records})

class home(View):
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

# Function based Logout
# def logout_view(request):
#     logout(request)
#     messages.success(request,"Logged out")
#     return redirect('home')

class logout_view(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Logged out")
        return redirect('home')

# Function based Register View
# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, "Successfully Registered")
#             return redirect('home')
#         else:
#             return render(request, 'register.html', {'form': form})
#     else:
#         form = SignUpForm()
#         return render(request, 'register.html', {'form': form})
#     return render(request, 'register.html', {'form': form})

class register(View):
    template_name='register.html'
    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successfully Registered")
            return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})
    def get(self,request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

# Function Based Record View
# def record(request,pk):
#     if request.user.is_authenticated:
#         record=Record.objects.get(id=pk)
#         return render(request,'record.html',{'cust_record':record})
#     else:
#         messages.success(request,"First Login or signup please !!!")
#         return redirect('home')

class record(LoginRequiredMixin, View):
    template_name='record.html'
    def get_record(pk):
        try:
            return Record.objects.get(id=pk)
        except:
            return None
    def get(self,request,pk):
        rec= record.get_record(pk)
        if rec:
            return render(request, self.template_name, {'cust_record': rec})
        else:
            messages.success(request,"No Record Found !!!")
            return redirect('home')

    def handle_no_permission(self):
        # Custom error message when user is not logged in
        messages.error(self.request, "You need to log in to access this page.")
        return redirect('home')

# Function Based Delete View
# def delete(request,pk):
#     if request.user.is_authenticated:
#         Record.objects.filter(id=pk).delete()
#         messages.success(request,"Record Deleted Successfully !!!")
#         return redirect('home')
#     else:
#         messages.success(request,"First Login or signup please !!!")
#         return redirect('home')

class delete(LoginRequiredMixin,View):
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

# Function based Add Record
# def add_record(request):
# 	form = AddRecordForm(request.POST or None)
# 	if request.user.is_authenticated:
# 		if request.method == "POST":
# 			if form.is_valid():
# 				add_record = form.save()
# 				messages.success(request, "Record Added...")
# 				return redirect('home')
# 	    return render(request, 'add_record.html', {'form':form})
# 	else:
# 		messages.success(request, "You Must Be Logged In...")
# 		return redirect('home')
# @login_required(login_url='home')
# def add_record(request):
#     if request.method == "POST":
#         form = AddRecordForm(request.POST,request.FILES)
#         if form.is_valid():
#             add_record = form.save()
#             messages.success(request, "Record Added...")
#             return redirect('home')
#     else:
#         form = AddRecordForm()
#
#     return render(request, 'add_record.html', {'form': form})
class add_record(LoginRequiredMixin,View):
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

# Function based UpdateView
# def update_record(request, pk):
# 	if request.user.is_authenticated:
# 		current_record = Record.objects.get(id=pk)
# 		form = AddRecordForm(request.POST or None, request.FILES or None,instance=current_record)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, "Record Has Been Updated!")
# 			return redirect('home')
# 		return render(request, 'update_record.html', {'form':form})
# 	else:
# 		messages.success(request, "You Must Be Logged In...")
# 		return redirect('home')

class update_record(LoginRequiredMixin,View):
    template_name='update_record.html'
    def post(self,request,pk):
        current_record=record.get_record(pk)
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
        current_record = record.get_record(pk)
        if current_record:
            form = RecordForm(request.POST or None, request.FILES or None, instance=current_record)
            return render(request, self.template_name, {'form': form})
        else :
            messages.success(request, "No Record Found!")
            return redirect('home')

    def handle_no_permission(self):
        messages.error(self.request, "You need to log in to Update the record.")
        return redirect('home')
