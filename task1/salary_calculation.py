def total_salary(path: str) -> tuple[int, float]:
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding="utf-8") as f:
            for line in f:
                name, salary = line.strip().split(',')

                total += int(salary)
                count += 1

            average = total/count

            result = (total, average)

            return result
        
    except (FileNotFoundError, FileExistsError) as fe:
        print(f"File was not found, please check: {fe}")

salary_sum, salary_avg = total_salary("salary_file.txt")
print(f"Total salary is: {salary_sum} and average salary is: {salary_avg}")