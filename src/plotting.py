import matplotlib.pyplot as plt
import re
from utils.molecular_data import molecular_data

def plot_molecule(atoms, bonds):
    '''
    creates a 3D plot of the molecule
    :atoms: list of tuples containing atom names and its corresponding coordinates
    :bonds: dictionary containing each atom as a key and its neighbours as values
    '''
    
    num_atoms = len(atoms)
    atom_types = [re.search(r'[A-Za-z]{1,2}', atom[0]).group(0) for atom in atoms]
    color_map = {'C': 'grey', 'H': 'white', 'N': 'blue', 'O': 'red', 'Cl': 'green', 'F': 'green', 'Br': 'brown', 'I': 'purple', 'S': 'yellow', 'P': 'orange'}

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.grid(True, which='both',linestyle='-', linewidth=0.5, color='grey', alpha=0.01)

    #plot atoms as scatter points
    for i, atom in enumerate(atoms):
        
        if atom_types[i] in molecular_data:
            element_name = molecular_data[atom_types[i]][1]
        else:
            element_name = atom_types[i]

        ax.scatter(atom[1][0], atom[1][1], atom[1][2], 
                label=element_name, 
                color=color_map.get(atom_types[i], 'black'), 
                edgecolors='black', s=250, alpha=0.5)
        
        ax.text(atom[1][0], atom[1][1], atom[1][2], atom[0], 
                color='black', 
                fontsize=10)
        
    #plot bonds between atoms
    atoms_dict = dict(atoms)
    for atom1_label, connected_atoms in bonds.items():
        for atom2_label in connected_atoms:
            atom1_coord = atoms_dict[atom1_label]
            atom2_coord = atoms_dict[atom2_label]
            ax.plot([atom1_coord[0], atom2_coord[0]], 
                    [atom1_coord[1], atom2_coord[1]],
                    [atom1_coord[2], atom2_coord[2]],
                    color='black')

    #sets labels
    ax.set_xlabel('X'), ax.set_ylabel('Y'), ax.set_zlabel('Z')

    #adds legend of unique molecules
    handles, labels = ax.get_legend_handles_labels()
    handle_list, label_list = [], []
    for handle, label in zip(handles, labels):
        if label not in label_list:
            handle_list.append(handle)
            label_list.append(label)
    plt.legend(handle_list, label_list, markerscale = 0.5)
    
    plt.show()
