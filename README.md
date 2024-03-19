# Entity Resolution Project README

## Table of Contents
1. [Overview](#overview)
2. [Tools Used](#tools-used)
3. [Data Cleaning](#data-cleaning)
4. [Classifier Building](#classifier-building)
5. [Database Setup](#database-setup)
6. [Training Data Simulation](#training-data-simulation)
7. [Deployment](#deployment)
8. [Usage](#usage)
9. [Contributing](#contributing)
10. [License](#license)

## Overview
This project focuses on entity resolution, specifically mapping grants to doctors from multiple datasets. The goal is to build a classifier that can predict matches between grants and doctors using various features such as the Jaro-Winkler distance between last names. The process involves reading in data, cleaning and preprocessing it, building and training a classifier, setting up a database to store connections, and deploying the classifier for matching purposes.

## Tools Used
- Python (programming language)
- Pandas (data manipulation)
- Scikit-learn (machine learning)
- SQLite (database)
- Jupyter Notebook (development environment)
- Git (version control)
- GitHub (code hosting and collaboration)

## Data Cleaning
The data cleaning phase involves preprocessing both the grants and doctors datasets. Tasks include handling missing values, standardizing formats (e.g., names, dates), and extracting relevant features for matching purposes.

## Classifier Building
We built a classifier using machine learning techniques to predict matches between grants and doctors. Features such as Jaro-Winkler distance between last names, common affiliations, and grant types are used to train the classifier.

## Database Setup
We set up an SQLite database to store our data and establish connections between grants and doctors. This database allows for efficient querying and retrieval of matched entities.

## Training Data Simulation
To train our classifier, we simulated training data by generating positive and negative samples of matched and unmatched pairs of grants and doctors. This simulated data helps improve the classifier's accuracy and generalization.

## Deployment
The trained classifier is deployed to perform real-time matching between grants and doctors. The deployment process ensures seamless integration with existing systems for efficient entity resolution.

## Usage
To use this project:
1. Clone the repository: `git clone https://github.com/yourusername/entity-resolution-project.git`
2. Install dependencies: `pip install -r requirements.txt`
