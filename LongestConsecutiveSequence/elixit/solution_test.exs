Code.require_file("./solution.exs")

ExUnit.start()

defmodule LongestConsecutiveSequenceTest do
  use ExUnit.Case

  test "empty" do
    assert 0 == LongestConsecutiveSequence.longestConsecutive([])
  end

  test "unordered" do
    assert 4 == LongestConsecutiveSequence.longestConsecutive([100, 4, 200, 1, 3, 2])
  end
end
