# Step-by-Step Algorithm

This file explains the algorithms for two Python programs:

1. Creating a password dictionary using lowercase and uppercase English letters.
2. Cracking a password-protected ZIP file using that dictionary.

Use the ZIP cracking program only for ZIP files you own or have explicit permission to test.

## Program 1: Password Dictionary Generator

Goal: create a text file containing every possible 5-character password using `a-z` and `A-Z`.

### Algorithm

1. Start the program.

2. Import the required Python modules:
   - `itertools`, used to generate combinations.
   - `string`, used to get English alphabets easily.

3. Create a variable containing all lowercase English letters:
   - `abcdefghijklmnopqrstuvwxyz`

4. Create another variable containing all uppercase English letters:
   - `ABCDEFGHIJKLMNOPQRSTUVWXYZ`

5. Combine both variables into one character set.

6. The final character set contains 52 characters:
   - 26 lowercase letters.
   - 26 uppercase letters.

7. Set the password length to `5`.

8. Choose the output file name, for example:
   - `password_dictionary.txt`

9. Open the output file in write mode.

10. Use a combination-generating method to create all possible arrangements of 5 characters from the 52-character set.

11. Each generated password will contain exactly 5 characters.

12. The same character may appear more than once in a password.

13. Example generated passwords may look like:
   - `aaaaa`
   - `aaaab`
   - `aaaac`
   - `aaaBa`
   - `ZZZZZ`

14. For every generated combination, join the individual characters together to form a password string.

15. Write the password string into the output file.

16. Add a new line after each password so that every password is stored on a separate line.

17. Repeat the process until all possible 5-character combinations are generated.

18. Close the output file.

19. Display a message saying that the password dictionary has been created successfully.

20. Stop the program.

### Number of Passwords Generated

Since there are 52 possible characters and the password length is 5:

```text
52 x 52 x 52 x 52 x 52 = 380,204,032
```

So the program generates `380,204,032` passwords.

## Program 2: ZIP Password Cracker Using Dictionary Attack

Goal: try each password from the dictionary file on a password-protected ZIP file until the correct password is found.

### Algorithm

1. Start the program.

2. Import the required Python modules:
   - `zipfile`, used to open and extract ZIP files.
   - `pathlib`, used to handle file paths.
   - `argparse`, used to accept input from the command line.

3. Take the ZIP file path from the user.

4. Take the dictionary file path from the user.

5. Take the output folder path from the user.

6. Check whether the ZIP file exists.

7. If the ZIP file does not exist, display an error message and stop the program.

8. Check whether the dictionary file exists.

9. If the dictionary file does not exist, display an error message and stop the program.

10. Create the output folder if it does not already exist.

11. Open the password-protected ZIP file.

12. Open the dictionary file in read mode.

13. Read the first line from the dictionary file.

14. Remove extra spaces and the newline character from the line.

15. Store the cleaned line as the password to try.

16. Convert the password from string format to byte format.

17. Try to extract the ZIP file using this password.

18. If the password is wrong, the extraction will fail.

19. If extraction fails, catch the error so the program does not stop.

20. Read the next password from the dictionary file.

21. Repeat the same process for each password in the dictionary.

22. If extraction succeeds, the password is correct.

23. Display the correct password.

24. Display the number of attempts made.

25. Extract the ZIP file contents into the output folder.

26. Stop trying more passwords.

27. Close the dictionary file.

28. Close the ZIP file.

29. Stop the program.

## Combined Working Process

1. Run the password dictionary generator program first.

2. The generator creates a file named `password_dictionary.txt`.

3. Place the password-protected ZIP file in the project folder, or provide its full path.

4. Run the ZIP password cracking program.

5. The cracking program opens the ZIP file.

6. It opens the password dictionary file.

7. It reads one password from the dictionary.

8. It tries that password on the ZIP file.

9. If the password is wrong, it moves to the next password.

10. If the password is correct, it extracts the ZIP file.

11. It prints the correct password.

12. The program ends.

## Important Notes

1. The dictionary file will be very large because it contains `380,204,032` passwords.

2. Creating the dictionary may take a long time.

3. Cracking the ZIP file may also take a long time.

4. The correct password must exist inside the dictionary file for the attack to succeed.

5. Python's built-in `zipfile` module supports traditional ZIP encryption.

6. Some AES-encrypted ZIP files may need another library such as `pyzipper`.
