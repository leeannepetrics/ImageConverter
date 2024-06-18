import os, subprocess

def convert_image(directory):
    files = os.listdir(directory)

    heic_files = []

    for file in files:
        if file.upper().endswith('.HEIC'):
            heic_files.append(file)

    for heic_file in heic_files:
        input_path = os.path.join(directory, heic_file)
        output_path = os.path.join(directory, heic_file.rsplit('.', 1)[0] + '.jpg')

        try:
            result = subprocess.run(["magick", input_path, "-strip", output_path], check=True)
            print(f"Converted {heic_file} to JPG successfully.")
            os.remove(input_path)
            print(f"Deleted original HEIC file: {heic_file}")

        except subprocess.CalledProcessError as e:
            print(f"Error converting {heic_file}: {e}")

        except OSError as e:
            print(f"Error deleting {heic_file}: {e}")