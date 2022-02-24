from lib.solutions.CHK import checkout_solution

"""
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+
"""
class TestSum():
    def test_checkout(self):
        """
        Check prices.
        """
        assert checkout_solution.checkout("AAAAAAAABB") == 200 + 130 + 45
        assert checkout_solution.checkout("AAAAAAAABBBEE") == 200 + 130 + 45 + 80
        assert checkout_solution.checkout("EEBB") == 110
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("AAAAB") == 210
        assert checkout_solution.checkout("AABBAA") == 225
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("CCD") == 55
        assert checkout_solution.checkout("xB") == -1
        assert checkout_solution.checkout("test") == -1
        assert checkout_solution.checkout("ABCa") == -1
        

        
