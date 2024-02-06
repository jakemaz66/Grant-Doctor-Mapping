# Grant Doctor Mapping 

## Overview
This project aims to match grants to doctors using a reusable classifier.

## Project Structure
'.vscode/RePORTER_PRJ_C_FY2022.zip': Contains the data
 'AuthorDoctorEntityResolver.py': Contains the resuable classifier class

## Setup
1. Clone the repository:
   ```bash
   git clone git@github.com:jakemaz66/Grant-Doctor-Mapping.git

## Notes
The 'Budget_Start" column in the dataset is missing a considerable number of values. For each missing value in the Budget_Start Column, there is also a corresponidng missing value in that row for the Budget_End Column. I have decided to impute the missing Budget_Start column values with the median of the column in order to accound for an unclear distribution. 
