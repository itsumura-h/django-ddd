from django.shortcuts import redirect, render

class TestViews:
    def show(request):
        return render(request, 'test.html')