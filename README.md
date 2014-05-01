PeptidomicsEnzymeEstimator 
==========================
###(aka: Peptidomics Enzyme Tabulator, PEnTab)



####Online version available:
Currently a Beta version is on my [personal page](http://peptidomics.evanaparker.com). Message me for access.

Dependencies:
-------------
  * Python 2.7
  * Biopython

  
  
What does this program do?
--------------------------

This program helps extract rough estimates of enzyme activity by mapping peptide feature intensity
to enzyme identity by evaluating the termini of the peptides against enzymatic systems. This program
does not propose to predict enzymatic activity nor can it be truly quantitative even if passed quantitative
data since a cut can rarely be traced to a specific enzyme. Still, the estimation provided by this mapping 
can provide insights into the dominant enzymatic systems and can be used to help identify unexpected
or uncharacterised behaviour.

The output includes intensities mapped to enzyme identities from the provided list, it also includes "orphan
specificities" These, unlike enzymatic mapping which is may overlap, are only extracted if no defined
enzymatic system can account for a peptides terminus. In this case, both amino acids accounting for the site
of cleavage at the terminus of the peptide will have 50% of the peptide's intensity mapped to a "c-side" and
an "n-side" amino acid cleavage category. Thus, a peptide arising from a fully characterized set of proteases
will have no mapped intensity in this category.

  
Quick tutorial: example code below
---------------------------------

    #first, import the module
    import PeptidomicsEnzymeEstimator as pee
    
    #next, open relevant library files:
    fastaFile = open("degradomeLibrary.fasta", "r")
    csvTestFile = open("15_samples_milk_degradome.csv", 'r')
    inputEnzymeList = ["Trypsin", "Elastase"]
    
    #load and preprocess peptides, then retrieve the results as a dictionary or a two tier list 
    #(the list result method is useful for making CSVs)
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

  * "sequence" - Single letter AA sequences of the peptides
  * "intensity" - An integer of float representing MS response
  * "protein_id" - This must be the accession number used in the uniprot file
  * "sample_id" - This string defines the experiment or chromatographic run and is used for grouping
              
lines prior to the header may be empty or may be marked with a '#' to indicate a comment

    

Annotated function and classes
-------------------------------
    
    class Peptide
    
This class represents the peptide, contains macroscopic information and search functions,
this class is initialized and maintained internally by the provided helper functions.
Use the help() function on peptide for further documentation


    function import_peptides_and_preprocess()
    
Takes the following arguments

  * peptideCsvFileObject = a file object of the peptide CSV file
  * fastaFileObject = a file object of the fasta library
  * validEnzymeList = a list of valid enzymes, these enzymes must have regex entries in the '_el' library

Returns

  * peptideList = A list of peptide objects

    function extract_data_from_processed_peptides()

Takes the following arguments

  * peptideList = A list of peptide objects
  * validEnzymeList = a list of valid enzymes with regex patterns, case sensitive. See below for enzymes.
  * method = A string for the grouping method, use "sampleId" to group by experiment and "accession" to group by protein.
  * result = A string specifying the output, use "dictionary" for raw data and "list" for a csv formatted lists

returns:

  * A list or dict depending on the result method, default value is dictionary.
    
   

Proteolytic enzymes:
--------------------
check the "_el" dictionary in EnzymeCutQuantifier.py for valid enzymes
    

    
A note on the meaning of N-side and C-side cleavages
----------------------------------------------------

This program uses the most common definition of N and C side cleavages and this section
was written to address any misconceptions that can arise from working with peptides.

Convention dictates writing sequences from N to C. While this convention is held
by this program, a confusing wrinkle can be illustrated using the sequence below where 
forward slashes represent an observed enzymatic cleavage producing the peptide VNLAS:

    n...R/VNLAS/W...c

We can say that enzymes are cutting on the C side of arginine or on the N side of valine.
So far, this is intuitive. But, if there is a C-side cut for arginine, this produces
the n-terminus of the peptide, alternatively an N-side cut on tryptophan will produce
the c-terminus of the peptide. Intensities will always be assigned using the specificity
of the cleavage, not using traditional n and c side assignments of a peptide. Keeping this
in mind will help interpreting the extraction of the "nSideOrphans" and "cSideOrphans" data. 

As an example, say the peptide above (VNLAS) has an intensity of 100 and it is analyzed
with no explicit enzymes. The cSideOrphans dictionary would contain {"R":100, "S":100}
and the nSideOrphans dictionary would contain {"V":100, "W":100}. If the same peptide
as analyzed using only trypsin then the analysis would return an enzyme dictionary with
{"trypsin":100}, cSideOrphans == {"S":100}, nSideOrphans == {"W":100}.
