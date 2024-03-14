from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bike, Basket, Order
from .forms import BikeForm


def index_view(request):
    return render(request, 'index.html')


def bike_view(request):
    bikes = Bike.objects.all()
    # bike_name = [bike.name for bike in bikes]

    return render(request, 'bikes.html', {'bikes': bikes})


def order_view(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return redirect('order.html', order_id=order)


class BikeView(View):

    def get(self, request, bike_id):
        bike = get_object_or_404(Bike, pk=bike_id)
        form = BikeForm()
        return render(request, 'bike_details.html', {'bike': bike, 'form': form})

    def post(self, request, bike_id):
        bike = get_object_or_404(Bike, pk=bike_id)
        basket = Basket()
        form = BikeForm(request.POST or None)
        error_message = "Unfortunately, this bike is currently not available due to insufficient parts."

        if bike.tire.quantity >= 2 and bike.frame.quantity >= 1 and bike.seat.quantity >= 1:
            if bike.has_basket is True and basket.quantity >= 1:
                if request.method == "POST" and form.is_valid():
                    form.save()
                    return redirect('order.html')
            else:
                return render(request, 'bike_details.html', {'bike': bike, \
                                                             'error_message': error_message})
        else:
            return render(request, 'bike_details.html', {'bike': bike, \
                                                         'error_message': error_message})



    # def order_bike(self, request):
    #     bike_parts_available = True
    #     if bike_parts_available:
    #         form = BikeOrderForm(request.POST or None)
    #         if request.method == 'POST' and form.is_valid():
    #             return render(request, "bike_detail.html", {'form': form})
    #     else:
    #         error_message = "Unfortunately, this bike is currently not available."
    #         return render(request, "bike_detail.html", {'error_message': error_message})
