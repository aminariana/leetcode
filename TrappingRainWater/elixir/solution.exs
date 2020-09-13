defmodule TrappingRainWater do
  def trap(height, watermark \\ 0, trapped \\ 0)

  def trap(height, _watermark, trapped) when height == [] do
    trapped
  end

  def trap(height, watermark, trapped) do
    [first | tail] = height
    last = List.last(height)

    if first > last do
      trap(Enum.reverse(height), watermark, trapped)
    else
      watermark = max(watermark, first)
      trap(tail, watermark, trapped + watermark - first)
    end
  end
end
