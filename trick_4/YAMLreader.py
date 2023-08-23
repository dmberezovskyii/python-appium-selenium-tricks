import yaml
from pathlib import Path


class YamlReader:

    @staticmethod
    def read_caps(device="pixel", filename="caps.yaml"):
        try:
            # Get the path to the properties folder
            properties_path = Path(__file__).resolve().parent / "../trick_4/properties"
            abs_path = properties_path / filename

            with open(abs_path, 'r', encoding="UTF-8") as stream:
                data = yaml.safe_load(stream)
                return data.get(device)
        except (yaml.YAMLError, KeyError) as e:
            print(f'Error: {e}')
            return None


if __name__ == '__main__':
    caps_data = YamlReader.read_caps()
    if caps_data:
        print(caps_data)
    else:
        print("Failed to read YAML.")
