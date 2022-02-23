from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        """
        Check prices.
        """
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("2B") == 45
        assert checkout_solution.checkout("test") == -1
        

        