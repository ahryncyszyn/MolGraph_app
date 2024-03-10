#from graphs import MoleculeGraph
import math
import os
import shutil

def xyz_to_mol_graphs(path):

    names_all, atoms_all, coords_all = xyz_reading(path)

    #sanity check
    #assert len(atoms) == len(coords), 'numbers of atoms and coordinate sets do not agree'

    num_molecules = len(atoms_all)
    print(atoms_all)
    print(atoms_all[0])
    bonds_all = []
    
    for i in range(num_molecules):
        mol_bonds = find_bonds(atoms_all[i], coords_all[i])

        if not checking_correct_bonds_num(atoms_all[i], mol_bonds):
            raise ValueError("The number of bonds exceeds the expected limit. Please adjust the bond lenght limit")
        else:
            bonds_all.append([mol_bonds])



    return names_all, atoms_all, bonds_all


def xyz_reading(paths):

    #list of lists to store coordinates and atoms of molecules
    names, coords, atoms = [], [[]], [[]]
    #name = 
    present_atoms = {}

    for file in paths:

        infile = open(file, 'r')
        name = file.split('/')[-1].split('.')[0]
        names.append(name)
        name_counter = 1

        for line in infile.readlines():
            elements = line.split()
            atom = elements[0]

            #new molecule is going to be stored in a new list 
            if len(elements) == 1 and len(coords[-1]) != 0:
                coords.append([])
                atoms.append([])
                present_atoms = {}

                names.append(name+str(name_counter))
                name_counter += 1
                
            #reads out the chemical composition of the molecule
            elif len(elements) == 4 and len(atom) == 1:

                if atom not in present_atoms:
                    present_atoms[atom] = 1

                atoms[-1].append(elements[0].capitalize()+str(present_atoms[atom]))
                coords[-1].append( [float(elements[i]) for i in range(1,4)] )

                present_atoms[atom] += 1
        
        infile.close()


    #for each molecule i, j atom's coordinates are atoms[i][j], coords[i][j]
    return names, atoms, coords

#assume atoms and coords are a list for one molecule
def find_bonds(atoms, coords, max_bond_length=1.6):
    bonds = []
    num_atoms = len(atoms)
    print(num_atoms)
    print(atoms)
    for i in range(num_atoms):
        for j in range(i+1, num_atoms):
            print("calculation for ", i, j)
            dist = calculate_distance(coords[i], coords[j])
            if dist < max_bond_length:
                bonds.append((atoms[i], atoms[j]))
    return bonds

def calculate_distance(coords1, coords2):
    return math.sqrt( sum( (coords1[k] - coords2[k])**2 for k in range(3) ))

def convert_to_graph():
    pass

def checking_correct_bonds_num(atoms, bonds):
    num_bonds = len(bonds)
    #adjust the maximum number of bonds per atoms
    return True

#paths = ['/Users/ahryncyszyn/Desktop/molecularviz_project/alanine2.xyz']
#path1 = paths[0]
print("-----------------")
#atoms, coordinates = xyz_reading(path1)
#mol_coordinates = coordinates[0]
#print(atoms[0])
#print(mol_coordinates[0])
#print(mol_coordinates[0][1])

#test = xyz_to_mol_graphs('singl', 'alanine.xyz')
#print(test[0])

file_path = '/Users/ahryncyszyn/Desktop/molecularviz_project/alanine.xyz'
file_name = file_path.split('/')[-1].split('.')[0]
print(file_name)
tescik = open(file_path, 'r')
