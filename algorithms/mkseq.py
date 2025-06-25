#!/usr/bin/env python3

import pandas as pd
import csv

#Create a csv file with the DNA sequences, gene ids, and the characterstics

def csv_maker(path,headings, data):
    """
    Creating a new csv
    """
    with open(path, "w", newline='') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=headings)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    data = ["Promoter ID,Description of the gene,Sequence".split(","),
            "RAB10_1,member RAS oncogene family,accgcaaggctagggcgtgagggaagggcgggcgtacgcccttgcgtgcGTCTCAGGCAG".split(","),
            "RAC1_1,ras-related C3 botulinum toxin substrate 1,gcgcgggggaggggaggccggatgtgagtggagcggccatttcctgtttCTCTGCAGTTT".split(","),
            "SERAC1_1,serine active site containing 1,tgggtggagccagccggcgggaggcgggcccagagcgggccgagggggcGGGGTCACGAG".split(","),
        "CHRAC1_1,chromatin accessibility complex 1,ggcggtgtccgagcgtcggcgcatgcgcagatcgggggcgcgaggcctcACGGAGCTCGT".split(","),
         "RDH10_1,retinol dehydrogenase 10,ggctcttcccggtcgcggggttatatagcgcggagcgtggagcccgctcAGAGCCGGCCC".split(","),
         "ABCA10_1,ATP binding cassette subfamily A member 10,cgcggccgcgccctcgcacagatcccagctgggtcacccgcactgagtcAACAGACTGAG".split(","),
         "GSAP_1,gamma-secretase activating protein,cagggggcgggggagaggaaagagggggcgggagcggggacgcgagggcGAGGCGGCCAC".split(","),
         "HBA1_1,hemoglobin subunit alpha 1,gcgtgcccccgcgccccaagcataaaccctggcgcgctcgcggcccggcACTCTTCTGGT".split(","),
         "HBS1L_1,HBS1 like translational GTPase,ccgtcgcgcggtgcacagctaagacgtcgcgcttgcgcaggcgctcggcGCAGAGGCCTG".split(","),
            ]
    my_list = []
    headings = data[0]
    for values in data[1:]:
        my_dict = dict(zip(headings, values))
        my_list.append(my_dict)

    path = "human_sample_genes.csv"
    csv_maker(path, headings, my_list)

