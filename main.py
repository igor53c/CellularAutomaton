# test_cellular_automaton.py
import unittest
from CellularAutomatonImpl import CellularAutomatonImpl


class TestCellularAutomaton(unittest.TestCase):

    def test_has_rule(self):
        automaton = CellularAutomatonImpl(30)  # Index sa bitovima 1, 2, 3, 4 postavljenim
        self.assertFalse(automaton.has_rule(0))
        self.assertTrue(automaton.has_rule(1))
        self.assertTrue(automaton.has_rule(2))
        self.assertTrue(automaton.has_rule(3))
        self.assertTrue(automaton.has_rule(4))
        self.assertFalse(automaton.has_rule(5))
        self.assertFalse(automaton.has_rule(6))
        self.assertFalse(automaton.has_rule(7))

    def test_evolve(self):
        automaton = CellularAutomatonImpl(111, 25)
        automaton.preset(" ██ █  █ █   ██████████  ")
        automaton.evolve()
        expected_state = "█████ ████ ███        █ █".strip()
        self.assertEqual(automaton.state().strip(), expected_state)


if __name__ == '__main__':
    unittest.main()
