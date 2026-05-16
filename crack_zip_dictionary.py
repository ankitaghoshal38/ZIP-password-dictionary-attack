import argparse
import zipfile
from pathlib import Path


def try_password(zip_file, password, output_dir):
    try:
        zip_file.extractall(path=output_dir, pwd=password.encode("utf-8"))
        return True
    except RuntimeError:
        return False
    except zipfile.BadZipFile as exc:
        raise SystemExit(f"Invalid zip file: {exc}") from exc


def crack_zip(zip_path, dictionary_path, output_dir):
    with zipfile.ZipFile(zip_path) as zip_file:
        with open(dictionary_path, "r", encoding="utf-8", errors="ignore") as dictionary:
            for attempt, line in enumerate(dictionary, start=1):
                password = line.strip()
                if not password:
                    continue

                if try_password(zip_file, password, output_dir):
                    return password, attempt

                if attempt % 100_000 == 0:
                    print(f"Tried {attempt:,} passwords...")

    return None, attempt if "attempt" in locals() else 0


def main():
    parser = argparse.ArgumentParser(
        description="Recover a ZIP password using a dictionary attack."
    )
    parser.add_argument("zip_file", help="Path to the password-protected ZIP file.")
    parser.add_argument(
        "-d",
        "--dictionary",
        default="password_dictionary.txt",
        help="Path to the password dictionary file.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="extracted_zip",
        help="Directory where files will be extracted if the password is found.",
    )
    args = parser.parse_args()

    zip_path = Path(args.zip_file)
    dictionary_path = Path(args.dictionary)
    output_dir = Path(args.output_dir)

    if not zip_path.is_file():
        raise SystemExit(f"ZIP file not found: {zip_path}")
    if not dictionary_path.is_file():
        raise SystemExit(f"Dictionary file not found: {dictionary_path}")

    output_dir.mkdir(parents=True, exist_ok=True)
    password, attempts = crack_zip(zip_path, dictionary_path, output_dir)

    if password is None:
        print(f"Password not found after {attempts:,} attempts.")
    else:
        print(f"Password found after {attempts:,} attempts: {password}")
        print(f"Files extracted to: {output_dir}")


if __name__ == "__main__":
    main()
