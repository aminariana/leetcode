Code.require_file("./solution.exs")

ExUnit.start

defmodule TrappingRainWaterTest do
  use ExUnit.Case

  test "empty" do
    assert 0 == TrappingRainWater.trap([])
  end

  test "hill" do
    assert 0 == TrappingRainWater.trap([0, 1, 2, 1, 0])
  end

  test "bowl" do
    assert 4 == TrappingRainWater.trap([2, 1, 0, 1, 2])
  end

  test "normal" do
    assert 6 == TrappingRainWater.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
  end
end
