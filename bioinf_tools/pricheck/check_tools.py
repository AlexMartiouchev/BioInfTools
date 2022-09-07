from biomart import BiomartServer
import pandas as pd

# convert VCF file to nested dictionary detailing CHROM and POS


def vcf_convert(file):
    pre_list = file.split("\n")
    variants_final = []

    if pre_list[-1] == "":  # removes interfering blank last line
        pre_list.pop(-1)

    for line in pre_list:
        line = line.split("\t")

        if line[0][0] != "#":
            variant_dict = {"CHROM": line[0], "POS": line[1]}
            variants_final.append(variant_dict)

    return variants_final


# set up server and dataset for common_check

server = BiomartServer("http://feb2014.archive.ensembl.org/biomart")
snp = server.datasets['hsapiens_snp']

# check database for common variants


def common_check(variant_dictionary):
    common_variants = []
    for variant in variant_dictionary:
        common = snp.search({
            "filters": {
                "chrom_start": int(variant["POS"]),
                "chrom_end": int(variant["POS"]),
                'variation_source': 'dbSNP',
                "variation_set_name": "1000 Genomes - All - common"
            }
        }, header=1)
        common_variants.append(common)
    return common_variants


# create list of items from response

def iterate_response(response):
    response_list = []
    for items in response:
        items = items.text
        response_list.append(items)
    return response_list


# create a list of common and uncommon variants
def common_output(vcf, result):
    found_variants = []
    uncommon_variants = []
    n = 0
    for items in result:
        items = items.split("\n")
        if items[1] == "":
            uncommon_variants.append(vcf[n])
            n += 1
        else:
            n += 1
    return uncommon_variants


def bed_convert(file):
    pre_list = file.split("\n")
    bed_prim_final = []

    if pre_list[-1] == "":  # removes interfering blank last line
        pre_list.pop(-1)

    for line in pre_list:
        line = line.split("\t")

        if line[0][0] != "#":
            bed_prim_dict = {"CHROM": line[0][3:], "From": line[1], "To": line[2], "ID": line[3]}
            bed_prim_final.append(bed_prim_dict)

    return bed_prim_final


def bed_compare(vcf, bed):
    with_p = []
    without_p = []
    for variant in vcf:
        for primer in bed:
            if str(variant["CHROM"]).upper() == str(primer["CHROM"]).upper():
                if primer["From"] <= variant["POS"] <= primer["To"]:
                    variant.update({"Primer": primer["ID"]})
    for variant in vcf:
        if "Primer" in variant:
            with_p.append(variant)
        else:
            without_p.append(variant)

    return with_p, without_p


'''
primed = []
not_primed = []


def checking(val):
    for index, row in val.iterrows():
        if row['From'] <= val <= row['To']:
            primed.append(val)
            return True
    not_primed.append(val)
'''
