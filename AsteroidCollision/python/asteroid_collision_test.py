from AsteroidCollision.python.asteroid_collision import asteroidCollision

class TestAsteroidCollision:
    def test_small_incoming_vanishes(self):
        assert [5,10] == asteroidCollision([5,10,-5])

    def test_mutual_destruction(self):
        assert [] == asteroidCollision([8,-8])

    def test_neutral(self):
        assert [-8, 8] == asteroidCollision([-8,8])

    def test_incoming_too_big_then_too_small(self):
        assert [10] == asteroidCollision([10,2,-5])

    def test_not_incoming(self):
        assert [-5,-10,5] == asteroidCollision([-5,-10,5])

    def test_incoming_collides_then_harmonious(self):
        assert [-2,-2,-2] == asteroidCollision([-2,-2,1,-2])

    def test_collides_until_empty(self):
        assert [-2,-2,-2] == asteroidCollision([1,-2,-2,-2])
