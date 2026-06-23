"""A hack so that pylint does not attempt to run on *.pyi files.

Since it is not possible to configure pylint to ignore *.pyi files,
this simple script adds:

'# pylint: skip-file'

to the top of each *.pyi file in the pyaqsapi directory.
Run this script after generating stubs with stubgen.
"""  # pylint: disable=wrong-spelling-in-docstring

import os

HEADER = "# pylint: skip-file \n\n"

PATH = "./pyaqsapi/"
count = 0

for root, _dirs, files in os.walk(PATH):  # noqa: F401, F841
    for file in files:
        if file.endswith(".pyi"):
            file_path = os.path.join(root, file)

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Prevent adding the header multiple times if run sequentially
            if not content.startswith(HEADER):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(HEADER + content)
                    count += 1
                    print(f"Added header to: {file_path}")
print(f"Total header of *.pyi files modified: {count}")
