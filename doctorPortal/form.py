from django import forms
from django.forms.widgets import DateInput
from . import models

class addPatientForm(forms.ModelForm):
    class Meta:
        model = models.PateintModel
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["fullname"].widget.attrs.update({"placeholder":"Enter Fullname"})
        self.fields["age"].widget.attrs.update({"placeholder":"Enter Age","type":"number"})
        self.fields["symptoms"].widget.attrs.update({"placeholder":"Enter Reason"})
        self.fields["mobile"].widget.attrs.update({"placeholder":"Enter Mobile Number"})
        self.fields["address"].widget.attrs.update({"placeholder":"Enter Address"})

class addDoctorForm(forms.ModelForm):
    class Meta:
        model = models.DoctorsModel
        fields = "__all__"
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)    
        self.fields["fullname"].widget.attrs.update({"placeholder":"Enter Fullname"})
        self.fields["age"].widget.attrs.update({"placeholder":"Enter Age","type":"number"})
        self.fields["specialize"].widget.attrs.update({"placeholder":"Enter Specialize"})
        self.fields["mobile"].widget.attrs.update({"placeholder":"Enter Mobile Number"})
        self.fields["address"].widget.attrs.update({"placeholder":"Enter Address"})

class addAppointmentForm(forms.ModelForm):
    class Meta:
        model = models.AppointmentModel
        fields = "__all__"
        widgets = {
            "time":DateInput(attrs={"type":"date"})
        }
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["pateint"].empty_label = "Select A Patient"
        self.fields["doctor"].empty_label = "Select A Doctor"
        self.fields["subject"].widget.attrs.update({"placeholder":"Enter Subject"})

        