import re


# Note: this implementation does simple "+" operation resolution on a spreadsheets
# and does cycle detections. But more sophisticated formulae were out of scope
# due to time constraints.
class Spreadsheet:
    def __init__(self, raw: list[list[int]]) -> None:
        self.raw = raw
        self.cache = {}

    def evaluate_cell(self, label: str) -> int:
        row, col = self.get_coordinates(label)
        print(f"coordinates of {label}: {(row, col)}")
        visited = set()
        stack = [label]
        print(f"Stack initial: {stack}")
        result = 0
        if label not in self.cache:
            while len(stack):
                print(f"while {stack}")
                current = stack.pop()
                print(f"popped {current}")
                if current.isdigit():
                    result += int(current)
                elif current in ["+", "-"]:
                    print(f"Operation {current}")
                elif current.find('+') >= 0:
                    for thing in current.split(' '):
                        stack.append(thing)
                    print(f"Addition formula stacked: {stack}")
                elif self.is_coordinates(current):
                    if current in visited:
                        raise RuntimeError(f"cycle detected at {current}")
                    row, col = self.get_coordinates(current)
                    print(f"Reference stacked: {stack}")
                    visited.add(current)
                    stack.append(self.raw[row][col])
                else:
                    raise ValueError(f"Formula stack trace: {stack}, current: {current}")
            self.cache[label] = result
        return self.cache[label]

    def get_coordinates(self, label: str) -> tuple[int, int]:
        row = 0
        col = 0
        for c in label:
            if c.isdigit():
                row = row * 10 + (int(c) - 1)
            else:
                col = col * 26 + (ord(c) - ord('A'))
        return (row, col)

    def is_coordinates(self, label) -> bool:
        return re.match(r'^[A-Z]+[1-9][0-9]*$', label)



def main():
    sheet = Spreadsheet([["1 + 2"]])
    assert 3 == sheet.evaluate_cell("A1")

if __name__ == "__main__":
    main()
