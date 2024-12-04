import logging
import unittest
import u_12_4_loging

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            obj = u_12_4_loging.Runner('walker', -1)
            for i in range(10):
                obj.walk()
            self.assertEqual(obj.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as VaEr:
            logging.warning(f"Неверная скорость для Runner, {VaEr.args}", exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            obj = u_12_4_loging.Runner(55)
            for i in range(10):
                obj.run()
            self.assertEqual(obj.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as TyEr:
            logging.warning(f"Неверный тип данных для объекта Runner, {TyEr.args}", exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj_1 = u_12_4_loging.Runner('Runker')
        obj_2 = u_12_4_loging.Runner('Walker')
        for i in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1, obj_2)


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")
