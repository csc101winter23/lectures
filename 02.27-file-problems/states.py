import sys


def parse_row(row, regions):
    """
    Parse a single row within a CSV of population data.

    :param row: A single textual row from a CSV
    :param regions: A dictionary mapping region names to populations
    """
    row = row.strip().split(",")

    # Note that the first column is the state names, which we don't need.
    region = row[1]
    population = int(row[2])

    if region not in regions:
        regions[region] = [population, 1]
    else:
        regions[region][0] = regions[region][0] + population
        regions[region][1] = regions[region][1] + 1


def parse_csv(csv_name):
    """
    Parse a CSV of population data.

    :param csv_name: A name of a CSV file
    :return: A dictionary mapping region names to populations
    """
    regions = {}

    with open(csv_name, "r") as csv_file:
        # Note that the first row is the column headings, which we don't need.
        csv_file.readline()

        for row in csv_file:
            parse_row(row, regions)

    return regions


def main():
    # Note that we don't actually care about the states' names; we only care
    #  about their regions and populations. We will need a dictionary mapping
    #  region names to both sum total populations and numbers of states, so
    #  that we can easily look those numbers up later.
    # By convention, such file names are usually taken as command line args.
    csv_name = sys.argv[1]
    regions = parse_csv(csv_name)

    for region in regions:
        print("The average population of the %s region is %f."
              % (region, regions[region][0] / regions[region][1]))


if __name__ == "__main__":
    main()
