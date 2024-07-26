# ML Project
## Objective
Develop and deploy a state-of-the-art classification model using advanced machine learning techniques.

## Dataset Description
The dataset provided is designed for a data classification problem. All columns are anonymized and categorized, with column names indicating feature indices and data types.

## Summary Report

### Data Preprocessing:
Data cleaning and simple EDA is done in the notebook [EDA](./EDA.ipynb). A summary of the work is presented here as well. 
EDA goals are:
- Perfom data quality checks, such as missing values, duplicates
- Understand data types
- Understand data distributions(descriptive metrics, outliers, data balance)


### Feature Engineering:
Methods for selecting and transforming relevant features, including:
Handling missing values
#### Encoding categorical variables
There are just 1 categorical attribute in the dataset which indicates time zone. OneHotEncoding was used to handle categorical attribute.
#### Feature scaling and normalization
Standard scaler is used for numerical attributes.
#### Generating new features through feature interaction or domain knowledge
Besides the steps taken in data cleaning part(datetime attribe aggregation to minutes), new features generation was skip due to time constrains. Having more time, the first step would be to include laged attributes since the dependent attribute defines the status of the process, so previous information might be useful in forecasting the current state.
#### Handling imbalanced data
Since the dataset is highly imbalanced, SMOTE approach was chosen to balance tha data by oversampling the minority class while creating syntetic observations.
### Model Training and Development:
After the data preprocesing(including imputing missing values, scaling and OneHotEncoding), data was trained on 2 models.
#### Model selection and justification
**Logistic regression** model was chosen as a baseline model for classification problem. The Logistic regression is one of the simpliest models used for classification problem. It is relatively simple to compute and odds ratios show features impact to the model output (if multicollinearity is not present).
As a state-of-art model, **XGBoost model** was chosen since it outperforms other models by some researches and are suitable for time series data as well. 
#### Model evaluation
Several metrics were use for models' evaluation and comparison. 2 main metrics for classification problem are comfusion matrix and ROC curve. Since the data is imbalanced and there should be more important to correctly forecast cased than a process is interrupted istead of continuous event, the recall is chosen as the most important metric for model comparison. 
#### Hyperparameter tuning methods and their outcomes
Bayes optimisation was selected for XGBoost hyperparameter tuning since it should outperfom other optimisation methods as GridSearchCV or RandomSeachCV.

#### Experiment Tracking
Git as version control system is used here. Going further, VSC is providing DVC extension for model tracking. Another tools to registter models and track experiments, that I have expierience working with, is MLFlow. This part was omitted due to time constrains and technology constrains.

