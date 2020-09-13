defmodule SumDivisibles do
  def sum(n) do
    n * (n + 1) / 2
  end

  def sum(n, divider) when is_integer(divider) do
    divider * sum(n / divider)
  end

  def sum(n, dividers) when is_list(dividers) do
    Enum.sum(for i <- 1..n, Enum.any?(dividers, fn d -> rem(i, d) == 0 end), do: i)
  end
end
