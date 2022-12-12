import pytest
import my_lib


# тест чисел Фибоначчи
class TestFibonacci:
    # тест чисел Фибоначчи с n = 10
    def testOnCorrect(self):
        assert my_lib.fibonacci(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    # тест чисел Фибоначчи c n = 0. Функция вызывает исключение IndexError.
    def testZeroCorrect(self):
        with pytest.raises(IndexError):
            my_lib.fibonacci(0)

    # тест с вводом неверного формата числа
    def testTypeIncorrect(self):
        with pytest.raises(TypeError):
            my_lib.fibonacci("21")
