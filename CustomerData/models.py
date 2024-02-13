from django.db import models

# Create your models here.
class Leads(models.Model):
    lead_name=models.CharField(max_length=50)
    lead_type=models.CharField(max_length=50)  
    contact=models.IntegerField()
    address=models.CharField(max_length=50)
    processing=models.CharField(max_length=50)
    
    class Meta:
        db_table="laeds_master"
    
class Deals(models.Model):
    leads=models.ForeignKey(Leads,on_delete=models.CASCADE)
    dealer_Name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    contact=models.IntegerField()
    products_Dealing=models.CharField(max_length=50)
    quotation=models.IntegerField()
    negotiation=models.IntegerField()
    deal_Status=models.CharField(max_length=10)
    
    class Meta:
        db_table="delas_master"    
    
class Task(models.Model):
    task_Type=models.CharField(max_length=30)
    durations=models.CharField(max_length=10)
    status=models.CharField(max_length=10)
    details=models.CharField(max_length=10)        
    
    class Meta:
        db_table="task_master"