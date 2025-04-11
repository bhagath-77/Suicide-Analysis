# Suicide-Analysis

Suicide death rates analysis and api is a data engineering project aimed at demonstrating real world skills in data collection cleaning analysis and api development. 
The project takes raw public health data on suicide death rates in the United States, processes it through an end to end ETL pipeline, explores key insights via visual analytics, and exposes the cleaned data through a fast API based RESTful API.

#### Step 1(ETL)

1) Importing pandas, a powerful python library for data manipulation and analysis .
2) Define a function clean _data() To execute your ETL steps in an organized way.
3)Read the data using pd read _csv(). Specify the path where the file is situated at.
4)Print the first few rows of the data set to get a brief overview.
5)Clean the data to remove irrelevant data on to bring consistency.
      Spaces
      Convert data to lower case 
      Removing spatial characters
6)Dropping the missing critical data on the specific columns.
7) the columns for clarity.
8)Save the clean data.
9)Execute the function by calling.


#### Step 2(API Integration)
Loads the clean suicide rates data from data/ clean _suicide_rates .Csv
Initializes fast api application with title, description, and version.
Provides multiple api endpoints:
  /- Welcome route with available API paths
  /all - Returns the entire dataset.
  /year/{year}- Filter data by year.
  /age/{age_group} - Filter data by age groups.
  /demographic/{demographic_group} - Filter data by demographic group.
  /years - list All available years 
  /age- groups - list all the available age groups
  /demographics - List all demographic groups.
Handles errors with clear messages if no data is found.
Auto- generates api documentation at /docs for easy testing.



 #### Strp 3(EDA)- Exploratory data analysis to explore the data and to extract the insights before we build any dashboards models or apis.
 ##### 1 : Cumulative death rate by age group.
    Description:
    This bar chart visualizes the total cumulative suicide death rate across different age groups.
     It clearly shows that:
        -> Older age groups 65 years and over 85 years and over and the board category of all ages  have the highest cumulative impact.
        ->  Middle aged groups such as fortify to 64 yrs and 25 to 45 yrs also show significantly high cumulative totals.
        -> Younger age groups 10 to 14 years and 15 to 19 years contribute less to the total but they are still important for prevention effort.
     Insight:
     AGE IS strong risk factor, with cumulative impact being highest in the older population segments.
#### 2 : Average Death rate by age group.
    Descrption:
    This horizontal bar chart displays the average suicide death rate per age group.
    it highlights :
    -> The 85 years and over group experiences the highest average death rate( 34.5 per 100,000).
    -> Other older age groups like 75 to 84 yrs and 65 to 74 yrs also show high average death rates.
    -> Younger age groups 10 to 14 years and 15 to 19 years show comparatively low average rates.
    Insight:
    The elderly population faces the highest suicide risk on average, indicating a need for a targeted mental health support.
#### 3 : Death rate trends overtime by age group
    Description:
    This multi - line chart visualizes the suicide death rate trends over time across different age groups.
    It shows that:
    -> The elderly 85 years and over have consistently had the highest rates, with noticeable spikes.
    -> Middle - aged groups maintain moderate rates with some fluctuations over the years.
    -> The youngest groups ten to fourteen years remains at the lowest levels but show a slight increase in recent years.
    Insight:
    Suicide rates in older populations remain persistently high over time while younger age groups show stable but slowly rising trend, warranting preventive action.
