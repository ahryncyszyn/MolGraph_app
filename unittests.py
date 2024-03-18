import unittest
import copy

from src.reading_xyz import *
from src.graphs import *
from src.plotting import *

class TestMolImporting(unittest.TestCase):
    
    def test_empty_file(self):
        path = ['example_input/for_testing/empty.xyz']
        with self.assertRaises(ValueError):
            test_db = xyz_to_mol_graphs(path)

    def test_importing_two_files(self):
        path = ['example_input/alanine.xyz', 'example_input/caffeine.xyz']
        test_db = xyz_to_mol_graphs(path)
        self.assertEqual(len(test_db), 2)

    def test_importing_one_file_with_three_molecules(self):
        path = ['example_input/for_testing/hydrocarbons.xyz']
        test_db = xyz_to_mol_graphs(path)
        self.assertEqual(len(test_db), 3)

class TestGrapConversion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = ['example_input/alanine.xyz']
        test_db = xyz_to_mol_graphs(path)
        cls.alanine = test_db['alanine']
        cls.alanine_copy = copy.deepcopy(cls.alanine)

    def test_atoms_number(self):
        self.assertEqual(len(self.alanine.atoms), 13)

    def test_bonds_number(self):
        no_bonds = int(0.5*sum(len(value) for value in self.alanine.graph.values()))
        self.assertEqual(no_bonds, 12)

    def test_adding_atom(self):
        proton = Atom('H8', 1.99536, 1.35685, -0.54570)
        self.alanine_copy.add_atom(proton)
        self.assertEqual(len(self.alanine_copy.atoms), 14)

    def test_adding_bond(self):
        self.alanine_copy.add_bond('H8', 'N1')
        no_bonds = int(0.5*sum(len(value) for value in self.alanine_copy.graph.values()))
        self.assertEqual(no_bonds, 13)


if __name__ == '__main__':
    unittest.main()