import random


class CellularAutomatonImpl:
    def __init__(self, index: int, width: int = 10) -> None:
        """
        Constructs a cellular automaton based on the index
        of the Wolfram Code using a given width for the number of cells.
        :param index: 8 bit representing the index of the automaton
        :param width: number of cells
        """
        self.cells = []
        self.index = index
        self.width = max(10, width)
        self.randomize()

    def randomize(self) -> None:
        """
        Generates a random state with the specified number of cells.
        """
        self.cells = []
        r = random.getrandbits(self.width)
        while r > 0:
            self.cells.append(r % 2 == 1)
            r = r >> 1

    def preset(self, s: str) -> None:
        """
        Sets the current state to a given string.
        A blank character represents the state false,
        otherwise true
        :param s: string representing the state
        """
        self.width = max(self.width, len(s))
        self.cells = []
        for x in s:
            self.cells.append(x != " ")

    def get_cell(self, i: int) -> int:
        """
        Provides the current state of the i-th cell
        :param i: number of the cell
        :return: state of the i-th cell 0 or 1
        """
        if 0 <= i < len(self.cells):
            return self.cells[i]
        return 0

    def has_rule(self, i: int) -> bool:
        """
        Calculates whether the i-th bit for rule i in the
        index of the automaton is set.
        :param i: number of the rule/bit
        :return: true when the i-th bit of the binary index is 1
        """
        # TODO scenario 1
        return (self.index >> i) & 1 == 1

    def evolve(self) -> None:
        """
        Calculates the next state for each cell based on the
        current own state and the neighbors.
        """
        # TODO scenario 2
        new_cells = [False] * self.width

        for i in range(self.width):
            left = self.get_cell(i - 1)
            center = self.get_cell(i)
            right = self.get_cell(i + 1)
            rule_index = (left << 2) | (center << 1) | right
            new_cells[i] = (self.index >> rule_index) & 1 == 1
        self.cells = new_cells

    def run(self, n: int) -> None:
        """
        Evolves the automaton n times and prints the state
        of all cells each time.
        :param n: number of evolutions
        """
        for i in range(n):
            self.evolve()
            print(self.state())

    def get_rule_set(self) -> set:
        """
        Provides the set of rules as numbers represented
        by the index of the automaton
        :return: the set of rules as numbers
        """
        rules = set()
        for i in range(8):
            if self.has_rule(i):
                rules.add(i)
        return rules

    def state(self) -> str:
        """
        Provides the current state of each cell as a string.
        :return: the state as a string
        """
        s = ""
        for b in self.cells:
            if b:
                s += "█"
            else:
                s += " "
        return s
