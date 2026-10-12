class TestCase:
    def __init__(self, steps=None, result=None):
        self.steps = {} if steps is None else steps
        self.result = result

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        del self.steps[step_number]

    def set_result(self, result):
        self.result = result

    def get_test_case(self):
        print({
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        })


test_case = TestCase()

test_case.set_step(1, 'Перейти на сайт')
test_case.set_step(2, 'Перейти в раздел Товары')
test_case.set_step(3, 'Нажать кнопку «В корзину» у первого товара')

test_case.set_result('Товар окажется в корзине')

test_case.get_test_case()