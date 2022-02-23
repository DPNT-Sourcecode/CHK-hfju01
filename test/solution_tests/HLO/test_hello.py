from lib.solutions.HLO import hello_solution


class TestSum():
    def test_sum(self):
        """
        Check success results.
        """
        assert hello_solution.hello("test") == "test"
        
        