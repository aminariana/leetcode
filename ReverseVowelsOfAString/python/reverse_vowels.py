def reverseVowels(s: str) -> str:
    vowels = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' }
    input = [*s]
    left, right = 0, len(input) - 1
    while left < right:
        while (input[left] not in vowels) and left < right:
            left += 1
        while (input[right] not in vowels) and left < right:
            right -= 1
        if left == right:
            break
        # both are on vowels, swap
        input[left], input[right] = input[right], input[left]
        # and move on
        left += 1
        right -= 1
    return ''.join(input)
