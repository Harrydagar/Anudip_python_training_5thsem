# Salary Calculator

basic_salary = float(input("Enter Basic Salary: ₹"))

# Validation
if basic_salary < 0:
    exit("Salary cannot be negative")

# Components
hra = basic_salary * 0.20      # 20% HRA (House Rent Allowance)
da = basic_salary * 0.10       # 10% DA (Dearness Allowance)
pf = basic_salary * 0.12       # 12% PF Deduction (Provident Fund)

# Salary Calculations
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

# Grade Determination
if net_salary > 50000:
    grade = "Senior Grade"
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

# Output
print("\n------ Salary Details ------")
print("Basic Salary : ₹", basic_salary)
print("HRA          : ₹", hra)
print("DA           : ₹", da)
print("PF Deduction : ₹", pf)
print("Gross Salary : ₹", gross_salary)
print("Net Salary   : ₹", net_salary)
print("Grade        :", grade)