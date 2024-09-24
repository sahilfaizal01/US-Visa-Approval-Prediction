# US-Work-Visa-Approval-Prediction
End-to-End MLOps

## Problem Statement
Given certain set of feature such as continent, education, job_experience, training, employment, current age etc.

## Some Features:
* case_id:- ID of each visa application
* continent:- Information of continent the employee
* education_of_employee:- Information of education of the employee
* has_job_experience:- Does the employee has any job experience? Y= Yes; N = No
* requires_job_training:- Does the employee require any job training? Y = Yes; N = No
* no_of_employees:- Number of employees in the employer's company
* yr_of_estab:- Year in which the employer's company was established
* region_of_employment:- Information of foreign worker's intended region of employment in the US.
* prevailing_wage:- Average wage paid to similarly employed workers in a specific occupation in the area of intended employment. The purpose of the prevailing wage is to ensure that the foreign worker is not underpaid compared to other workers offering the same or similar service in the same area of employment.
* unit_of_wage:- Unit of prevailing wage. Values include Hourly, Weekly, Monthly, and Yearly.
* full_time_position:- Is the position of work full-time? Y = Full Time Position; N = Part Time Position
* case_status:- Flag indicating if the Visa was certified or denied


## Solution Scope:
This can be used on real life by US visa applicants so that they can improve their application for the approval process

## Solution Approach
ML Classification Algorithms
  
## Proposed Solution
ML powered solution
1. Load the data from DB
2. Perform EDA and feature engineering to select the desirable features
3. Fit the ML classification algorithm and finds out which one performs better
4. Select the top few and tune hyperparameters
5. Select the best model based on desired metrics
