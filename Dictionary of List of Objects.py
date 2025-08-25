class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location


list_of_customers = [Customer(101, 'Mark', 'US'),
                     Customer(102, 'Jane', 'Japan'),
                     Customer(103, 'Kumar', 'India')]

for Customer in list_of_customers:
    print (Customer.cust_id,Customer.cust_name,Customer.location)

print()

dict_of_customer = {
    "c1":list_of_customers[0],
    "c2":list_of_customers[1],
    "c3":list_of_customers[2]
}

for key,value in dict_of_customer.items():
    print (value.cust_id,value.cust_name,value.location)