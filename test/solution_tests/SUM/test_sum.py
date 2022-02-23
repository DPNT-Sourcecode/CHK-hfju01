from lib.solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        """
        Check success results.
        """
        assert sum_solution.compute(1, 2) == 3
        assert sum_solution.compute(0, 0) == 0

    def test_invalid_input(self):
        """
        Check invalid inputs.

        TODO: use fixture/factory
        """
        assert sum_solution.compute(-1, 2) == None
        assert sum_solution.compute("a", 2) == None
        assert sum_solution.compute(10.3, 2) == None
        assert sum_solution.compute(101, 2) == None
        assert sum_solution.compute(1, 101) == None
        