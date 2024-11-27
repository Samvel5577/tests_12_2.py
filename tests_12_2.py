class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def __eq__(self, other):
        return self.name == other.name

    def run(self, time):
        self.distance += self.speed * time

    def walk(self, time):
        self.distance += (self.speed / 2) * time


class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}

        times = {runner.name: self.distance / runner.speed for runner in self.runners}

        sorted_runners = sorted(times.items(), key=lambda x: (x[1], x[0]))

        for i, (runner_name, _) in enumerate(sorted_runners, start=1):
            results[i] = runner_name
        return results


import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print("\nРезультаты всех тестов:")
        for key, result in cls.all_results.items():
            print(f"{key}: {result}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, [self.runner1, self.runner3])
        result = tournament.start()
        TournamentTest.all_results[1] = result
        self.assertTrue(list(result.values())[-1] == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        result = tournament.start()
        TournamentTest.all_results[2] = result
        self.assertTrue(list(result.values())[-1] == "Ник")

    def test_all_runners(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        result = tournament.start()
        TournamentTest.all_results[3] = result
        self.assertTrue(list(result.values())[-1] == "Ник")


if __name__ == "__main__":
    unittest.main()
