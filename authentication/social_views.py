from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.views import View

from django.http import HttpResponseRedirect


'''
class GoogleLogin(View):
    template_name = "authentication/index.html"
    
    
    def get(self, request, *args, **kwargs):
        print("===== self request === ", self.request.GET)
        print("===== request === ", request.GET)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = { 'page_code': SIDEBAR_MENU_PAGE_CODE_CITY }
        context.update(data)
        return context
        
'''
    
class GoogleLogin(View):
    template_name = 'authentication/index.html'

    def get(self, request, *args, **kwargs):
        print("Post ", request.GET)
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        print("Post ", request.POST)
        return render(request, self.template_name)