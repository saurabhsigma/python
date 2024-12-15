calculation_to_units = 24
name_of_unit = "hours"

def days_to_unit(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units } {name_of_unit}")
    print("All good!")

days_to_unit(35)
days_to_unit(20)