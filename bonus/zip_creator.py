import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    path = pathlib.Path(dest_dir, "compressed_archive.zip")

    with zipfile.ZipFile(path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)       # Creates a 'path-string' for the file

            archive.write(filepath, arcname=filepath.name)
            # 'arcname' gives the name of the file instead of the entire path of the file


if __name__ == "__main__":
    make_archive(filepaths=["bonus4.py", "bonus6.py"], dest_dir="dest")
