#implemented using dictionary
#keys are vertices, values are lists of adjacent vertices
class Atom:
    def __init__(self, symbol, x, y, z):
        self.symbol = symbol
        self.x = x
        self.y = y
        self.z = z

class MoleculeGraph:
    def __init__(self, name):
        self.name = name
        self.atoms = []
        self.graph = {}

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

db = []
molecule = MoleculeGraph("alanine")
carbon = Atom("C1", -1, 0, -1)
carbon2 = Atom("C2", 0, 0, 1)
oxygen = Atom("O1", -2, 2, 0)
molecule.add_atom(carbon)
molecule.add_atom(carbon2)
molecule.add_atom(oxygen)
molecule.add_bond("C1", "C2")
molecule.add_bond("O1", "C1")
molecule.print_graph()





