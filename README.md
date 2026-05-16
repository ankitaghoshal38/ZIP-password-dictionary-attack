# ZIP-password-dictionary-attack
Python scripts to generate a 5-character alphabetic password dictionary and recover authorized password-protected ZIP files using a dictionary attack.
# ZIP Password Dictionary Attack

Use these scripts only for ZIP files you own or have explicit permission to test.

## 1. Create the password dictionary

```powershell
python .\generate_password_dictionary.py -o password_dictionary.txt
```

This generates all 5-character passwords made from lowercase and uppercase English
letters: `a-z` and `A-Z`.

Total passwords:

```text
52^5 = 380,204,032
```

The file will be very large.

## 2. Crack a password-protected ZIP file

```powershell
python .\crack_zip_dictionary.py .\protected.zip -d .\password_dictionary.txt -o .\extracted_zip
```

If the password is found, the ZIP contents are extracted to the output directory.

Note: Python's built-in `zipfile` module supports traditional ZIP encryption. Some
AES-encrypted ZIP files created by tools like 7-Zip or WinRAR may require another
library such as `pyzipper`.
