Code.require_file("./solution.exs")

ExUnit.start()

defmodule SumDivisiblesTest do
  use ExUnit.Case

  test "sum up to 10" do
    assert 55 == SumDivisibles.sum(10)
  end

  test "sum up to 97" do
    assert 4753 == SumDivisibles.sum(97)
  end

  test "sum multiples of 3 up to 12" do
    assert 30 == SumDivisibles.sum(12, 3)
  end

  test "sum multiples of 3 or 5 up to 15" do
    assert 60 == SumDivisibles.sum(15, [3, 5])
  end

  test "sum multiples of 3 or 5 or 7 or 44 up to 1000" do
    assert 277_038 == SumDivisibles.sum(1000, [3, 5, 7, 44])
  end
end
