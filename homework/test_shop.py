"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(10) == True
        assert product.check_quantity(1000) == True
        assert product.check_quantity(1001) == False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product_count = product.quantity
        buy_count = 50
        product.buy(buy_count)
        assert product.quantity == product_count - buy_count




    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 5)
        assert product in cart.products
        assert cart.products[product] == 5

    def test_remove_product_from_cart(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 5)
        assert cart.products[product] == 5

    def test_remove_product_empty_quantity(self,cart, product):
        cart.add_product(product, 2)
        cart.remove_product(product)
        assert product not in cart.products

    def test_remove_product_more_than_in_cart(self, cart, product):
        cart.add_product(product, 7)
        cart.remove_product(product, 10)
        assert product not in cart.products

    def test_clear_cart(self, cart, product):
        cart.add_product(product, 3)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_prise(self, cart, product):
        cart.add_product(product, 3)
        assert cart.get_total_price() == 300

    def test_buy(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()

    def test_buy_more_than_in_stock(self,cart, product):
        cart.add_product(product, 1001)
        pytest.raises(ValueError, cart.buy)

