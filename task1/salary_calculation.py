from pathlib import Path

def total_salary(path: str) -> tuple[int, float]:
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding="utf-8") as f:
            for line in f:
                stripped_line = line.strip()

                #skipping empty line
                if not stripped_line:
                    continue

                name, salary = line.split(',')

                total += int(salary)
                count += 1

            #returning empty tuple if file is empty
            if count == 0:
                return (0, 0.0)

            average = total/count

            result = (total, average)

            return result
        
    except (FileNotFoundError, FileExistsError, ValueError):
        return (0,0.0)

dir_path = Path(__file__).parent

file_path = dir_path / "salary_file.txt"

salary_sum, salary_avg = total_salary(file_path)
print(f"Total salary is: {salary_sum} and average salary is: {salary_avg}")