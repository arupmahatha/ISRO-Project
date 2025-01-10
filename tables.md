
# Statistical Summary of Oceanographic Variables

    This table presents the coefficients, intercepts, R² values, mean squared errors (MSE), and sample sizes for various oceanographic variables. These statistics are essential for understanding the relationships between the variables and their predictive capabilities.

    | Feature   | Coefficient | Intercept | R²     | MSE    | Sample Size |
    |-----------|-------------|-----------|--------|--------|-------------|
    | thetao    | 0.0216     | -0.2397   | 0.0637 | 0.0533 | 837         |
    | so        | -0.0157    | 0.8038    | 0.0588 | 0.0536 | 837         |
    | uo        | 0.2795     | 0.3610    | 0.0323 | 0.0551 | 837         |
    | vo        | -0.1792    | 0.3591    | 0.0049 | 0.0567 | 837         |
    | wo        | -49.5334   | 0.3620    | 0.0000 | 0.0570 | 837         |
    | kd        | 10.6336    | -0.2561   | 0.7170 | 0.0161 | 837         |
    | ph        | -0.2770    | 2.6042    | 0.0039 | 0.0567 | 837         |
    | spco2     | -0.0048    | 0.5176    | 0.0117 | 0.0563 | 837         |
    | o2        | -0.0029    | 0.9749    | 0.0186 | 0.0559 | 837         |
    | no3       | 0.0194     | 0.3163    | 0.0546 | 0.0539 | 837         |
    | po4       | 2.0907     | 0.3452    | 0.0118 | 0.0563 | 837         |
    | si        | 0.0152     | 0.3259    | 0.0036 | 0.0568 | 837         |
    | fe        | 64.8834    | 0.2081    | 0.2080 | 0.0451 | 837         |



# Variance Inflation Factors (VIF)

    This table presents the Variance Inflation Factors for the oceanographic variables, which helps to identify multicollinearity in the regression model.

    | Variable | VIF            |
    |----------|----------------|
    | ph       | 18637.945260   |
    | o2       | 7592.157342    |
    | thetao   | 2406.430547    |
    | so       | 1086.004117    |
    | spco2    | 891.899284     |
    | kd       | 18.775604      |
    | si       | 16.852081      |
    | fe       | 5.807439       |
    | no3      | 4.731273       |
    | po4      | 1.935344       |
    | uo       | 1.205261       |
    | vo       | 1.129519       |
    | wo       | 1.051415       |



# OLS Regression Results

    This table presents the Ordinary Least Squares (OLS) regression results for the dependent variable 'chl'. The coefficients, standard errors, t-values, p-values, and confidence intervals are provided for each predictor variable. The R-squared value indicates the proportion of variance in the dependent variable that can be explained by the independent variables.

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                    chl   R-squared:                       0.770
    Model:                            OLS   Adj. R-squared:                  0.765
    Method:                 Least Squares   F-statistic:                     168.7
    Date:                Sun, 29 Dec 2024   Prob (F-statistic):          5.13e-199
    Time:                        19:36:40   Log-Likelihood:                 496.52
    No. Observations:                 669   AIC:                            -965.0
    Df Residuals:                     655   BIC:                            -902.0
    Df Model:                          13                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const         -2.7562      3.418     -0.806      0.420      -9.468       3.955
    thetao        -0.0051      0.010     -0.536      0.592      -0.024       0.014
    so             0.0146      0.006      2.468      0.014       0.003       0.026
    uo             0.1220      0.033      3.719      0.000       0.058       0.186
    vo             0.0431      0.051      0.851      0.395      -0.056       0.142
    wo          1468.1934   3203.971      0.458      0.647   -4823.099    7759.486
    kd            10.5459      0.325     32.449      0.000       9.908      11.184
    ph             0.5149      0.392      1.313      0.190      -0.255       1.285
    spco2         -0.0077      0.004     -1.841      0.066      -0.016       0.001
    o2            -0.0081      0.002     -4.120      0.000      -0.012      -0.004
    no3            0.0053      0.003      2.110      0.035       0.000       0.010
    po4           -1.8393      0.432     -4.261      0.000      -2.687      -0.992
    si             0.0046      0.008      0.595      0.552      -0.011       0.020
    fe            18.4705      4.715      3.918      0.000       9.213      27.728
    ==============================================================================
    Omnibus:                      207.720   Durbin-Watson:                   1.937
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):              991.358
    Skew:                           1.327   Prob(JB):                    5.36e-216
    Kurtosis:                       8.341   Cond. No.                     1.56e+08
    ==============================================================================

    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 1.56e+08. This might indicate that there are
    strong multicollinearity or other numerical problems.

    R^2 Score for Linear Regression: 0.7624



