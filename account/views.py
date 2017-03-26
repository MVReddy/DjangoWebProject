from django.http import HttpResponse
from models import Question, Account
from django.shortcuts import render


def index(request):
    data = Question.objects.all()

    response = [(obj.question_text, obj.pub_date) for obj in data]
    response.append("ABC jad;lads;kf;amsd/")
    return HttpResponse(response)


def accounts(request):
    accounts_data = Account.objects.all()

    context = {'xyz': accounts_data, 'a': 10}

    return render(request, 'accounts.html', context)


def detail(request, account_id):
    account = Account.objects.get(pk=account_id)

    context = {'account': account}

    return render(request, 'new_detail.html', context)
