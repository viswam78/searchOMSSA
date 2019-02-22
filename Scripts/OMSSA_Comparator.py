#########################
# Github repo for README on this: https://github.com/viswam78/OMSSA_Searches
########################

# Import modules

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Input: omssacsv files, fdr range
# Results in ROC curve


def main():
    """
    Usage: python OMSSA_Comparator.py <path to omssa csv file 1> <path to omssa csv file 2>
    """

    parser = argparse.ArgumentParser(
        description='Usage: python OMSSA_Comparator.py <path to omssa csv file 1> <path to omssa csv file 2>')
    parser.add_argument("omssacsv1", help="First omssa result file")
    parser.add_argument("omssacsv2", help="Second omssa result file")
    parser.parse_args()

    args = sys.argv
    omssacsv_ref = args[1]
    omssacsv_nonref = args[2]

    # Pass the omssa output files as arguments
    # omssacsv_nonref = r'C:\Bitbucket_repos\NCBI_OMSSA\Output\Run1.csv'
    # omssacsv_ref = r'C:\Bitbucket_repos\NCBI_OMSSA\Output\Run2.csv'

    ref_nonref = [omssacsv_ref, omssacsv_nonref]

    for omssacsvFiles in ref_nonref:
        
        omssacsv_name = os.path.join(omssacsvFiles)

        updatePSMs = add_reverse_info(omssacsv_name)

        plot_roc_curve(updatePSMs, omssacsv_name)

    return 0


def add_reverse_info(csv_df):
    """
    Use ##REV## info from Defline to calculate false-hits, rest are true-hits
    """
    df = pd.read_csv(os.path.join(csv_df))
    # Note a space before E-value (use df.columns to look at header values and do not forget [[[import pdb; pdb.set_trace()]]])
    df_sorted = df.sort_values(by=[' E-value'])
    df_sorted['IsReverse'] = df_sorted[' Defline'].str.match('###REV###')
    # Turn IsReverse to 1 (from google!)
    df_sorted['IsReverseValue'] =  df_sorted['IsReverse'] * 1
    df_sorted['false-hits'] = np.cumsum(df_sorted['IsReverseValue'])
    df_sorted['rev_labels'] = -1 * df_sorted['IsReverseValue'] + 1
    df_sorted['true-hits'] = np.cumsum(df_sorted['rev_labels'])
    return df_sorted


def plot_roc_curve(df, filenameFDR):
    """
    Function to plot ROC curve
    """
    fig = plt.figure()
    plt.plot(df['false-hits'], df['true-hits'])
    plt.ylabel('True Positives')
    plt.xlabel('False positives')
    # plt.show()
    fig.savefig(os.path.join('../Output_pngs', os.path.basename(filenameFDR) + '_ROC.png'), dpi=fig.dpi)
    return 0

# Execute the main function
if __name__ == "__main__":
    main()

