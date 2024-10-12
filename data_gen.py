import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seeds for reproducibility
np.random.seed(42)
random.seed(42)

# ---------------------------------------------
# 1. Generate Customer Data (customers.csv)
# ---------------------------------------------

num_customers = 5000

# Generate Customer IDs
customer_ids = [f"CUST{str(i).zfill(5)}" for i in range(1, num_customers + 1)]

# Age: 18 to 65 years
ages = np.random.randint(18, 66, size=num_customers)

# Gender: Skewed towards males (60% male, 40% female)
genders = np.random.choice(["Male", "Female"], size=num_customers, p=[0.6, 0.4])

# Income Levels
income_brackets = [
    (0, 20000),  # 10%
    (20000, 50000),  # 50%
    (50000, 100000),  # 30%
    (100000, 200000),  # 10%
]
income_probs = [0.1, 0.5, 0.3, 0.1]
income_levels = np.random.choice(
    len(income_brackets), size=num_customers, p=income_probs
)
incomes = [
    np.random.randint(income_brackets[i][0], income_brackets[i][1])
    for i in income_levels
]

# Employment Status
employment_statuses = np.random.choice(
    ["Employed", "Self-employed", "Unemployed"], size=num_customers, p=[0.6, 0.3, 0.1]
)

# Geographical Distribution
geographies = np.random.choice(["Urban", "Rural"], size=num_customers, p=[0.7, 0.3])

# Compile DataFrame
customers_df = pd.DataFrame(
    {
        "CustomerID": customer_ids,
        "Age": ages,
        "Gender": genders,
        "MonthlyIncome": incomes,
        "EmploymentStatus": employment_statuses,
        "Location": geographies,
    }
)

# Save to CSV
customers_df.to_csv("generated_files/customers.csv", index=False)

# ---------------------------------------------
# 2. Generate Loan Product Data (loan_products.csv)
# ---------------------------------------------

loan_products = [
    {
        "LoanType": "Normal Loan",
        "MinAmount": 50000,
        "MaxAmount": 1000000,
        "MinTerm": 12,
        "MaxTerm": 60,
        "InterestRate": 0.10,
        "Sector": "General",
    },
    {
        "LoanType": "Jipange Loan",
        "MinAmount": 20000,
        "MaxAmount": 500000,
        "MinTerm": 6,
        "MaxTerm": 36,
        "InterestRate": 0.08,
        "Sector": "Personal Development",
    },
    {
        "LoanType": "Maziwa Loan",
        "MinAmount": 20000,
        "MaxAmount": 500000,
        "MinTerm": 6,
        "MaxTerm": 36,
        "InterestRate": 0.09,
        "Sector": "Agriculture",
    },
    {
        "LoanType": "Avocado Loan",
        "MinAmount": 50000,
        "MaxAmount": 1000000,
        "MinTerm": 12,
        "MaxTerm": 60,
        "InterestRate": 0.11,
        "Sector": "Agriculture",
    },
    {
        "LoanType": "Green Energy Loan",
        "MinAmount": 20000,
        "MaxAmount": 500000,
        "MinTerm": 6,
        "MaxTerm": 36,
        "InterestRate": 0.07,
        "Sector": "Renewable Energy",
    },
    {
        "LoanType": "Boda Boda Loan",
        "MinAmount": 50000,
        "MaxAmount": 1000000,
        "MinTerm": 12,
        "MaxTerm": 60,
        "InterestRate": 0.12,
        "Sector": "Transport",
    },
    {
        "LoanType": "Salary Advance",
        "MinAmount": 10000,
        "MaxAmount": 100000,
        "MinTerm": 3,
        "MaxTerm": 12,
        "InterestRate": 0.05,
        "Sector": "Emergency",
    },
    {
        "LoanType": "Special Advance",
        "MinAmount": 10000,
        "MaxAmount": 100000,
        "MinTerm": 3,
        "MaxTerm": 12,
        "InterestRate": 0.06,
        "Sector": "Emergency",
    },
    {
        "LoanType": "Seasonal Advance",
        "MinAmount": 20000,
        "MaxAmount": 500000,
        "MinTerm": 6,
        "MaxTerm": 24,
        "InterestRate": 0.08,
        "Sector": "Seasonal Business",
    },
    {
        "LoanType": "Emergency Loan",
        "MinAmount": 10000,
        "MaxAmount": 50000,
        "MinTerm": 3,
        "MaxTerm": 12,
        "InterestRate": 0.09,
        "Sector": "Emergency",
    },
    {
        "LoanType": "Additional Loan",
        "MinAmount": 10000,
        "MaxAmount": 500000,
        "MinTerm": 6,
        "MaxTerm": 36,
        "InterestRate": 0.10,
        "Sector": "Various",
    },
]

