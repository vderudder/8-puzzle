from puzzle8world import PuzzleEnvironment
from puzzle8world import update_zero


class TestMoveLeft:
    def test__move_left1(self):
        brd = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        expected_brd = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_left()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_left2(self):
        brd = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
        expected_brd = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_left()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_left3(self):
        brd = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
        expected_brd = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_left()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_left4(self):
        brd = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        expected_brd = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_left()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_left5(self):
        brd = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]
        expected_brd = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_left()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd


class TestMoveRight:
    def test__move_right1(self):
        brd = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        expected_brd = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_right()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_right2(self):
        brd = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
        expected_brd = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_right()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_right3(self):
        brd = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        expected_brd = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_right()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_right4(self):
        brd = [[1, 2, 0], [3, 4, 5], [6, 7, 8]]
        expected_brd = [[1, 2, 0], [3, 4, 5], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_right()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_right5(self):
        brd = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]
        expected_brd = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_right()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd


class TestMoveUp:
    def test__move_up1(self):
        brd = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
        expected_brd = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_up()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_up2(self):
        brd = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]
        expected_brd = [[0, 2, 3], [1, 4, 5], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_up()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_up3(self):
        brd = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
        expected_brd = [[1, 2, 0], [4, 5, 3], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_up()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_up4(self):
        brd = [[1, 2, 0], [3, 4, 5], [6, 7, 8]]
        expected_brd = [[1, 2, 0], [3, 4, 5], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_up()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_up5(self):
        brd = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        expected_brd = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_up()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd


class TestMoveDown:
    def test__move_down1(self):
        brd = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
        expected_brd = [[1, 4, 2], [3, 0, 5], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_down()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_down2(self):
        brd = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]
        expected_brd = [[1, 2, 3], [6, 4, 5], [0, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_down()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_down3(self):
        brd = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
        expected_brd = [[1, 2, 3], [4, 5, 8], [6, 7, 0]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_down()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_down4(self):
        brd = [[1, 2, 0], [3, 4, 5], [6, 7, 8]]
        expected_brd = [[1, 2, 5], [3, 4, 0], [6, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_down()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_down5(self):
        brd = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
        expected_brd = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_down()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd

    def test__move_down6(self):
        brd = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        expected_brd = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

        puzzle = PuzzleEnvironment(brd, 3)
        puzzle._move_down()
        actual_brd = puzzle._board

        assert expected_brd == actual_brd


class TestUpdateZero:
    def test_update_zero_1(self):
        board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        expected = [0, 0]

        actual = update_zero(board)

        assert expected == actual

    def test_update_zero_2(self):
        board = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
        expected = [0, 1]

        actual = update_zero(board)

        assert expected == actual

    def test_update_zero_3(self):
        board = [[1, 2, 0], [3, 4, 5], [6, 7, 8]]
        expected = [0, 2]

        actual = update_zero(board)

        assert expected == actual

    def test_update_zero_4(self):
        board = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]
        expected = [1, 0]

        actual = update_zero(board)

        assert expected == actual

    def test_update_zero_5(self):
        board = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        expected = [1, 1]

        actual = update_zero(board)

        assert expected == actual

    def test_update_zero_6(self):
        board = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
        expected = [1, 2]

        actual = update_zero(board)

        assert expected == actual

    def test_update_zero_7(self):
        board = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
        expected = [2, 0]

        actual = update_zero(board)

        assert expected == actual

    def test_update_zero_8(self):
        board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        expected = [2, 1]

        actual = update_zero(board)

        assert expected == actual

    def test_update_zero_9(self):
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        expected = [2, 2]

        actual = update_zero(board)

        assert expected == actual


moveLeft = TestMoveLeft()

moveLeft.test__move_left1()
moveLeft.test__move_left2()
moveLeft.test__move_left3()
moveLeft.test__move_left4()
moveLeft.test__move_left5()

moveRight = TestMoveRight()

moveRight.test__move_right1()
moveRight.test__move_right2()
moveRight.test__move_right3()
moveRight.test__move_right4()
moveRight.test__move_right5()

moveUp = TestMoveUp()

moveUp.test__move_up1()
moveUp.test__move_up2()
moveUp.test__move_up3()
moveUp.test__move_up4()
moveUp.test__move_up5()

moveDown = TestMoveDown()

moveDown.test__move_down1()
moveDown.test__move_down2()
moveDown.test__move_down3()
moveDown.test__move_down4()
moveDown.test__move_down5()

update = TestUpdateZero()

update.test_update_zero_1()
update.test_update_zero_2()
update.test_update_zero_3()
update.test_update_zero_4()
update.test_update_zero_5()
update.test_update_zero_6()
update.test_update_zero_7()
update.test_update_zero_8()
update.test_update_zero_9()
