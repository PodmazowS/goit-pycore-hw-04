def get_cats_info(path: str) -> list[dict[str, str]]:
    cats_list = []
    try:
        with open(path, 'r', encoding="utf-8") as f:
            cat_record = {}
            for line in f:
                cat_id, cat_name, cat_age = line.strip().split(",")
                cat_record = {"id": cat_id, "name": cat_name, "age": cat_age}

                cats_list.append(cat_record)

            return cats_list
            
    except FileNotFoundError as fh:
        return print(f"File not found in {fh}")


cats = get_cats_info("cats_file.txt")
print(cats)