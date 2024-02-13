from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def Leads_Create(request):
    if request.method == 'POST':
        formdata = request.POST
        lead_name = formdata.get('lead_name')
        lead_type = formdata.get('lead_type')  # Corrected the field name
        contact = formdata.get('contact')
        address = formdata.get('address')
        processing = formdata.get('processing')
        
        # Create a new Leads instance and save it
        leads = Leads.objects.create(
            lead_name=lead_name,
            lead_type=lead_type,
            contact=contact,
            address=address,
            processing=processing,
        )

        messages.success(request, "Lead created successfully!")

    return render(request, 'leads.html')

def Lead_view(request):
    data = Leads.objects.all()
    return render(request, 'Lead_view.html', {'data': data})




def Deals_Create(request):
    if request.method == 'POST':
        formdata = request.POST
        leads_id = formdata.get("leads_id")
        leads = Leads.objects.get(id = leads_id)
        dealer_Name = formdata.get('dealer_Name')
        address = formdata.get('address')  
        contact = formdata.get('contact')
        products_Dealing = formdata.get('products_Dealing')
        quotation = formdata.get('quotation')
        negotiation = formdata.get('negotiation')
        deal_Status = formdata.get('deal_Status')

        
        # Create a new Deals instance and save it
        deals = Deals(
            leads = leads,
            dealer_Name=dealer_Name,
            address=address,
            contact=contact,
            products_Dealing=products_Dealing,
            quotation=quotation,
            negotiation=negotiation,
            deal_Status=deal_Status,
        )
        deals.save()
        messages.success(request, "Lead created successfully!")
      

    return render(request, 'deals.html', context={"leadss":Leads.objects.all()} )
   
def deals_view(request):
    data = Deals.objects.all()
    return render(request, 'deal_view.html', {'data': data})


def Task_Create(request):
    message=''
    if request.method == 'POST':
        formdata = request.POST
        task_Type = formdata.get('task_Type')
        durations = formdata.get('durations')  
        status = formdata.get('status')
        details = formdata.get('details')
        
        # Create a new Task instance and save it
        tasks = Task.objects.create(
            task_Type=task_Type,
            durations=durations,
            status=status,
            details=details,
        
        )

        message="Task Added successfully!"

    return render(request, 'task.html', context={'result':message})

def task_view(request):
    data = Task.objects.all()
    return render(request, 'Task_view.html', {'data': data})
