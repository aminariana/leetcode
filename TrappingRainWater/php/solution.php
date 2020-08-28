<?php
function trap($height)
{
    $trapped = 0;
    $l = 0;
    $r = count($height) - 1;
    $watermark = 0;
    while ($l <= $r) {
        if ($height[$l] <= $height[$r]) {
            $watermark = max($watermark, $height[$l]);
            $trapped += $watermark - $height[$l++];
        } else {
            $watermark = max($watermark, $height[$r]);
            $trapped += $watermark - $height[$r--];
        }
    }
    return $trapped;
}
