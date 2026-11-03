from pathlib import Path

def get_cats_info(path: str) -> list[dict[str, str]]:
    cats_list = []
    try:
        with open(path, 'r', encoding="utf-8") as f:
            for line in f:
                stripped_line = line.strip()

                if not stripped_line:
                    continue
                
                cat_id, cat_name, cat_age = line.strip().split(",")
                cat_record = {"id": cat_id, "name": cat_name, "age": cat_age}

                cats_list.append(cat_record)

            return cats_list
            
    except FileNotFoundError:
        return {}

script_directory = Path(__file__).parent

file_path = script_directory / "cats_file.txt"

cats = get_cats_info(file_path)
print(cats)