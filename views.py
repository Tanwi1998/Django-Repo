from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def InsertPageView(request):
    return render(request,"app/insert.html")


def InsertData(request):

    # Data come from HTML to View

    id= request.POST['id']
    fname= request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']

# Creating Object of Model Class

# Inserting data into table

    newuser= Student.objects.create(Id= id,Firstname=fname,Lastname=lname,Email=email,Contact=contact)


# After Insert render on Show Page view

    return redirect("showpage")



# Show Page View

def ShowPage(request):

    # Select * from table
    # For fetching all the data of the table

    all_data= Student.objects.all()
    return render(request,"app/show.html", {'key1': all_data})



# Edit Page View

def EditPage(request,pk):
    get_data= Student.objects.get(id=pk)
    return render(request,"app/edit.html", {'key2': get_data})



# Update Data View

def UpdateData(request,pk):
    udata= Student.objects.get(id=pk)
    udata.Firstname= request.POST['fname']
    udata.Lastname= request.POST['lname']
    udata.Email= request.POST['email']
    udata.Contact= request.POST['contact']



# Query for Update

    udata.save()

# Render to Showpage

    return redirect('showpage')


# Delete Data View

def DeleteData(request,pk):
    ddata= Student.objects.get(id=pk)
    

# Query for Update
   
    ddata.delete()


# Render to ShowPage

    return redirect('showpage')