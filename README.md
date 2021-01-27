# ACM Research Coding Challenge (Spring 2021)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge-S21`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uqAJNXUe).

## Question One

Genome analysis is the identification of genomic features such as gene expression or DNA sequences in an individual's genetic makeup. A genbank file (.gb) format contains information about an individual's DNA sequence. The following dataset in `Genome.gb` contains a complete genome sequence of Tomato Curly Stunt Virus. 

**With this file, create a circular genome map and output it as a JPG/PNG/JPEG format.** We're not looking for any complex maps, just be sure to highlight the features and their labels.

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## David Kumar's solution 

Note: Works cited as links within parentheses 

1. Surf the web for info on circular genome diagrams and how they are rendered from a genbank by means of biological methods due to my limited knowledge of biology and then computational methods.
2. Find a library capable of reading the genbank file format and manipulating sequence data.(https://biopython.org/wiki/SeqIO)
3. Read through biopython's vast documentation to find a module capable of drawing whole genomes as circular wheel diagrams.(https://biopython-tutorial.readthedocs.io/en/latest/notebooks/17%20-%20Graphics%20including%20GenomeDiagram.html) 
4. Install the dependencies(using pip) - biopython, reportlab, pillow.
5. Read the data from genbank file and store it.
6. Create an empty diagram, track and feature sets.
7. Add the five gene features to the diagram represented by different colors.
8. For the purpose illustration, choose ten restriction endonuclease found in the Tomato Curly Stunt Virus(https://www.neb.com/products/restriction-endonucleases)
to represent on the diagram.
9. Create the circular wheel diagram using the Reportlab object.
10. Render to the PNG format.
