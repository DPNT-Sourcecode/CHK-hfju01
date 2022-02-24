from lib.solutions.CHK import checkout_solution

"""
+------+-------+---------------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
+------+-------+---------------------------------+
"""
class TestSum():
    def test_checkout(self):
        """
        Check prices.
        """
        # assert checkout_solution.checkout("SSTXYZZZ") == 45 + 45 + 20 + 17
        assert checkout_solution.checkout("SSTXYZ") == 45 + 45
        assert checkout_solution.checkout("STXYZ") == 45 + 20 + 17
        assert checkout_solution.checkout("SSS") == 45
        assert checkout_solution.checkout("VVVVV") == 220
        assert checkout_solution.checkout("UUU") == 40 * 3
        assert checkout_solution.checkout("UUUU") == 40 * 3
        assert checkout_solution.checkout("RRRQQQ") ==  150 + 60
        assert checkout_solution.checkout("PPPPPQQQ") == 280
        assert checkout_solution.checkout("RRRQQ") == 150 + 30
        assert checkout_solution.checkout("NNN") == 120
        assert checkout_solution.checkout("NNNM") == 120
        assert checkout_solution.checkout("NNNMM") == 120 + 15
        assert checkout_solution.checkout("HHHHHHHHHH") == 80
        assert checkout_solution.checkout("HHHHH") == 45
        assert checkout_solution.checkout("HHHHHH") == 55
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("KK") == 120
        assert checkout_solution.checkout("KKK") == 120 + 70
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40
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
        

        


