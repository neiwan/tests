import my_lib
import pytest


# тест калькулятора
class TestCalc:
    # задаем числа и знак действия
    @pytest.fixture()
    def plus(self):
        return 10, 10, '+'

    # задаем числа и знак действия
    @pytest.fixture()
    def minus(self):
        return 10, 10, '-'

    # задаем числа и знак действия
    @pytest.fixture()
    def multiply(self):
        return 10, 10, '*'

    # задаем числа и знак действия
    @pytest.fixture()
    def divide(self):
        return 10, 10, '/'

    # задачем значения с ошибкой
    @pytest.fixture()
    def error(self):
        return '+', '-', '+'

    # тест калькулятора 10+10
    def testPlus(self, plus):
        assert my_lib.calc(*plus) == 20

    # тест калькулятора 10-10
    def testMinus(self, minus):
        assert my_lib.calc(*minus) == 0

    # тест калькулятора 10*10
    def testMultiply(self, multiply):
        assert my_lib.calc(*multiply) == 100

    # тест калькулятора 10/10
    def testDivide(self, divide):
        assert my_lib.calc(*divide) == 1

    # тест калькулятора с ошибкой TypeError исключая ошибку
    def testerrorwithpytest(self, error):
        with pytest.raises(TypeError):
            my_lib.calc(error)
