from django.shortcuts import render

def sendsms(request):
    context= {}
    if request.method == "POST" :
        context['req'] = {}
        context['req']['phoneNumber'] = request.POST.get('phoneNumber')
        context['req']['name'] = request.POST.get('name')
        context['req']['family'] = request.POST.get('family')
        context['req']['messageText'] = request.POST.get('messageText')
    return render(request, 'client/sms.html', context)