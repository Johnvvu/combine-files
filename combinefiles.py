import pandas as pd
import glob, os

dir = input("Please type in the full directory path to the CSVs:").strip()
all_files = glob.glob(dir + "/*.csv")

fn_choice = input("\nDo you want to include the filename as a new field in the dataset? (y or n)").strip()

if fn_choice.lower() == 'y':
    df = pd.concat([pd.read_csv(f).assign(filename=os.path.basename(f).split('.')[0]) for f in all_files], sort=False)
else:
    df = pd.concat((pd.read_csv(f) for f in all_files), sort=False)
    
out_choice = input("\nDo you want to save the combined files to a CSV or Excel file?\n\n1. Excel file\n2. CSV File\n\nChoose 1 or 2:").strip()

if out_choice == '1':
    df.to_excel("combined_files.xlsx", index=False)
    print("\nTask Completed.  Combined_files.xlsx has has been saved to: " + os.getcwd())
else:
    df.to_csv("combined_files.csv", index=False)
    print("\nTask Completed.  Combined_files.csv has has been saved to: " + os.getcwd())
