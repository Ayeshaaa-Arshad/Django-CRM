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

# Function based Logout

# def logout_view(request):
#     logout(request)
#     messages.success(request,"Logged out")
#     return redirect('home')


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


# Function Based Record View

# def record(request,pk):
#     if request.user.is_authenticated:
#         record=Record.objects.get(id=pk)
#         return render(request,'record.html',{'cust_record':record})
#     else:
#         messages.success(request,"First Login or signup please !!!")
#         return redirect('home')



# Function Based Delete View

# def delete(request,pk):
#     if request.user.is_authenticated:
#         Record.objects.filter(id=pk).delete()
#         messages.success(request,"Record Deleted Successfully !!!")
#         return redirect('home')
#     else:
#         messages.success(request,"First Login or signup please !!!")
#         return redirect('home')



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

