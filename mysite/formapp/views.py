from django.shortcuts import render
from django.core.mail import send_mail

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Email to admin (yourself)
        send_mail(
            subject='New Contact Form Submission',
            message=full_message,
            from_email='your_email@gmail.com',
            recipient_list=['your_email@gmail.com'],
            fail_silently=False,
        )

        # Auto reply to the user
        send_mail(
            subject='Thanks for contacting us!',
            message=f'Dear {name},\n\nWe received your message and will get back to you soon.\n\n- Team Sakshi',
            from_email='your_email@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )

        return render(request, 'formapp/thankyou.html', {'name': name})

    return render(request, 'formapp/contact.html')