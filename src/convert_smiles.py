from rdkit import Chem

def smiles_to_inchikey(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    inchi_key = Chem.MolToInchiKey(mol)
    return inchi_key