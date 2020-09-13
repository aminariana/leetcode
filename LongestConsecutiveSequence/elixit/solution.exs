# TODO: Warning (aminariana) -- the following code does not do correct memoization.
# Due to immutability in Elixir, I still need to figure out how to mutate memo between recursions.

defmodule LongestConsecutiveSequence do
  def longestConsecutive(nums) when nums == nil or nums == [] do
    0
  end

  def longestConsecutive(nums) do
    memo = Enum.reduce(nums, %{}, fn n, m -> Map.put(m, n, 0) end)

    nums
    |> Enum.map(fn n -> dfs(n, memo) end)
    |> Enum.max()
  end

  defp dfs(v, memo) do
    if !Map.has_key?(memo, v), do: 0, else: 1 + dfs(v + 1, memo)
  end
end
