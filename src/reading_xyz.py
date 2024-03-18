from src.graphs import MolecularGraph, Atom
import math

def xyz_to_mol_graphs(path):
    '''
    creates a database of molecular graphs
    :path: a list of absolute paths to the input file(s)
    :return: a dictionary containing the name of the molecule as key
             and the graph object of that molecule as a value
    '''

    molecules_db = xyz_reading(path)

    num_molecules = len(molecules_db)
    print(num_molecules, " molecule(s) have been imported.")
    
    for molecule in molecules_db:
        atom_coords = molecules_db[molecule].atoms
        define_bonds(molecules_db, molecule, atom_coords)

    return molecules_db


def xyz_reading(paths):
    '''
    converts the .xyz file(s) into a MolecularGraph object for each molecule
    accounts for the cases where one file contains multiple molecules
    :paths: a list of absolute paths to the .xyz file(s)
    '''

    #dictionary stores the names of all created objects (molecules)
    molecules_db = {}

    for file in paths:

        infile = open(file, 'r')
        name = file.split('/')[-1].split('.')[0]
        name_counter = 1
        present_atoms = {}

        for line in infile.readlines():
            elements = line.split()
            if len(elements) >= 1:
                atom = elements[0]

            #an xyz file line containing only the number of atoms means a new molecule 
            if len(elements) == 1 and str(elements[0]).isnumeric():
                present_atoms = {}
                
                #add numbers to the name only if there are more than one molecule in a file
                temp_name = name if name_counter==1 else name+str(name_counter)
                name_counter += 1

                #create the molecule object and store it in a dictionary
                molecule = MolecularGraph(temp_name)
                molecules_db[temp_name] = molecule
                
            #reads out the chemical composition of the molecule
            elif len(elements) == 4 and len(atom) == 1:

                if atom not in present_atoms:
                    present_atoms[atom] = 1

                atom_name = atom.capitalize()+str(present_atoms[atom])
                current_atom = Atom(atom_name, float(elements[1]), float(elements[2]), float(elements[3]))
                molecule.add_atom(current_atom)
                present_atoms[atom] += 1

        infile.close()

    if len(molecules_db) == 0:
        raise ValueError(f'Selected files did not contain any molecules! Please keep in mind that only .xyz files are supported.')
        
    return molecules_db


#assume atoms and coords are a list for one molecule
def define_bonds(molecules_db, molecule, atom_coords, max_bond_length=1.6):
    ''' 
    finds bonds based on the max_bond_length threshold and adds them to the graph object
    :molecules_db: dictionary storing the molecular graph objects and their names as keys
    :molecule: the name of the molecule, key to the molecules_db
    :atom_coords: the .atom attribute of MoleculeGraph object, 
                  a list of tuples containing the atom and its coordinates 
    '''
    num_atoms = len(atom_coords)
    coords = [i[1] for i in atom_coords]
    atoms = [i[0] for i in atom_coords]

    for i in range(num_atoms):
        for j in range(i+1, num_atoms):
            dist = calculate_distance(coords[i], coords[j])
            if dist < max_bond_length:
                molecules_db[molecule].add_bond(atoms[i], atoms[j])

    return 


def calculate_distance(coords1, coords2):
    ''' 
    calculates the 3D Euclidean distance between two atoms
    :coords1: coordinates in 3D of the first atom
    :coords2: coordinates in 3D of the second atom
    '''
    return math.sqrt( sum( (float(coords1[k]) - float(coords2[k]))**2 for k in range(3) ))