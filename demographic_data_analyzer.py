import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv("adult.data.csv")

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    total = len(df)
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / total) * 100, 1)

    # 4. What percentage with advanced education make >50K?
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_edu_rich = df[higher_edu & (df['salary'] == '>50K')].shape[0]
    lower_edu_rich = df[~higher_edu & (df['salary'] == '>50K')].shape[0]
    higher_edu_total = df[higher_edu].shape[0]
    lower_edu_total = df[~higher_edu].shape[0]

    higher_education_rich = round((higher_edu_rich / higher_edu_total) * 100, 1)
    lower_education_rich = round((lower_edu_rich / lower_edu_total) * 100, 1)

    # 5. Minimum hours of work per week
    min_work_hours = df['hours-per-week'].min()

    # 6. What percentage of people who work minimum hours per week have >50K salary?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0]
    rich_percentage = round((rich_min_workers / num_min_workers.shape[0]) * 100, 1)

    # 7. Country with highest percentage of people earning >50K
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_rich_percentages = (rich_country_counts / country_counts) * 100
    highest_earning_country = country_rich_percentages.idxmax()
    highest_earning_country_percentage = round(country_rich_percentages.max(), 1)

    # 8. Most popular occupation for people >50K in India
    top_IN_occupation = df[(df['salary'] == '>50K') & 
                           (df['native-country'] == 'India')]['occupation'].mode()[0]

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India for those earning >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
