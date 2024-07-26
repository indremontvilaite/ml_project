# ML Project
## Objective
Develop and deploy a state-of-the-art classification model using advanced machine learning techniques.

## Dataset Description
The dataset provided is designed for a data classification problem. All columns are anonymized and categorized, with column names indicating feature indices and data types.

## Summary Report

### Data Preprocessing:
Data cleaning and simple EDA is done in the notebook [EDA](./EDA.ipynb). A summary of the work is presented here as well. 
EDA goals are:
- Perfom data quality checks, such as missing values, duplicates.
- Understand data types.
- Understand data distributions(descriptive metrics, outliers, data balance).
- Understand what data preprecesing steps to take before modeling.

#### Findings

- The data set is an event table where event is continious or interrapted connection. Most of the attributes in the data set are numeric type. The ones which are not numeric are:
    - datetime of an event. This attribute was rounded to minutes to remove duplicates by relevant subset.
    - 2 integer type attributes which might represend indication of different users or/and virtual machines, etc.
    - time zone attribute.
    - all other (over 300) attributes are float type. 

- Data cleaning. Data was cleaned by rounding timestamps to minutes and removing dublicated rows by subset of categorical attributes since the mail goal is to predict interrupted connections so intteruption and event before intterption should be the most valuable.
- Correlation across the columns. There was checked if there are identical columns in dataset and the correlation between them. As you can se from Descriptive statistics plot, there are some replicated patterns in attributes statistics. 

![Desc](./pictures/desr_plot.png)
Besides, there no duplicated collumns in the dataset (as it looks like for the first sight), however, some collumns have very high or even perfect correlation equal to 1. This indicates multicollinearity which is problem for model explainability(for Logistic regression model). Around 40 columns were removed from the dataset due to high correlation (over 0.99).

***Correllation matric of numeric attribus*** 
![Corr](./pictures/corr.png)
- Missing values. There are a lot of missing values in dataset, some attributes reaching over 99% of missings. The differences across missing values by event type is analysed to check if some missing values can be related to event type, like interruption.

***Missing values distribution differences between Interrupted and Continuous event*** 
![Missings](./pictures/missing_diff.png)
The results are showing that there are different distributions in missing values between event type, but any column had missing values just in one category. From descriptive statistics analysis, there is observed that the direffences between mean and median are quite huge for some attributtes even after outliers replacement with less extreme values. Due to that reason, meadian is selected as a value for missings imputing.

***Mean and Median values plot for numeric attributes***

![Mean median](./pictures/mean_median.png)
- Data balanse. The dataset is highly inbalance be event time. The interruptions consist 1.4% of original dataset and 6.4% of cleaned dataset. This suggest that data balancing techniques should be used while modeling.
- Outliers were replaced by less extreme values, 0.95 and 0.05 percentiles. Even after the hanling of outliers, we can se that the data is asymetric by the difference between average and median values.
---
### Feature Engineering:
Here are methods for selecting and transforming relevant features.
#### Handling missing values
Based on analysis done in EDA, median metric is selected for numeric attributes. For categorical, a new category is created. 
#### Encoding categorical variables
There are just 1 categorical attribute in the dataset, which indicates time zone. OneHotEncoding was used to handle categorical attribute.
#### Feature scaling and normalization
Standard scaler is used for numerical attributes.
#### Generating new features through feature interaction or domain knowledge
Besides the steps taken in data cleaning part(datetime attribe aggregation to minutes), new features generation was skip due to time constrains. Having more time, the first step would be to include laged attributes since the dependent attribute defines the status of the process, so previous information might be useful in forecasting the current state.
#### Handling imbalanced data
Since the dataset is highly imbalanced, SMOTE approach was chosen to balance tha data by oversampling the minority class while creating syntetic observations.
### Model Training and Development:
After the data preprocesing(including imputing missing values, scaling and OneHotEncoding), data was trained on 2 models.
#### Hyperparameter tuning methods and their outcomes
Bayes optimisation was selected for XGBoost hyperparameter tuning since it should outperfom other optimisation methods as GridSearchCV or RandomSeachCV.

---
#### Model selection and justification
**Logistic regression** model was chosen as a baseline model for classification problem. The Logistic regression is one of the simpliest models used for classification problem. It is relatively simple to compute and odds ratios show features impact to the model output (if multicollinearity is not present).
As a state-of-art model, **XGBoost model** was chosen since it outperforms other models by some researches and are suitable for time series data as well. 
#### Model evaluation
Several metrics were use for models' evaluation and comparison. 2 main metrics for classification problem are comfusion matrix and ROC curve. Since the data is imbalanced and there should be more important to correctly forecast cased than a process is interrupted istead of continuous event, the recall is chosen as the most important metric for model comparison.

|Model name | ROC AUC | Recall | Precision|
|----------------------------------------|----------|----------|----------|
|Logistic regression	|0.88|	0.81|	0.75|
|XGBoost basic	|0.94 |	0.50 |	0.96 |
|XGBoost with Bayes hyperparameter tuning	|0.93|	0.49 |	0.96|

Based on models' goodness of fit metrics, and Recall especially since it is the most important in this case, the best performance is from Logistic regression model, which is quite surprising. Logistic regression was used as a baseline model and any hyperparameter tuning is not performed. Moreover, Bayes optimisation for hyperparameters tuning has not improved XGBoost model performance. XGBoost models are forecasting with the same precision. However, XGBoost models have better ROC/AUC and precision than Logisting regression, the recall is the main metric here.

Models' overfitting was checked by comparing metrics from train and test sets, and they were very similar indicating low overfitting. For more legit results, a validation dataset(test dataset which model has not seen) should be used.

To improve models performance, the key part should be feature engineering there laged values should be created. In addition, other mdel types as TabNNs or Deep and Wide model from Keras.

#### Experiment Tracking
Git as version control system is used here. Going further, VSC is providing DVC extension for model tracking. Another tools to registter models and track experiments, that I have expierience working with, is MLFlow. This part was omitted due to time constrains and technology constrains.

