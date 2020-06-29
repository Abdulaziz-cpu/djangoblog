from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="İstifadəçi adı",widget=forms.TextInput(attrs={'placeholder':'İstifadəçi adı',"class":"form-control"}))
    password = forms.CharField(label="Parol",widget=forms.PasswordInput(attrs={'placeholder':'parol',"class":"form-control"}))
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="İstifadəçi adı",widget=forms.TextInput(attrs={'placeholder':'İstifadəçi adı',"class":"form-control"}))
    first_name = forms.CharField(max_length=50,label="Adı",widget=forms.TextInput(attrs={'placeholder':'Ad',"class":"form-control"}))
    last_name = forms.CharField(max_length=50,label="Soyadı",widget=forms.TextInput(attrs={'placeholder':'Soyad',"class":"form-control"}))
    email = forms.CharField(max_length=50,label="Email adresi",widget=forms.EmailInput(attrs={'placeholder':'example@examp.com',"class":"form-control"}))
    password = forms.CharField(max_length=20,label="Parol",widget=forms.PasswordInput(attrs={'placeholder':'parol',"class":"form-control"}))
    confrim = forms.CharField(max_length=20,label="Parolu təkrar edin",widget=forms.PasswordInput(attrs={'placeholder':'parol',"class":"form-control" }))
    checkbox = forms.BooleanField(required=True, label="Qaydalarla razısınız?")
    def clean(self):
        username = self.cleaned_data.get("username")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confrim = self.cleaned_data.get("confrim")
        checkbox = self.cleaned_data.get("checkbox")
        

        if password and confrim and password != confrim:
            raise forms.ValidationError("Parollar eyni deyil!!!")
        else:
            values = {
                "username" : username,
                "first_name" : first_name,
                "last_name" : last_name,
                "email" : email,
                "password" : password,
                "checkbox" : checkbox,
                
            
                
                
            }
            return values

    