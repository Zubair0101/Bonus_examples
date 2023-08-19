import zipfile


def extract_archive(filepath, destination):
    with zipfile.ZipFile(filepath, 'r') as archive:
        archive.extractall(destination)


if __name__ == "__main__":
    extract_archive(filepath=r"C:\IdeaProjects\Python Course 2.0\compressed_archive.zip",
                    destination=r"C:\IdeaProjects\Python Course 2.0\bonus\dest")
