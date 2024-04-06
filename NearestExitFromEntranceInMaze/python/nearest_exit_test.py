from NearestExitFromEntranceInMaze.python.nearest_exit import nearestExit

class TestNearestExit:
    def test_pick_nearest(self):
        maze = [
            ["+","+",".","+"],
            [".",".",".","+"],
            ["+","+","+","."]]
        assert 1 == nearestExit(maze, [1,2])

    def test_across(self):
        maze = [
            ["+","+","+"],
            [".",".","."],
            ["+","+","+"]]
        assert 2 == nearestExit(maze, [1,0])

    def test_exclude_self(self):
        maze = [[".","+"]]
        assert -1 == nearestExit(maze, [0,0])

    def test_huge(self):
        top = ["+"] * 100
        mid = ["+"] + ["."] * 98 + ["+"]
        maze = []
        maze.append(top)
        for _ in range(98):
            maze.append(mid.copy())
        maze.append(top.copy())
        assert -1 == nearestExit(maze, [42,4])

    def test_exit_far_from_wall_entrance(self):
        maze = [
            ["+",".","+","+","+","+","+"],
            ["+",".","+",".",".",".","+"],
            ["+",".","+",".","+",".","+"],
            ["+",".",".",".","+",".","+"],
            ["+","+","+","+","+",".","+"]]
        assert 12 == nearestExit(maze, [0,1])
