from graphs import MoleculeGraph, Atom
import math

def xyz_to_mol_graphs(path):

    molecules_db = xyz_reading(path)

    num_molecules = len(molecules_db)
    print(num_molecules, " molecules have been imported.")
    
    for molecule in molecules_db:
        atom_coords = molecules_db[molecule].atoms
        define_bonds(molecules_db, molecule, atom_coords)

        #if not checking_correct_bonds_num(atoms_all[i], mol_bonds):
        #    raise ValueError("The number of bonds exceeds the expected limit. Please adjust the bond lenght limit")
        
    return 

#assume atoms and coords are a list for one molecule
def define_bonds(molecules_db, molecule, atom_coords, max_bond_length=1.6):
    num_atoms = len(atom_coords)
    coords = [i[1] for i in atom_coords]
    atoms = [i[0] for i in atom_coords]

    for i in range(num_atoms):
        for j in range(i+1, num_atoms):
            dist = calculate_distance(coords[i], coords[j])
            if dist < max_bond_length:
                molecules_db[molecule].add_bond(atoms[i], atoms[j])

    print(molecules_db[molecule].graph)
    return 

def calculate_distance(coords1, coords2):
    return math.sqrt( sum( (float(coords1[k]) - float(coords2[k]))**2 for k in range(3) ))

#takes in a list of absolute paths
def xyz_reading(paths):

    #dictionary stores the names of all created objects (molecules)
    molecules_db = {}

    for file in paths:

        infile = open(file, 'r')
        name = file.split('/')[-1].split('.')[0]
        name_counter = 1
        present_atoms = {}

        for line in infile.readlines():
            elements = line.split()
            atom = elements[0]

            #an xyz file line containing only the number of atoms means a new molecule 
            if len(elements) == 1:
                present_atoms = {}

                temp_name = name+str(name_counter)
                name_counter += 1

                #create the molecule object and store it in a dictionary
                molecule = MoleculeGraph(temp_name)
                molecules_db[temp_name] = molecule
                
            #reads out the chemical composition of the molecule
            elif len(elements) == 4 and len(atom) == 1:

                if atom not in present_atoms:
                    present_atoms[atom] = 1

                atom_name = atom.capitalize()+str(present_atoms[atom])
                current_atom = Atom(atom_name, elements[1], elements[2], elements[3])
                molecule.add_atom(current_atom)
                present_atoms[atom] += 1
        
    return molecules_db

def checking_correct_bonds_num(atoms, bonds):
    num_bonds = len(bonds)
    #adjust the maximum number of bonds per atoms
    return True


file_path = ['/Users/ahryncyszyn/Desktop/molecular converter app/example_input/alanine.xyz', '/Users/ahryncyszyn/Desktop/molecular converter app/example_input/alanine2.xyz']
molecules_db = xyz_to_mol_graphs(file_path)

