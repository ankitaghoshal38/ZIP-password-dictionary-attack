import argparse
import itertools
import string


DEFAULT_LENGTH = 5
CHARACTERS = string.ascii_lowercase + string.ascii_uppercase


def generate_passwords(length):
    for password_tuple in itertools.product(CHARACTERS, repeat=length):
        yield "".join(password_tuple)


def main():
    parser = argparse.ArgumentParser(
        description="Create a password dictionary using a-z and A-Z."
    )
    parser.add_argument(
        "-o",
        "--output",
        default="password_dictionary.txt",
        help="Output dictionary file path.",
    )
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=DEFAULT_LENGTH,
        help="Password length to generate.",
    )
    args = parser.parse_args()

    if args.length <= 0:
        raise SystemExit("Password length must be greater than 0.")

    total = len(CHARACTERS) ** args.length
    print(f"Generating {total:,} passwords into {args.output}")

    with open(args.output, "w", encoding="utf-8", newline="\n") as dictionary_file:
        for index, password in enumerate(generate_passwords(args.length), start=1):
            dictionary_file.write(password + "\n")
            if index % 1_000_000 == 0:
                print(f"Wrote {index:,} passwords...")

    print("Done.")


if __name__ == "__main__":
    main()
