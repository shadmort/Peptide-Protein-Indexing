import requests
import pandas as pd

class PPI:
    attribute = 'Index an AA sequence detected in MS to a protein sequence.'

    def __init__(self, df, acc_id):
        self.df = df
        self.id = acc_ID

    def AA_sequence(acc_id):
        """
        Retrieves the protein sequence for a UniProt ID:
    
        Parameters:
        acc_id: the UniProt Accession ID
    
        Returns:
        str: the amino acid sequence
        """
        url = f'https://www.uniprot.org/uniprot/{acc_id}.fasta'
        response = requests.get(url)
    
        if response.status_code == 200:
            fasta_data = response.text
            sequence = ''.join(fasta_data.split('\n')[1:])
            return sequence
        else:
            print(f'Failed to retrieve data for {acc_id}')

    def ppi(df, acc_id):
        """
        Perfroms the peptide-protein indexing in one step:

        Parameters:
        df: dataframe containing the AA seqences with protein accession in 'Master Protein Accesssions' column
        acc_id: the Uniprot Accession ID

        Returns:
        list: list of AA seqence and position in sequence
        """

        def printIndex(p_string, aa_seq):
        """
        Prints [AA]: [Position]

        Parameters:
        p_string: the protein sequence as a string
        aa_sequence: the MS-identified AA sequence

        Returns:
        list: a list of 
        """
 
        flag = False
        for i in range(len(p_string)):
            if (p_string[i:i + len(aa_seq)] == aa_seq):
                foo = i+1
                bar = i+len(aa_seq)
                return(f'{aa_seq}: {foo}-{bar}')
                flag = True
     
        if (flag == False):
            print("NONE")
            
        protein_df = df[df['Master Protein Accessions'] == acc_id]
        pset = set(protein_df['Annotated Sequence'].to_list())
        trimmed = []
        [trimmed.append(x[4:-4]) for x in pset]
        res = []
        [res.append(x.upper()) for x in trimmed]
        indexList = []
        [indexList.append(printIndex(prot, x)) for x in res3]
        return(indexList)
        print(indexList)
        
# Driver
bmc = 'P13796'
sequence = PPI.AA_sequence(bmc)
PPI_df = PPI.ppi(df, bmc)
PPI_df = pd.DataFrame(PPI_df)
PPI_df[0].str.split(':', expand=True).rename(columns={0: 'Peptide', 1: 'Start-End'})
PPI_df[0].str.split(':', expand=True).rename(columns={0: 'Peptide', 1: 'Start-End'}).to_csv(f'{bmc}_peptide-protein-index.csv')
