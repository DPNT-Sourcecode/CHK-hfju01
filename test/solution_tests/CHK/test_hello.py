from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        """
        Check prices.
        """
        assert checkout_solution.checkout("test") == -1
        
        