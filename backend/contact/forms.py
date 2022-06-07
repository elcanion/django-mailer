from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    inquiry = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    def get_info(self):
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        message = f'{name} (:{from_email}:) said:'
        message += f'\n"{subject}"\n\n'
        message += cl_data.get('message')

        return subject, message

    def send(self):
        subject, message = self.get_info()

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
