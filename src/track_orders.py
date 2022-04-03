class TrackOrders:

    def __init__(self):
        self.orders = list()
        self.orders_quantity = 0

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        self.orders_quantity = len(self.orders)
        return self.orders_quantity

    def add_new_order(self, customer, order, day):
        header = ['customer', 'order', 'day']
        row = [customer, order, day]
        new_order = dict(zip(header, row))
        self.orders.append(new_order)

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = [
            order['order'] for order in self.orders
            if order['customer'] == customer
        ]
        most_ordered = max(set(customer_orders), key=customer_orders.count)
        return most_ordered

    def get_never_ordered_per_customer(self, customer):
        menu = set([order['order'] for order in self.orders])
        customer_orders = [
            order['order'] for order in self.orders
            if order['customer'] == customer
        ]
        never_asked = menu.difference(customer_orders)
        return never_asked

    def get_days_never_visited_per_customer(self, customer):
        days = set([order['day'] for order in self.orders])
        customer_days_visited = [
            order['day'] for order in self.orders
            if order['customer'] == customer
        ]
        days_never_visited = days.difference(customer_days_visited)
        return days_never_visited

    def get_busiest_day(self):
        customer_orders = [order['day'] for order in self.orders]
        busiest_day = max(set(customer_orders), key=customer_orders.count)
        return busiest_day

    def get_least_busy_day(self):
        customer_orders = [order['day'] for order in self.orders]
        least_busy_day = min(set(customer_orders), key=customer_orders.count)
        return least_busy_day
