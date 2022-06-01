from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.views import View
from .forms import MailForm, MailForm2
from .models import *
from django.urls import reverse_lazy


def mail(request):
    return render(request, 'mail/mail.html')


def mail1(request):
    return render(request, 'mail/v1.html')


def mail2(request):
    return render(request, 'mail/v2.html')


def mail3(request):
    return render(request, 'mail/v3.html')


def partners(request):
    partner = Partner.objects.all()
    return render(request, 'partners/partners.html', {"partners": partner})


def contacts(request):
    contact1 = Contact.objects.filter(department=1)
    contact2 = Contact.objects.filter(department=2)
    contact3 = Contact.objects.filter(department=3)

    return render(request, 'contacts/contacts.html', {"contacts1": contact1, "contacts2": contact2, "contacts3": contact3})


def job(request):
    return render(request, 'job/job.html')


class OrderCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = MailForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.data.get('first_name')
            name = form.data.get('name')
            last_name = form.data.get('last_name')
            email = form.data.get('email')
            phone = form.data.get('phone')
            address = form.data.get('address')
            text = form.data.get('text')
            message = f'ФИО: {first_name} {name} {last_name}\nПочта: {email}\nТелефон: {phone}\nАдрес: {address}\n' \
                      f'Текст обращения: {text}\nФайл: Смотрите в админ панели'

            send_mail(
                f'Физ лицо: {first_name} {name} {last_name}',
                message,
                'mazzzek@bk.ru',
                ['trud14@bk.ru'],
                fail_silently=False,
            )

            form.save()
            messages.add_message(request, messages.SUCCESS, 'Обращение отправлено!')
            return HttpResponseRedirect(redirect_to=reverse_lazy('v2'))
        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных.')


class OrderCreateView2(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = MailForm2(request.POST, request.FILES)
        if form.is_valid():
            organ = form.data.get('organ')
            position = form.data.get('position')
            inn = form.data.get('inn')
            first_name = form.data.get('first_name')
            name = form.data.get('name')
            last_name = form.data.get('last_name')
            email = form.data.get('email')
            phone = form.data.get('phone')
            address = form.data.get('address')
            text = form.data.get('text')
            message = f'Организация: {organ}\nИНН: {inn}\nДолжность: {position}' \
                      f'ФИО: {first_name} {name} {last_name}\nПочта: {email}\nТелефон: {phone}\nАдрес: {address}\n' \
                      f'Текст обращения: {text}\nФайл: Смотрите в админ панели'

            send_mail(
                f'Юр лицо: {organ} {position} {inn}',
                message,
                'mazzzek@bk.ru',
                ['trud14@bk.ru'],
                fail_silently=False,
            )

            form.save()
            messages.add_message(request, messages.SUCCESS, 'Обращение отправлено!')
            return HttpResponseRedirect(redirect_to=reverse_lazy('v3'))
        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных.')
