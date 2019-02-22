# https://pubchem.ncbi.nlm.nih.gov/omssa/
# Command to run omssa searches, looking for b,y ions with some fixed and variable modifications
# CA2.fasta is the database made using blastdb from ncbi toolkit and with a sample dta file
# The output is the omssa_sample.csv that has the list of peptide spectral matches for a cut-off
omssacl -i 1,4 -mf 3 -mv 1 -f MSHHWGYGK.dta -d CA2.fasta -oc omssa_sample.csv