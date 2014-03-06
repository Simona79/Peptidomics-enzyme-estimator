"""
This unit test module checks the enzyme regex functions for proper function.
Any addtions to the enzyme list must include unit tests
"""

from PeptidomicsEnzymeEstimator import enzymeListNC



if __name__ == "__main__":
    import unittest
    
    class TestPeptideRe(unittest.TestCase):

        def setUp(self):
            pass
        
        """ Base format for easy creation of new tests
        def test_(self):
            #c side 
            self.assertIsNotNone(enzymeListNC[""]["c"].search("AAAAAAAAA"))
            self.assertIsNotNone(enzymeListNC[""]["c"].search())
            self.assertIsNone(enzymeListNC[""]["c"].search())
            #n side
            self.assertIsNotNone(enzymeListNC[""]["n"].search())
            self.assertIsNotNone(enzymeListNC[""]["n"].search())
            self.assertIsNone(enzymeListNC[""]["n"].search())
        """
        
        def test_arg_c_proteinase(self):
            #c side 
            self.assertIsNotNone(enzymeListNC["Arg-C proteinase"]["c"].search("APZYFTRPS"))
            self.assertIsNotNone(enzymeListNC["Arg-C proteinase"]["c"].search("_NPRY_"))
            self.assertIsNone(enzymeListNC["Arg-C proteinase"]["c"].search("PRYSTYS"))
            self.assertIsNone(enzymeListNC["Arg-C proteinase"]["c"].search("_____"))
            #n side
            self.assertIsNotNone(enzymeListNC["Arg-C proteinase"]["n"].search("ARPZYFTnPS"))
            self.assertIsNotNone(enzymeListNC["Arg-C proteinase"]["n"].search("_RPNY_"))
            self.assertIsNone(enzymeListNC["Arg-C proteinase"]["n"].search("PDYSRYS"))
            self.assertIsNone(enzymeListNC["Arg-C proteinase"]["n"].search("_____"))
            
        def test_asp_n_endopeptidase(self):
            #c side
            self.assertIsNotNone(enzymeListNC["Asp-N endopeptidase"]["c"].search("ABCREFDH"))
            self.assertIsNotNone(enzymeListNC["Asp-N endopeptidase"]["c"].search("ABCREFD_"))
            self.assertIsNone(enzymeListNC["Asp-N endopeptidase"]["c"].search("ABDREFP_"))
            self.assertIsNone(enzymeListNC["Asp-N endopeptidase"]["c"].search("_____"))
            self.assertIsNone(enzymeListNC["Asp-N endopeptidase"]["c"].search(""))
            #n side
            self.assertIsNotNone(enzymeListNC["Asp-N endopeptidase"]["n"].search("ABDREFP_"))
            self.assertIsNotNone(enzymeListNC["Asp-N endopeptidase"]["n"].search("_BDREFP_"))
            self.assertIsNone(enzymeListNC["Asp-N endopeptidase"]["n"].search("__DREFP_"))
            self.assertIsNone(enzymeListNC["Asp-N endopeptidase"]["n"].search("_____"))

        def test_BNPS_Skatole(self):
            #c side 
            self.assertIsNotNone(enzymeListNC["BNPS-Skatole"]["c"].search("AAAAAAWAA"))
            self.assertIsNotNone(enzymeListNC["BNPS-Skatole"]["c"].search("AAAAAAWA_"))
            self.assertIsNone(enzymeListNC["BNPS-Skatole"]["c"].search("AAAAAAW__"))
            #n side
            self.assertIsNotNone(enzymeListNC["BNPS-Skatole"]["n"].search("AWAAAAA__"))
            self.assertIsNotNone(enzymeListNC["BNPS-Skatole"]["n"].search("_WAAAAW__"))
            self.assertIsNone(enzymeListNC["BNPS-Skatole"]["n"].search("AAAAAAW__"))
            
        def test_Chymotrypsin_low_specificity(self):
            #c side 
            self.assertIsNotNone(enzymeListNC["Chymotrypsin low-specificity"]["c"].search("AAAAAALAA"))
            self.assertIsNotNone(enzymeListNC["Chymotrypsin low-specificity"]["c"].search("AAAAAALA_"))
            self.assertIsNotNone(enzymeListNC["Chymotrypsin low-specificity"]["c"].search("AAAAAAWA_"))
            self.assertIsNotNone(enzymeListNC["Chymotrypsin low-specificity"]["c"].search("AAAAAAHC_"))
            self.assertIsNone(enzymeListNC["Chymotrypsin low-specificity"]["c"].search("AAAAAAWP_"))
            self.assertIsNone(enzymeListNC["Chymotrypsin low-specificity"]["c"].search("AAAAAAHA_"))
            #n side
            self.assertIsNotNone(enzymeListNC["Chymotrypsin low-specificity"]["n"].search("AFAAAANAA"))
            self.assertIsNotNone(enzymeListNC["Chymotrypsin low-specificity"]["n"].search("_MAAAALAA"))
            self.assertIsNone(enzymeListNC["Chymotrypsin low-specificity"]["n"].search("_MPAAALAA"))
        
        def test_Chymotrypsin_high_specificity(self):
            #c side 
            self.assertIsNotNone(enzymeListNC["Chymotrypsin high-specificity"]["c"].search("AAAAAAYAA"))
            self.assertIsNotNone(enzymeListNC["Chymotrypsin high-specificity"]["c"].search("AAAAAAFA_"))
            self.assertIsNotNone(enzymeListNC["Chymotrypsin high-specificity"]["c"].search("AAAAAAWA_"))
            self.assertIsNone(enzymeListNC["Chymotrypsin high-specificity"]["c"].search("AAAAAAWMA"))
            #n side
            self.assertIsNotNone(enzymeListNC["Chymotrypsin high-specificity"]["n"].search("AYAAAAAMA"))
            self.assertIsNotNone(enzymeListNC["Chymotrypsin high-specificity"]["n"].search("AWAAAAWMA"))
            self.assertIsNone(enzymeListNC["Chymotrypsin high-specificity"]["n"].search("__WMAAAWMA"))
            
        def test_Pepsin(self):
            #c side 
            self.assertIsNotNone(enzymeListNC["Pepsin"]["c"].search("AAAAAAAFA"))
            self.assertIsNotNone(enzymeListNC["Pepsin"]["c"].search("AAAAAAWAA"))
            self.assertIsNone(enzymeListNC["Pepsin"]["c"].search("AAAAAAAAA"))
            #n side
            self.assertIsNotNone(enzymeListNC["Pepsin"]["n"].search("AFAAAAAA"))
            self.assertIsNotNone(enzymeListNC["Pepsin"]["n"].search("_WAAAAAAFA"))
            self.assertIsNone(enzymeListNC["Pepsin"]["n"].search("AAAAAAAFAA"))
            
        def test_Cathepsin_D(self):
            #c side 
            self.assertIsNotNone(enzymeListNC["Cathepsin D"]["c"].search("AAAAAAPIA"))
            self.assertIsNotNone(enzymeListNC["Cathepsin D"]["c"].search("AAAAAAVP_"))
            self.assertIsNone(enzymeListNC["Cathepsin D"]["c"].search("AAAAAANN_"))
            #n side
            self.assertIsNotNone(enzymeListNC["Cathepsin D"]["n"].search("AWFAAAAAA"))
            self.assertIsNotNone(enzymeListNC["Cathepsin D"]["n"].search("AFMAAAAAAA"))
            self.assertIsNone(enzymeListNC["Cathepsin D"]["n"].search("NNNAAAAAA"))
        
        def test_Thrombin(self):
            #c side 
            self.assertIsNotNone(enzymeListNC["Thrombin"]["c"].search("AAAAAARGA"))
            self.assertIsNotNone(enzymeListNC["Thrombin"]["c"].search("AAAAGRA_"))
            self.assertIsNone(enzymeListNC["Thrombin"]["c"].search("AAAAGRA__"))
            #n side
            self.assertIsNotNone(enzymeListNC["Thrombin"]["n"].search("_RGAAAAA"))
            self.assertIsNotNone(enzymeListNC["Thrombin"]["n"].search("GRAAAAA"))
            self.assertIsNone(enzymeListNC["Thrombin"]["n"].search("AAAAAA"))
        
        def test_Elastase(self):
            #c side 
            self.assertIsNotNone(enzymeListNC["Elastase"]["c"].search("AAAAAARPA"))
            self.assertIsNotNone(enzymeListNC["Elastase"]["c"].search("AAAAAAVA_"))
            self.assertIsNone(enzymeListNC["Elastase"]["c"].search("AAAAAANN_"))
            #n side
            self.assertIsNotNone(enzymeListNC["Elastase"]["n"].search("ALLAAAAAA"))
            self.assertIsNotNone(enzymeListNC["Elastase"]["n"].search("_AFAAAAAAA"))
            self.assertIsNone(enzymeListNC["Elastase"]["n"].search("NNNAAAAAA"))    
    
    unittest.main(exit=False)