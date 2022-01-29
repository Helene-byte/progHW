class Item:
    '''
    Создайте пользовательский класс для описания товара (предположим,
это задел для интернет-магазина). В качестве полей товара можете
использовать значение цены, описание, габариты товара. Создайте пару
экземпляров вашего класса и протестируйте их работу.
    '''
    def __init__(self, item, price, color, size):
        self.item = item
        self.price = price
        self.color = color
        self.size = size

    def __str__(self):
        return "\n"\
            "Item name: " + self.item + "\n" \
               + "Price: " + str(self.price) + "\n" \
               + "Color: " + self.color + "\n" \
               + "Size: " + self.size+"\n" \
                + "+++++++++++++++++++++++"


class Customer:
    """
    Создайте класс «Покупатель». В качестве полей можете использовать
    фамилию, имя, отчество, мобильный телефон и т. д.
    """
    def __init__(self, surname, name, phone, address):
        self.surname = surname
        self.name = name
        self.phone = phone
        self.address = address

    def __str__(self):
        return "Surname: " + self.surname + "\n" \
               + "Name: " + self.name + "\n" \
               + "Phone: " + self.phone + "\n" \
               + "Address: " + self.address + "\n" \
               + "+++++++++++++++++++++++"

class Order:
    """
    Заказ может содержать несколько товаров.
Заказ должен содержать данные о пользователе, который его осуществил.
Реализуйте метод вычисления суммарной стоимости заказа. Определите
метод __str__() для корректного вывода информации о этом заказе.
    """
    def __init__(self, customer, items, quantity):
        self.customer = customer
        self.items = items
        self.quantity = quantity

    def __str__(self):

        return "Customer: " + self.customer + "\n" \
               + "Items: " +  ('[%s]' % ', '.join(map(str, self.items))) + "\n"\
               + "Quantity : " +( '[%s]' % ', '.join(map(str, self.quantity)))  + "\n"\
               + "Total amount : " + str(self.total_amount(items = self.items, quantity =  self.quantity)) + "\n"\
               + "+++++++++++++++++++++++"

    def total_amount(self,items,quantity):
        total=[]
        items_price=[]
        self.quantity=quantity
        self.items=items
        for item in self.items:
            items_price.append(item.price)
        for num1, num2 in zip(items_price, self.quantity):
            total.append(num1 * num2)
        return sum(total)

item1=Item("D1",50.50, "red", "M")
item2=Item("D1",45, "white", "M")
customer1=Customer("Bloggs", "Joe", "380661112233", "NY, Brooklyn")
customer2=Customer("Jones", "Bridgit", "380661112235", "London, BY")
order1=Order(customer1.name,[item1,item2],[1,2])
to_pay=order1.total_amount([item1,item2],[1,2])

print(to_pay)
print(order1)