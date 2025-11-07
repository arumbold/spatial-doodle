# Introducing North Sussex Judo
## ATHLETE Algorithm Design block

This file describes the end-to-end algorithm process

## (START)
### Athlete data

```
name
training_plan
current_weight
competition_weight_category
competitions_entered
coaching_hours (optional)
```
[Back](../README.md#start)


#### Validation Rules for athlete data

```
Limited private coaching_hours (MAX 5 hours per week)
Competition entry RESTRICTED to Intermediate and Elite
Competitions held on second saturday each month 
Prices and Costs as currency, with precision of 2 Decimal Places
Data Validation is required for these input fields.
Validation errors "should prompt the user to re-enter"(Assignment Brief, 2025)
User errors should "display suitable messages"(Assignment Brief, 2025)
Months are 4 weeks in length
```
[Back](../README.md#validation-and-processing)


#### Process to register a new athlete
```
If the user does not already exist, present the option to create.
```
[Back](../README.md#validation-and-processing)


#### Process to create the reports
```
itemised list [of all costs for the month]
total cost of training and competitions for the month
how their current weight compares to their competition weight category.
```
[Back](../README.md#process-output-data)


### Report contents
```
name
itemised_cost_list
monthly_cost
weight
competition_weight_category
```
[Back](../README.md#process-output-data)

## (END)