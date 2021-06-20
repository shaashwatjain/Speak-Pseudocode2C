import click
from pseudo_parser import pseudo_Parser


@click.command()
@click.option(
    "--filename",
    default="input2.txt",
    help="The file from which the pseudocode will be read",
)
@click.option(
    "--output",
    default="output.c",
    help="The file which will contain the compiled code",
)
def main(filename, output):

    ast = Pseudo_Parser().parse(text)

    output_file = open(output, "w+")
    #  A line will come which will write the text in file
    output_file.close()


if __name__ == "__main__":
    main()
