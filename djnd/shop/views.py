from django.shortcuts import render
from django.views.generic import TemplateView


class ShopView(TemplateView):
    template_name = "shop/shop.html"

    # def get(self, request, *args, **kwargs):
    # get shop items
