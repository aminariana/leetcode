def decodeString(s: str) -> str:
    stack = []
    for c in s:
        if c == ']':
            content = []
            while len(stack) and (pop := stack.pop()) != '[':
                content.insert(0, pop)
            for count in range(int(stack.pop())):
                stack.extend(content)
        elif c.isdigit():
            if len(stack) and stack[-1].isnumeric():
                c = int(stack.pop()) * 10 + int(c)
            stack.append(str(c))
        else:
            stack.append(c)
    return ''.join(stack)
