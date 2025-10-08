from statistics import median


def analyse_scores(scores):
    if not scores:
        return {"error": "No scores provided"}
    
    number_of_scores = len(scores)
    #percentage = 
    the_median = median(scores)
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    
    # Count grades
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for score in scores:
        if score >= 90:
            grade_counts["A"] += 1
        elif score >= 80:
            grade_counts["B"] += 1
        elif score >= 70:
            grade_counts["C"] += 1
        elif score >= 60:
            grade_counts["D"] += 1
        else:
            grade_counts["F"] += 1
    
    return {
        "Percentage of A's," : f'{(grade_counts["A"]/number_of_scores)*100}%',
        "Percentage of B's," : f"{(grade_counts["B"]/number_of_scores)*100}%",
        "Percentage of C's," : f"{(grade_counts["C"]/number_of_scores)*100}%",
        "Percentage of D's," : f"{(grade_counts["D"]/number_of_scores)*100}%",
        "Percentage of F's," : f"{(grade_counts["F"]/number_of_scores)*100}%",
        "Passing Rate:," : f"{(((grade_counts["A"]+grade_counts["B"]+grade_counts["C"]+grade_counts["D"])/number_of_scores)*100)}%",
        "Median" : the_median,
        "Average": round(average, 2),
        "Highest": highest,
        "Lowest": lowest,
        "Total Students": len(scores),
        "Grade Distribution": grade_counts
    }

# Test data
test_scores = [85, 92, 78, 90, 87, 95, 82, 88, 91, 79]
empty_list = []

print("Test Results:")
print(analyse_scores(test_scores))
print("\nEmpty List Test:")
print(analyse_scores(empty_list))