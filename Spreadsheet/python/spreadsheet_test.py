from Spreadsheet.python.spreadsheet import Spreadsheet

class TestSpreadsheet:
    # def test_simple_cell_digit(self):
    #     sheet = Spreadsheet([[1]])
    #     assert 1 == sheet.evaluate_cell("A1")

    def test_simple_cell_digit_as_string(self):
        sheet = Spreadsheet([["1"]])
        assert 1 == sheet.evaluate_cell("A1")

    def test_simple_grid(self):
        sheet = Spreadsheet([["1", "2"], ["3", "4"]])
        assert 1 == sheet.evaluate_cell("A1")
        assert 2 == sheet.evaluate_cell("B1")
        assert 3 == sheet.evaluate_cell("A2")
        assert 4 == sheet.evaluate_cell("B2")

    def test_formula_cell_no_reference(self):
        sheet = Spreadsheet([["1 + 2"]])
        assert 3 == sheet.evaluate_cell("A1")

    def test_formula_cell_simple_reference(self):
        sheet = Spreadsheet([["B1 + 20", "10"]])
        assert 30 == sheet.evaluate_cell("A1")

    def test_formula_cell_cycle(self):
        sheet = Spreadsheet([["B1", "A1"]])
        try:
            sheet.evaluate_cell("A1")
            assert False
        except RuntimeError as err:
            assert str(err) == "cycle detected at A1"

