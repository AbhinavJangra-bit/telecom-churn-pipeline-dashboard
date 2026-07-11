SELECT 
    customerID,
    gender,
    SeniorCitizen,
    Partner,
    Dependents,
    tenure,
    Contract,
    PaperlessBilling,
    PaymentMethod,
    MonthlyCharges,
    -- 1. Structural Data Fix: Handle text-based empty strings in TotalCharges safely
    CASE 
        WHEN TotalCharges = ' ' THEN 0.0 
        ELSE CAST(TotalCharges AS REAL) 
    END AS TotalCharges,
    -- 2. Mine Service Risk Profiles: Combine high-risk streaming traits
    CASE 
        WHEN StreamingTV = 'Yes' AND StreamingMovies = 'Yes' THEN 'Heavy Streamer'
        WHEN StreamingTV = 'Yes' OR StreamingMovies = 'Yes' THEN 'Basic Streamer'
        ELSE 'No Streaming Services'
    END AS streaming_profile,
    -- 3. Core Support Metric: Check if they are missing critical protective features
    CASE 
        WHEN TechSupport = 'Yes' AND OnlineSecurity = 'Yes' THEN 'Fully Protected'
        WHEN TechSupport = 'Yes' OR OnlineSecurity = 'Yes' THEN 'Partially Protected'
        ELSE 'No Support Features'
    END AS protection_tier,
    -- 4. Target Label
    Churn
FROM 
    customer_churn;