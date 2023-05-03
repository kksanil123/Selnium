import unittest

from Zee5.signup.signup import SignUp
from Zee5.signin.signin import Signin

tc1 = unittest.TestLoader().loadTestsFromTestCase(SignUp)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Signin)

ts1 = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(test=ts1)

# if __name__ == "__main__":
#     unittest.main()
# else:
#     print(f"This module is running with __name__ : {__name__}")
