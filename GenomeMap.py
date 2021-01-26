from Bio.SeqFeature import SeqFeature, FeatureLocation
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO


def create_diagram():

    # gathering the required genbank data from the specified file
    recs = SeqIO.read("Genome.gb", "genbank")

    # creating an empty diagram
    gd_diagram = GenomeDiagram.Diagram("Circular Genome Map of Genome Sequence of Tomato Curly Stunt Virus")

    # adding an empty track
    gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")

    # adding an empty feature set
    gd_feature_set = gd_track_for_features.new_set()

    # parsing each of the 5 gene features and generating a feature on the diagram - v1,v2,c1,c2,c3

    for feature in recs.features:
        if feature.type != "gene":
            # exclude this feature
            continue

        # adding colors to each feature
        if len(gd_feature_set) % 5 == 0:
            color = colors.violet
        elif len(gd_feature_set) % 5 == 1:
            color = colors.indigo
        elif len(gd_feature_set) % 5 == 2:
            color = colors.blue
        elif len(gd_feature_set) % 5 == 3:
            color = colors.green
        else:
            color = colors.orange

        gd_feature_set.add_feature(feature, sigil="ARROW",
                               color=color, label=True,
                               label_size=14, label_angle=0)

    # displaying position of selected sites by means of specified restriction endonuclease

    for site, name, color in [("CTCGAG", "SacI", colors.violet),
                              ("GGATCC", "BamHI", colors.indigo),
                              ("AGCT", "AluI", colors.blue),
                              ("CGTACG", "SphI", colors.green),
                              ("GGGCCC", "ApaI", colors.yellow),
                              ("GACGT", "AatII", colors.orange),
                              ("GTCGAC", "SalI", colors.red),
                              ("CCGG", "MspI", colors.darkviolet),
                              ("AGATCT", "XbaI", colors.darkblue)]:
        index = 0
        while True:
            index = recs.seq.find(site, start=index)
            if index == -1:
                break
            feature = SeqFeature(FeatureLocation(index, index + len(site)))
            gd_feature_set.add_feature(feature, color=color, name=name,
                                       label=True, label_size=10,
                                       label_color=color)
            index += len(site)

    # creating circular shape using Reportlab objects
    gd_diagram.draw(format="circular", circular=True, pagesize=(20 * cm, 20 * cm),
                    start=0, end=len(recs), circle_core=0.5)

    # renders diagram to necessary format
    gd_diagram.write("circular_genome_map.png", "PNG")


# driver function
if __name__ == '__main__':

    create_diagram()
