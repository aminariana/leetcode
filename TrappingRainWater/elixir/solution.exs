defmodule TrappingRainWater do
  def trap(height) do
    trap(height, 0, 0)
  end

  def trap(height, watermark, trapped) do
    case height == [] do
      false ->
        [first|tail] = height
        last = List.last(height)
        if first > last do
          trap(Enum.reverse(height), watermark, trapped)
        else
          watermark = max(watermark, first)
          trap(tail, watermark, trapped + watermark - first)
        end
      true -> trapped
    end
  end
end
