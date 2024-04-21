from EvaluateDivision.python.calc_equation import calcEquation

class TestCalcEquation:
    def test_deep(self):
        assert [6.00000,0.50000,-1.00000,1.00000,-1.00000] == calcEquation(
            equations=[["a","b"],["b","c"]],
            values=[2.0,3.0],
            queries=[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        )

    def test_two_letters(self):
        assert [3.75000,0.40000,5.00000,0.20000] == calcEquation(
            equations=[["a","b"],["b","c"],["bc","cd"]],
            values=[1.5,2.5,5.0],
            queries=[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
        )

    def test_out_of_range(self):
        assert [0.50000,2.00000,-1.00000,-1.00000] == calcEquation(
            equations=[["a","b"]],
            values=[0.5],
            queries=[["a","b"],["b","a"],["a","c"],["x","y"]]
        )
