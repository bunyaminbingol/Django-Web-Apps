from django import forms
from myapp.models import Product
from django.forms import widgets


# class ProductCreateForm(forms.Form):
#     product_name = forms.CharField(label="Ürün Adı", required = True, min_length=3, max_length=20,
#                                    error_messages={
#                                        "min_length": "min 3 karakter giriniz",
#                                        "max_length": "max 20 karakter giriniz"}, 
#                                    widget=forms.TextInput(attrs={'class': 'form-control'})) # required = False -> boş bırakılabilir
#     price = forms.DecimalField(label="Fiyat", min_value=10, max_value=10000, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     description = forms.CharField(label="Ürün Açıklaması", widget=forms.Textarea(attrs={'class': 'form-control'}))
#     slug = forms.SlugField(label="Url", widget=forms.TextInput(attrs={'class': 'form-control'}))

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product # modeli Product olarak belirledik
        fields = ('name', 'price', 'description', 'slug', 'image') # hangi alanların gözükeceğini belirledik
        error_messages = {
            "name": {
                "required": "Ürün adı boş bırakılamaz",
                "max_length": "max 20 karakter giriniz",
                "min_length": "min 3 karakter giriniz"
            }
        }
        labels = {
            "name": "Ürün Adı",
            "price": "Fiyat",
            "description": "Ürün Açıklaması",
            "slug": "Url"
        }
        widgets = {
            "name": widgets.TextInput(attrs={'class': 'form-control'}),
            "price": widgets.NumberInput(attrs={'class': 'form-control'}), # numberinput sayısal değerler için
            "description": widgets.Textarea(attrs={'class': 'form-control'}),
            "slug": widgets.TextInput(attrs={'class': 'form-control'})
        }
        
class UploadForm(forms.Form):
    image = forms.FileField()