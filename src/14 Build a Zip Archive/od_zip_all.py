import pathlib
import zipfile

def zip_all(input_dir, extentions_list, output_file_path):
  directory = pathlib.Path(input_dir)

  with zipfile.ZipFile(output_file_path, mode="w") as archive:
    for file_path in directory.rglob("*"):
      if file_path.suffix in extentions_list:
        archive.write(file_path,
                    arcname=file_path.relative_to(directory)
                    )

  with zipfile.ZipFile(output_file_path, mode="r") as archive:
    archive.printdir()

zip_all('.\\my_stuff', ['.jpg','.txt'], 'od_stuff.zip')   