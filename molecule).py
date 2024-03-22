def count_atoms(molecule):
    atoms = {}
    current_atom = ''
    current_count = ''
    
    for char in molecule:
        if char.isupper():
            if current_atom:
                atoms[current_atom] = atoms.get(current_atom, 0) + (int(current_count) if current_count else 1)
            current_atom = char
            current_count = ''
        elif char.islower():
            current_atom += char
        elif char.isdigit():
            current_count += char
    
    # Add the last atom
    if current_atom:
        atoms[current_atom] = atoms.get(current_atom, 0) + (int(current_count) if current_count else 1)
    
    return atoms

molecule = "H2O"
print("Molecule:", molecule)
print("Count of atoms:", count_atoms(molecule))
