from unittest import TestCase

from PrimeFactor import PrimeFactor, I_PrimeFactor


class TestPrimeFactor(TestCase):
    def test_case1(self):
        pf = PrimeFactor()
        if not isinstance(pf,I_PrimeFactor):
            self.assertFalse()
        self.assertEqual([],pf.run(1))

    def test_case2(self):
        pf = PrimeFactor()
        if not isinstance(pf,I_PrimeFactor):
            self.assertFalse()
        self.assertEqual([2],pf.run(2))

    def test_case3(self):
        pf = PrimeFactor()
        if not isinstance(pf,I_PrimeFactor):
            self.assertFalse()
        self.assertEqual([3],pf.run(3))
    def test_case4(self):
        pf = PrimeFactor()
        if not isinstance(pf,I_PrimeFactor):
            self.assertFalse()
        self.assertEqual([2,2],pf.run(4))

    def test_case5(self):
        pf = PrimeFactor()
        if not isinstance(pf,I_PrimeFactor):
            self.assertFalse()
        self.assertEqual([5],pf.run(5))
