from django.shortcuts import render


def index_view(request):
    context = {}
    return render(request, template_name='base.html', context=context)
