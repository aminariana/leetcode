from OnlineStockSpan.python.stock_spanner import StockSpanner

class TestStockSpanner:
    def test_spanner(self):
        spanner = StockSpanner()
        inputs = [100, 80, 60, 70, 60, 75, 85]
        outputs = list(map(lambda price: spanner.next(price), inputs))
        assert [1, 1, 1, 2, 1, 4, 6] == outputs
