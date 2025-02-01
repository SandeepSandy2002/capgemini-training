
class customers:
    def __init__(self):
        self.customer_id = list(map(int, input("Enter customer IDs: ").split()))
        self.customer_name = list(input('Enter customer names: ').split())
        self.phone = list(map(int, input('Enter phone numbers: ').split()))
        self.email = list(input('Enter email of customers: ').split())
        self.street = list(input('Enter the street names: ').split())
        self.city = list(input('Enter the city names: ').split())
        self.state = list(input('Enter the state names: ').split())
        self.zipcode = list(map(int, input('Enter the zip codes: ').split()))

class orders(customers):
    def __init__(self):
        super().__init__()
        self.orderid = list(map(int, input("Enter order IDs: ").split()))
        self.orderstatus = list(input('Enter order statuses: ').split())
        self.required_date = list(map(int, input("Enter required dates (format: day month year): ").split()))
        self.shipped_date = list(map(int, input("Enter shipped dates (format: day month year): ").split()))
        self.store_id = args[5]
        self.staff_id = args[6]

class customers_order(orders):  # Use dictionary
    def __init__(self):
        super().__init__()
        if len(self.customer_id) == len(self.orderid):  # Ensure equal length before zipping
            self.orderdetails = dict(zip(self.customer_id, self.orderid))
        else:
            self.orderdetails = {}
            print("Warning: customer_id and orderid lists have different lengths.")
        self.orderstaus=dict(zip(self.required_date,self.shipped_date))

c1 = customers()
c2 = customers_order()

print("Zipcode list:", c2.zipcode)
print("Order Details customerid:orderid ", c2.orderdetails)
print(f'order status :{c2.orderstaus}')