loan_products_df = pd.DataFrame(loan_products)
loan_products_df.to_csv("generated_files/loan_products.csv", index=False)

# ---------------------------------------------
# 3. Generate Loan Data (loans.csv)
# ---------------------------------------------

num_loans = 10000

# Loan IDs
loan_ids = [f"LOAN{str(i).zfill(6)}" for i in range(1, num_loans + 1)]

# Randomly assign loan types
loan_types = np.random.choice(loan_products_df["LoanType"], size=num_loans)

# Map loan types to product details
product_details = loan_products_df.set_index("LoanType").to_dict("index")

# Generate loan amounts, terms, interest rates, and disbursement dates
loan_amounts = []
loan_terms = []
interest_rates = []
disbursement_dates = []

start_date = datetime(2019, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = (end_date - start_date).days

for loan_type in loan_types:
    details = product_details[loan_type]
    amount = np.random.randint(details["MinAmount"], details["MaxAmount"] + 1)
    term = np.random.randint(details["MinTerm"], details["MaxTerm"] + 1)
    rate = details["InterestRate"]
    disbursement_day = start_date + timedelta(days=np.random.randint(0, date_range + 1))
    loan_amounts.append(amount)
    loan_terms.append(term)
    interest_rates.append(round(rate, 4))
    disbursement_dates.append(disbursement_day.strftime("%Y-%m-%d"))

# Approval Turnaround Time
approval_times = []
for idx in range(num_loans):
    if loan_amounts[idx] <= 100000:  # Quick loans
        approval_time = np.random.randint(1, 4)
    else:  # Large loans
        approval_time = np.random.randint(7, 15)
    approval_times.append(approval_time)

# Compile DataFrame
loans_df = pd.DataFrame(
    {
        "LoanID": loan_ids,
        "CustomerID": np.random.choice(customers_df["CustomerID"], size=num_loans),
        "LoanType": loan_types,
        "LoanAmount": loan_amounts,
        "LoanTermMonths": loan_terms,
        "InterestRate": interest_rates,
        "DisbursementDate": disbursement_dates,
        "ApprovalTimeDays": approval_times,
    }
)

# Save to CSV
loans_df.to_csv("generated_files/loans.csv", index=False)

# ---------------------------------------------
# 4. Generate Repayment Data (repayments.csv)
# ---------------------------------------------

num_repayments = 50000

# Select loans to generate repayments for
repayment_loans = loans_df.sample(n=num_repayments, replace=True).reset_index(drop=True)


# Define the monthly payment calculation function
def calculate_monthly_payment(principal, annual_rate, term_months):
    monthly_rate = annual_rate / 12  # Convert annual rate to monthly
    if monthly_rate == 0:
        payment = principal / term_months
    else:
        payment = (
            principal
            * (monthly_rate * (1 + monthly_rate) ** term_months)
            / ((1 + monthly_rate) ** term_months - 1)
        )
    return payment


# Initialize lists to store repayment data
repayment_amounts = []
repayment_dates = []
repayment_statuses = []

status_choices = ["On Time", "Late", "Defaulted", "Prepaid"]
status_probs = [0.8, 0.1, 0.05, 0.05]

for idx, row in repayment_loans.iterrows():
    # Calculate the monthly repayment amount
    amount = calculate_monthly_payment(
        row["LoanAmount"], row["InterestRate"], row["LoanTermMonths"]
    )
    repayment_amounts.append(round(amount, 2))

    # Generate repayment dates based on disbursement date
    disb_date = datetime.strptime(row["DisbursementDate"], "%Y-%m-%d")
    payment_number = np.random.randint(1, row["LoanTermMonths"] + 1)
    payment_date = disb_date + timedelta(days=30 * payment_number)
    repayment_dates.append(payment_date.strftime("%Y-%m-%d"))

    # Assign repayment status
    status = np.random.choice(status_choices, p=status_probs)
    repayment_statuses.append(status)

# Payment Methods
payment_methods = np.random.choice(
    ["M-Pesa", "Bank Transfer", "Cash"], size=num_repayments, p=[0.9, 0.05, 0.05]
)

# Compile DataFrame
repayments_df = pd.DataFrame(
    {
        "RepaymentID": [f"RP{str(i).zfill(7)}" for i in range(1, num_repayments + 1)],
        "LoanID": repayment_loans["LoanID"],
        "RepaymentDate": repayment_dates,
        "RepaymentAmount": repayment_amounts,
        "RepaymentStatus": repayment_statuses,
        "PaymentMethod": payment_methods,
    }
)

# ---------------------------------------------
# Introduce Data Anomalies in Repayments
# ---------------------------------------------

# Overpayments (1% of repayments)
overpayment_indices = repayments_df.sample(frac=0.01, random_state=42).index
repayments_df.loc[overpayment_indices, "RepaymentAmount"] *= np.random.uniform(
    1.1, 1.5, size=len(overpayment_indices)
)

# Refunds (0.5% of repayments)
refund_indices = repayments_df.sample(frac=0.005, random_state=24).index
repayments_df.loc[
    refund_indices, "RepaymentAmount"
] *= -1  # Negative amount to indicate refund

# Save to CSV
repayments_df.to_csv("generated_files/repayments.csv", index=False)

# ---------------------------------------------
# 5. Generate Collections Data (collections.csv)
# ---------------------------------------------

# Filter loans that are overdue (Repayment Status 'Late' or 'Defaulted')
overdue_repayments = repayments_df[
    repayments_df["RepaymentStatus"].isin(["Late", "Defaulted"])
]

# Remove duplicates to avoid multiple collections for the same repayment
overdue_repayments = overdue_repayments.drop_duplicates(
    subset=["LoanID", "RepaymentDate"]
)

# Assume collection attempts are made
collection_attempts = overdue_repayments.reset_index(drop=True)

collection_methods = np.random.choice(
    ["Phone", "SMS", "In-person"], size=len(collection_attempts), p=[0.5, 0.3, 0.2]
)
collection_results = np.random.choice(
    ["Success", "Failure"], size=len(collection_attempts), p=[0.6, 0.4]
)

# Compile DataFrame
collections_df = pd.DataFrame(
    {
        "CollectionID": [
            f"COL{str(i).zfill(6)}" for i in range(1, len(collection_attempts) + 1)
        ],
        "LoanID": collection_attempts["LoanID"],
        "CollectionDate": collection_attempts["RepaymentDate"],
        "CollectionMethod": collection_methods,
        "CollectionResult": collection_results,
    }
)

# Save to CSV
collections_df.to_csv("generated_files/collections.csv", index=False)

# ---------------------------------------------
# 6. Generate Loan Seasonality Data (loan_seasonality.csv)
# ---------------------------------------------

# Create a DataFrame to represent seasonality
seasonality_records = []

# Define months for peaks
avocado_peak_months = [4, 5, 10, 11]  # April-May, October-November
transport_peak_months = [12]  # December for festive season

for year in range(2019, 2025):
    for month in range(1, 13):
        date_str = f"{year}-{month:02d}"
        avocado_demand = 1.5 if month in avocado_peak_months else 1.0
        transport_demand = 1.5 if month in transport_peak_months else 1.0
        seasonality_records.append(
            {
                "Month": date_str,
                "AvocadoLoanDemandIndex": avocado_demand,
                "TransportLoanDemandIndex": transport_demand,
            }
        )

seasonality_df = pd.DataFrame(seasonality_records)
seasonality_df.to_csv("generated_files/loan_seasonality.csv", index=False)

# ---------------------------------------------
# 7. Generate Customer Satisfaction Data (customer_satisfaction.csv)
# ---------------------------------------------

num_feedback = 1000  # Number of feedback records

feedback_customers = np.random.choice(customers_df["CustomerID"], size=num_feedback)

ratings_choices = [5, 4, 3, 2, 1]
ratings_probs = [0.35, 0.35, 0.20, 0.05, 0.05]
ratings = np.random.choice(ratings_choices, size=num_feedback, p=ratings_probs)

comments_pool = [
    "Great service",
    "Quick approval",
    "Need better communication",
    "Very satisfied",
    "Could be improved",
    "Friendly staff",
    "Long wait times",
    "Excellent experience",
    "Unhappy with the service",
    "Will recommend to others",
]
comments = np.random.choice(comments_pool, size=num_feedback)

# Compile DataFrame
satisfaction_df = pd.DataFrame(
    {
        "FeedbackID": [f"FB{str(i).zfill(6)}" for i in range(1, num_feedback + 1)],
        "CustomerID": feedback_customers,
        "Rating": ratings,
        "Comment": comments,
    }
)

# Save to CSV
satisfaction_df.to_csv("generated_files/customer_satisfaction.csv", index=False)

# ---------------------------------------------
# 8. Ensure Even Distribution Over 5 Years
# ---------------------------------------------

# The disbursement dates and repayment dates are already spread evenly over the 5-year period in the code above.

# ---------------------------------------------
# 9. Final Notes
# ---------------------------------------------

print("Data generation complete. CSV files have been saved.")
