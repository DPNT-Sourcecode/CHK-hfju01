from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        """
        Check prices.
        """
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("AAAAB") == 210
        assert checkout_solution.checkout("AABBAA") == 225
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("CCD") == 65
        assert checkout_solution.checkout("xB") == -1
        assert checkout_solution.checkout("test") == -1
        

        

