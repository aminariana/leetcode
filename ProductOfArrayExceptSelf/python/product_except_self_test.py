from ProductOfArrayExceptSelf.python.product_except_self import productExceptSelf

class TestProductExceptSelf:
    def test_simple(self):
        assert [24,12,8,6] == productExceptSelf([1,2,3,4])
            
    def test_with_negatives(self):
        assert [0,0,9,0,0] == productExceptSelf([-1,1,0,-3,3])
