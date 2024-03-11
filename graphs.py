from elements_data import elements_data
from plotting import plot_molecule
import re

class Atom:
    def __init__(self, symbol, x, y, z):
        self.symbol = symbol
        self.x = x
        self.y = y
        self.z = z

#graph implemented using a dictionary
#keys are vertices (atoms), values are lists of adjacent vertices
class MolecularGraph:
    def __init__(self, name):
        self.name = name
        self.graph = {}
        self.atoms = []


    def add_atom(self, atom):
        #add a function that appends in order
        self.atoms.append((atom.symbol, (atom.x, atom.y, atom.z)))

    
    def add_bond(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)


    def print_graph(self):
        printed_bonds = set()
        sorted_atoms = sorted(self.atoms, key=lambda atom: atom[1][0])
    
        for vertex, _ in sorted_atoms:
            for neighbor in self.graph[vertex]:
                bond = tuple(sorted((vertex, neighbor)))
                if bond not in printed_bonds:
                    print(vertex, '->', neighbor)
                    printed_bonds.add(bond)


    def change_name(self, new_name):
        self.name = new_name


    def calculate_mol_mass(self):
        names = [atom[0] for atom in self.atoms]
        total_mass = 0
        pattern = re.compile(r'([a-zA-Z]{1,3})')
        
        for name in names:
            match = pattern.match(name)
            if match:
                symbol = match.group(1)
                if symbol in elements_data:
                    total_mass += elements_data[symbol][0]
                else:
                    print(f"Unknown element symbol: {symbol}")

        return total_mass
    
    
    def visualize(self):
        plot_molecule(self.atoms, self.graph)
        

        

db = []
molecule = MolecularGraph("alanine")
carbon = Atom("Hg1", -1, 0, -1)
carbon2 = Atom("C2", 0, 0, 1)
oxygen = Atom("O1", -2, 2, 0)
molecule.add_atom(carbon)
molecule.add_atom(carbon2)
molecule.add_atom(oxygen)
molecule.add_bond("C1", "C2")
molecule.add_bond("O1", "C1")
print(molecule.calculate_mol_mass())





