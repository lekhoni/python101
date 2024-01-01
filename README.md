# Testing homeworks and projects

## Open Terminal or Command Prompt

On Windows, you can search for "cmd" or "Command Prompt" in the start menu.
On macOS or Linux, you can open "Terminal" from applications or search.

## Change Directory

Change the directory to where your files are located using the cd command. For example:
```bash
cd path/to/your/project/directory/python101
```


## Ensure Python is Installed

Make sure you have Python installed on your system. You can verify it by running `python --version` or `python3 --version` in your terminal or command prompt.

## Navigate to Your Project Directory

Use the command line to navigate to the directory where your lesson files are located. For example if you are trying lesson1:

```
cd lesson1
```

## Running the Tests

Once you're in the correct directory, you can run the tests using the following command:
```
python -m unittest <test_file_name>.py
```

Replace <test_file_name> with the actual name of your test file. If the test file is named test_variables.py, the command would be:

```
python -m unittest test_variables.py
```
