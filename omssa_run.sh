# https://pubchem.ncbi.nlm.nih.gov/omssa/
# Command to run omssa searches, looking for b,y ions with some fixed and variable modifications
# The database made using blastdb from ncbi toolkit and with a sample dta file
# The output is with an added n-term acetylation to look for.

# Second omssa run (fixed carbamidomethylation and variable methionine oxidation and variable n-term acetylation)
omssacl -i 1,4 -mf 3 -mv 1 -fm Input\\Input.mgf -d blastDb\\Input.fasta -oc Output\\output_run.csv
