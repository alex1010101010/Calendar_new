from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy



class SignUpView(generic.CreateView):
    form_class = UserCreationForm #from Django? How can I modify this?
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    #What does the method below do?
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.extra_field = self.cleaned_data["extra_field"]
        if commit:
            user.save()
        return user
