from unittest import TestCase

from tlaplus_kernel.kernel import TLARunner

class TestExpressions(TestCase):

    def test_set(self):
        tr = TLARunner()
        res = tr.run_expr('{e \in ( (1..3)\X(1..3) ): e[1] <= e[2]}')
        expected = '{<<1, 1>>, <<1, 2>>, <<1, 3>>, <<2, 2>>, <<2, 3>>, <<3, 3>>}'
        self.assertEqual(res, expected)

    def test_error(self):
        tr = TLARunner()
        res = tr.run_expr('!!!')
        self.assertTrue("Parse Error" in res)