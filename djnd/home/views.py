from django.views.generic import TemplateView


class OurWorkView(TemplateView):
    template_name = "home/our_work_page.html"
    
    # def get(self, request, *args, **kwargs):
