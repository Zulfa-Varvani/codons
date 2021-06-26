# Codon Translator 🧬📃
Translation of nucleotides in the mRNA into a sequence of amino acids using the genetic code

Genes provide instructions for the formation of proteins and are expressed in two steps: transcription and translation. 
In this project, we take the translated sequence of the DNA (messenger RNA or mRNA) and translate it into a sequence of amino acids in a polypeptide chain. 
Cells decode mRNAs by reading their nucleotides in groups of three, called codons. The 'start' codon marks the beginning of the protein (AUG = Met), while three codons indicate the 'stop' of the protein sequencing.
mRNA codons are read from 5' to 3' and specify amino acids from the N-terminus to C-terminus. 
Full relationships between codons and amino acids summarized in a genetic code.

In this program, user enters an mRNA sequence to be decoded and translated into an amino acid sequence. The program identifies the start codon (AUG) and divides the string into three's (as codons are three nucleotides). Each codon is compared to the codons written in table.txt and attributed an amino acid at that index. New string of amino acid formed and printed out.
