PeptidomicsEnzymeEstimator
==========================

Dependencies:
-------------
Python 2.7
Biopython
    
Quck tutorial: example code below
---------------------------------

    #first, import the module
    import PeptidomicsEnzymeEstimator as pee
    
    #next, open relevant library files:
    fastaFile = open("degradomeLibrary.fasta", "r")
    csvTestFile = open("test_15mothers_degradome.csv", 'r')
    inputEnzymeList = ["Trypsin", "Elastase"]
    
    #load and preprocess peptides, then retrieve the results as a dictionary or a two tier list (useful for making CSVs)
    peptideList = pee.import_peptides_and_preprocess(csvTestFile, fastaFile, inputEnzymeList)
    resultCSV = pee.extract_data_from_processed_peptides(peptideList, inputEnzymeList, result = "list")
    
    #export results to file
    import csv
    with open('output.csv', 'wb') as csvfile:
        resultWriter = csv.writer(csvfile)
        resultWriter.writerows(resultCSV)
    
    
Peptide file format
--------------------

CSV file, top line must have columns matching
"sequence" - Single letter AA sequences of the peptides
"intensity" - An integer of float representing MS response
"protein_id" - This must be the accession number used in the uniprot file
"sample_id" - This string defines the experiment or chromatographic run and is used
              for grouping
              
lines prior to this may be empty (having less than 5 characters) or may be marked with 
a '#' to indicate the start of a comment

    

Annotated function and classes
-------------------------------
    
    class Peptide
    
This class represents the peptide, contains macroscopic information and search functions,
this class is initialized and maintained internally by the provided helper functions.
Use the help() function on peptide for further documentation


    function import_peptides_and_preprocess()
    
Takes the following arguments

-peptideCsvFileObject = a file object of the peptide CSV file

-fastaFileObject = a file object of the fasta library

-validEnzymeList = a list of valid enzymes, these enzymes must have regex entries in the '_el' library

Returns

-peptideList = A list of peptide objects

    function extract_data_from_processed_peptides()

Accepts the following arguments

-peptideList = A list of peptide objects

-validEnzymeList = a list of valid enzymes with regex patterns, case sensitive. See below for enzymes.

-method = A string for the grouping method, use "sampleId" to group by experiment and "accession" to group by protein.

-result = A string specifying the output, use "dictionary" for raw data and "list" for a csv object precursor shown inte example

returns:

-A list or dict depending on the result method, default value is dictionary.
    
   

Proteolytic enzymes:
--------------------
check the "_el" dictionary in EnzymeCutQuantifier.py for valid enzymes
    

    
A note on the meaning of N-side and C-side clevages
---------------------------------------------------

This program uses the most common defintion of N and C side cleavages and this section
was written to address any misconceptions that can arise from working with peptides.

Convention dictates writing sequences from N to C. While this convention is held
by this program, a confusing wrinkle can be illustrated using the sequence below where 
forward    slashes represent an observed enzymatic cleavage producing the peptide VNLAS:

    n...R/VNLAS/W...c

We can say that enzymes are cutting on the C side of arginine or on the N side of Valine.
So far, this is intuitive. But, if there is a C-side cut for arginine, this produces
the n-terminus of the peptide, alternatively an N-side cut on tryptophan will produce
the c-terminus of the peptide. Keeping this contradiction in mind will assist when 
interpreting the extraction of the "nSideOrphans" and "cSideOrphans" data.
