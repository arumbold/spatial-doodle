# Author: Aaron Rumbold
# Course: HND Digital Technologies for England (Cyber Security)
# 		  Unit 4 - Programming (2025)
# License: MIT

import decimal
from api.load_data import athlete_data
from api.data_processing import calculate_competition_weight_category
from api.data_processing import generate_cost_list
from api.file_handling import save_report_to_file
from api.file_handling import save_csv_to_file

name="report.py"
print(f'{name}::{__name__}')

class AthleteReport:
    def __init__(self, athlete_name, cost_list, athlete_weight, compitition_weight_category):
        self.athlete_name = athlete_name
        self.cost_list = cost_list
        self.athlete_weight = athlete_weight
        self.competition_weight_category = compitition_weight_category
    
    def create_summary(self):
        summary = f"Athlete Report for {self.athlete_name}\n"
        summary += f"Weight: {self.athlete_weight} kg\n"
        summary += f"Competition Weight Category: {self.competition_weight_category}\n"
        summary += "Cost List:\n"
        for cost in self.cost_list:
            summary += f" - {cost}\n"
        return summary
    
    def create_CSV(self):
        csv_data = "Description,Amount\n"
        for cost in self.cost_list:
            csv_data += f"{cost.description},{cost.amount}\n"
        return csv_data


class BillItem:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
    
    def __str__(self):
        return f"{self.description}: ${self.amount:.2f}"

def create_report(command_arguments=None):
    if command_arguments is None:
        command_arguments = []
    elif len(command_arguments) < 2:
        print("No athlete name provided for report generation.")
        return
    athlete_name = command_arguments[1]
    athlete_info = athlete_data.get(athlete_name)
    if athlete_info is None:
        print(f"Athlete '{athlete_name}' not found.")
        return
    athlete_weight = athlete_info.get("weight_kg")
    competition_weight_category = calculate_competition_weight_category(athlete_weight)
    cost_list = generate_cost_list(athlete_info)
    report = AthleteReport(athlete_name, cost_list, athlete_weight, competition_weight_category
    )
    report_summary = report.create_summary()
    report_csv = report.create_CSV()

    save_report_to_file(athlete_name, report_summary)
    save_csv_to_file(athlete_name, report_csv)

    
    print("Creating Athlete Report...")



__all__ = [create_report]