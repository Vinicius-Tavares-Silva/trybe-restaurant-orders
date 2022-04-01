from collections import Counter
import csv


def analyze_log(path_to_file):
    try:
        orders = read_csv(path_to_file)
    except FileNotFoundError:
        if path_to_file.endswith(".csv"):
            raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    most_ordered = most_ordered_by_customer(orders, 'maria')
    selected_order = count_order(orders, 'arnaldo', 'hamburguer')
    never_asked_by_customer = never_asked(orders, 'joao')
    never_visited = days_never_visited(orders, 'joao')
    file = open('data/mkt_campaign.txt', 'w')
    file.write(f'{most_ordered}\n')
    file.write(f'{selected_order}\n')
    file.write(f'{never_asked_by_customer}\n')
    file.write(f'{never_visited}\n')
    file.close


def read_csv(path):
    with open(path) as file:
        header = ['customer', 'order', 'day']
        orders = []
        order_reader = csv.reader(file, delimiter=",", quotechar='"')
        data = order_reader
        for row in data:
            order = dict(zip(header, row))
            orders.append(order)
    return orders


def most_ordered_by_customer(orders, customer):
    customer_orders = [
        order['order'] for order in orders if order['customer'] == customer
    ]
    most_ordered = max(set(customer_orders), key=customer_orders.count)
    return most_ordered


def count_order(orders, customer, order):
    customer_orders = [
        order['order'] for order in orders if order['customer'] == customer
    ]
    count_orders = Counter(customer_orders)
    selected_order = count_orders[order]
    return selected_order


def never_asked(orders, customer):
    menu = set([order['order'] for order in orders])
    customer_orders = [
        order['order'] for order in orders if order['customer'] == customer
    ]
    never_asked = menu.difference(customer_orders)
    return never_asked


def days_never_visited(orders, customer):
    days = set([order['day'] for order in orders])
    customer_days_visited = [
        order['day'] for order in orders if order['customer'] == customer
    ]
    days_never_visited = days.difference(customer_days_visited)
    return days_never_visited


analyze_log('data/orders_1.csv')