# Robust Regression (Huber) Results:

    This table presents the results of the Robust Linear Model (RLM) regression using the Huber method. It includes coefficients, standard errors, z-values, p-values, and confidence intervals for each predictor variable. The robust regression is particularly useful for handling outliers in the data.

                        Robust linear Model Regression Results                    
    ==============================================================================
    Dep. Variable:                    chl   No. Observations:                  669
    Model:                            RLM   Df Residuals:                      655
    Method:                          IRLS   Df Model:                           13
    Norm:                          HuberT                                         
    Scale Est.:                       mad                                         
    Cov Type:                          H1                                         
    Date:                Sun, 29 Dec 2024                                         
    Time:                        19:36:41                                         
    No. Iterations:                    41                                         
    ==============================================================================
                    coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const         -3.0569      2.503     -1.221      0.222      -7.962       1.848
    thetao         0.0006      0.007      0.085      0.932      -0.013       0.014
    so             0.0125      0.004      2.882      0.004       0.004       0.021
    uo             0.0659      0.024      2.744      0.006       0.019       0.113
    vo             0.0085      0.037      0.230      0.818      -0.064       0.081
    wo           656.8804   2345.878      0.280      0.779   -3940.956    5254.717
    kd             9.9942      0.238     42.000      0.000       9.528      10.461
    ph             0.4736      0.287      1.649      0.099      -0.089       1.036
    spco2         -0.0063      0.003     -2.051      0.040      -0.012      -0.000
    o2            -0.0056      0.001     -3.905      0.000      -0.008      -0.003
    no3            0.0037      0.002      2.011      0.044    9.51e-05       0.007
    po4           -1.9884      0.316     -6.292      0.000      -2.608      -1.369
    si             0.0027      0.006      0.471      0.637      -0.009       0.014
    fe            12.7697      3.452      3.699      0.000       6.004      19.535
    ==============================================================================

    If the model instance has been used for another fit with different fit parameters, then the fit options might not be the correct ones anymore .

    R^2 Score for Robust Linear Regression: 0.7628



# Neural Network Results:
    Training MSE: 0.0000
    Testing MSE: 0.0119
    Training R2: 1.0000
    Testing R2: 0.7794



# Random Forest Results:
    Training MSE: 0.0015
    Testing MSE: 0.0098
    Training R2: 0.9734
    Testing R2: 0.8170



# Ensemble Model Results:
    Training MSE: 0.0004
    Testing MSE: 0.0088
    Training R2: 0.9935
    Testing R2: 0.8368



# SHAP Values for Lowest and Highest Predictions

    This table summarizes the SHAP (SHapley Additive exPlanations) values for the features contributing to the lowest and highest predictions made by the model. SHAP values help in understanding the impact of each feature on the model's predictions.

    | Feature | Lowest Prediction SHAP Value | Highest Prediction SHAP Value |
    |---------|------------------------------|-------------------------------|
    | thetao  | -0.005664                    | 0.014712                      |
    | so      | -0.000830                    | 0.003333                      |
    | uo      | -0.006064                    | 0.054601                      |
    | vo      | -0.002407                    | 0.004767                      |
    | wo      | -0.001455                    | 0.000458                      |
    | kd      | -0.160058                    | 0.826507                      |
    | ph      | -0.002156                    | -0.000026                     |
    | spco2   | -0.000388                    | 0.006182                      |
    | o2      | -0.003871                    | 0.013861                      |
    | no3     | -0.002629                    | 0.001656                      |
    | po4     | 0.004132                     | 0.003153                      |
    | si      | -0.006197                    | -0.001095                     |
    | fe      | -0.024966                    | 0.014132                      |
