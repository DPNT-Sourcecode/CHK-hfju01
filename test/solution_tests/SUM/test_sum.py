from lib.solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_invalid_input(self):
        assert sum_solution.compute(-1, 2) == None
        assert sum_solution.compute("a", 2) == None
        assert sum_solution.compute(10.3, 2) == None
        assert sum_solution.compute(101, 2) == None
        assert sum_solution.compute(1, 101) == None
        

        


