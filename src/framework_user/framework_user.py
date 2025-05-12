from test_framework_base.hardware.printers.vendorA import DeviceAYZ
#from test_framework_base.hardware.printers.vendorB import DeviceXXA
from test_framework_base import TestFramewor
# setup hardware for tests

class UserFramework:
    def run():
        #setattr(TestFramewor, "__test__", False)
        printer = DeviceAYZ("Time xxx:") #Can initialize and call any device specific method that was wrapped arround
        #printer = DeviceXXA()
        hw_context = {"printer":printer}

        test_runner = TestFramewor("src/framework_user/tests/")
        TestFramewor.set_hw_context(hw_context)
        # run tests
        test_runner.run_tests(["-s"])
        # generate reporsts
        # test_runner.report()
