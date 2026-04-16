from django.shortcuts import render
from .models import Client
from datetime import date

def get_clients(request):
    today = date.today()

    clients = Client.objects.filter(is_deleted=False)

    # filtro (opcional)
    clients = clients.filter(name__icontains='João')
    clients = clients.filter(birth_date__lt=f"{today.year - 18}-01-01")

    # 👇 cálculo manual (SEM ERRO)
    for client in clients:
        orders = client.orders.all()

        client.total_orders = sum(order.quantity for order in orders)
        client.total_spent = sum(order.quantity * order.price for order in orders)

    return render(request, 'clients.html', {
        'clients': clients
    })