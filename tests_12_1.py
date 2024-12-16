import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = runner.Runner('Евгений')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runer = runner.Runner('Елизаветта')
        for i in range(10):
            runer.run()
        self.assertEqual(runer.distance, 100)

    def test_challenge(self):
        walker2 = runner.Runner('Катя')
        runer2 = runner.Runner('Саша')
        for i in range(10):
            walker2.walk()
            runer2.run()
        self.assertNotEqual(runer2.distance, walker2.distance)


