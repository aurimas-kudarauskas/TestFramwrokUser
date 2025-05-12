from test_framework_base import TestFramewor
from test_framework_base.hardware.printers import Printer_I
import pytest

def test_something_with_printer():
    printer:Printer_I = TestFramewor.get_hardware_by_key("printer")
    printer.send_msg("Message from the test")
    assert True