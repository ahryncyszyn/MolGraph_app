from utils.molecular_data import molecular_data
from src.plotting import plot_molecule
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

    def __str__(self):
        no_bonds = int(0.5*sum(len(value) for value in self.graph.values()))
        return f"{self.name} molecule, with {len(self.atoms)} atoms and {no_bonds} single bonds"

    def add_atom(self, atom):
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
                if symbol in molecular_data:
                    total_mass += molecular_data[symbol][0]
                else:
                    print(f"Unknown element symbol: {symbol}")

        return total_mass
    
    def plot_molecule(self):
        plot_molecule(self.atoms, self.graph)






