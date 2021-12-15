import pandas as pd
import statsmodels.api as sm


def display_regression_stats(table, predictor, response):

    y = table[response]
    x = table[predictor]

    # Add constant to predictor variables
    x = sm.add_constant(x)

    # Fit linear regression model
    model = sm.OLS(y, x).fit()

    # Display model summary
    print()
    print(f"{response} vs {predictor}: {model.f_pvalue}")
    print(model.summary())


all_metrics = pd.read_csv('all_metrics.csv')

health_infrastructure_indicators = [
    'Hospitals per 1,000 Population',
    'Community Health Centers per 1,000 Population',
    'Total beds per 1,000 Population',
    'ICU beds per 1,000 Population',
    'Total Primary Care Practitioners per 1,000 Population',
    'Percentage of Practitioners Needed Met']

for indicator in health_infrastructure_indicators:
    display_regression_stats(
        table=all_metrics,
        predictor=indicator,
        response='Deaths by 1,000 Population')
    display_regression_stats(
        table=all_metrics,
        predictor=indicator,
        response='Deaths by 1,000 Cases')
