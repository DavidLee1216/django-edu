from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.views.generic.edit import FormView

from contactus.forms import ContactUsForm, SUBJECT_CHOICES
from MxOnline.settings import EMAIL_FROM


class ContactUsView(FormView):
    template_name = 'contact.html'
    email_template_name = 'contact_notification_email.txt'
    form_class = ContactUsForm
    success_url = "/contact/success/"
    subject = "Contact Us Request"

    def get_initial(self):
        initial = super(ContactUsView, self).get_initial()
        if not self.request.user.is_anonymous:
            initial['name'] = self.request.user.get_full_name()
            initial['email'] = self.request.user.email
        initial['subject'] = '-----'

        return initial

    def form_valid(self, form):
        form_data = form.cleaned_data

        if not self.request.user.is_anonymous:
            form_data['username'] = self.request.user.username

        form_data['subject'] = dict(SUBJECT_CHOICES)[form_data['subject']]

        # POST to the support email
        sender = settings.SERVER_EMAIL
        recipients = (getattr(settings, 'CONTACT_US_EMAIL'),)

        tmpl = loader.get_template(self.email_template_name)
        send_mail(self.subject, tmpl.render(form_data), EMAIL_FROM, recipients)

        return super(ContactUsView, self).form_valid(form)
