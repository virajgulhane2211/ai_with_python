# Pandas DataFrame Demo
try:
    import pandas as pd
    df = pd.DataFrame({"Name":["Asha","Ravi","Meena"], "Marks":[80,35,67]})
    print(df)
    print(df[df["Marks"] >= 40])
except ImportError:
    print("Install Pandas: pip install pandas")
