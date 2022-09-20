import argparse

from unhingify.rules.random_capitalization import RandomCapitalizationRule
from unhingify.rules.space_around_punctuation import SpaceAroundPunctuationRule
from unhingify.rules.to_lower import ToLowerRule
from unhingify.transformer import Transformer


def main():
    # Take in input from stdin.
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=argparse.FileType("r"), default="-")
    parser.add_argument("-o", "--output", help="The file to write to.")
    args = parser.parse_args()

    # Read the input.
    text = args.input.read().strip()

    tx = Transformer()
    tx.add_rule(ToLowerRule(), 0)
    tx.add_rule(RandomCapitalizationRule(), 10)
    tx.add_rule(SpaceAroundPunctuationRule(), 10)

    # Apply the rules.
    text = tx.apply(text)

    # Write the output.
    if args.output:
        with open(args.output, "w") as f:
            f.write(text)
    else:
        print(text)


if __name__ == "__main__":
    main()
