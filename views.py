from django.shortcuts import render

from rest_framework.views import APIView

# Create your views here.


class Index(APIView):

    def get(self, request, *args, **kwargs):

        return render(request, template_name='index.html')


class Talk(APIView):

    def get(self, request, *args, **kwargs):

        return render(request, template_name='talk.html')


class Order(APIView):

    def get(self, request, *args, **kwargs):

        return render(request, template_name='order.html')


class ListDetail(APIView):

    def get(self, request, *args, **kwargs):

        return render(
            request, 
            template_name='list_detail.html', 
            context={"area": request.GET.get('area')}
        )


class TakeOrder(APIView):

    def get(self, request, *args, **kwargs):

        return render(
            request, 
            template_name='take_order.html',
            context={"order_type": request.GET.get('order_type')}
        )
