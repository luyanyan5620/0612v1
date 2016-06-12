from django.forms import ModelForm 
from jlpt1.models import ExamInfo

# create your ..
class ExamInfoForm(ModelForm):  
    class Meta:  
        model = ExamInfo  
        fields = '__all__' 
