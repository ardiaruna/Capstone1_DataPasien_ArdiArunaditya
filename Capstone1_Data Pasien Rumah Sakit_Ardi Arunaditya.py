from tabulate import tabulate
import pyinputplus as pyip
import math

patient_data = [
    {"Code": "IH1",
     "Name": "Intan Hassanah",
     "Gender (M/F)": "F",
     "Age": 25,
     "Height (cm)": 160,
     "Weight (kg)": 40},

    {"Code": "W2",
     "Name": "Waluyo",
     "Gender (M/F)": "M",
     "Age": 40,
     "Height (cm)": 166,
     "Weight (kg)": 80},

    {"Code": "ZP3",
     "Name": "Zulaikha Purnawati",
     "Gender (M/F)": "F",
     "Age": 29,
     "Height (cm)": 155,
     "Weight (kg)": 57}
]

def get_name(patient_data):
    return patient_data["Name"]

def get_gender(patient_data):
    return patient_data["Gender (M/F)"]

def get_age(patient_data):
    return patient_data["Age"]

def get_height(patient_data):
    return patient_data["Height (cm)"]

def get_weight(patient_data):
    return patient_data["Weight (kg)"]

def func_num(prompt):
    num = pyip.inputNum(prompt, 
                        blockRegexes=[r"[\s]"], 
                        min=1)
    return num

def func_name(prompt):
    name = pyip.inputStr(prompt,
                         blockRegexes=[r"[\d]"],
                         blank= False)
    if len(name) >= 2:
        name = name.title()
        return name
    else:
        print("This response is invalid, please insert minimal 2 letters")
        return func_name(prompt)

def func_gender(prompt):
    gender = pyip.inputStr(prompt,
                                  blockRegexes=[r"[\d]", r"[^mfMF]"],
                                  blank= False)
    gender = gender.capitalize()
    return gender

def func_code(name):
    code_name = name.split()
    if len(code_name) == 1:
        first_initial = code_name[0][0].upper()
        code_name = f"{first_initial}"
    else:
        first_initial = code_name[0][0].upper()
        last_initial = code_name[-1][0].upper()
        code_name = f"{first_initial}{last_initial}"
    code_num = len(patient_data) + 1
    code_patient = f"{code_name}{code_num}"
    return code_patient

def select_patient_code(prompt):
    while True:
        code_patient = pyip.inputStr(prompt,
                                    blockRegexes=[r"[\s]"],
                                    blank= False).upper()
        for index, patient in enumerate (patient_data):
            if patient["Code"] == code_patient:
                print(f"\nData For Patient {patient_data[index]["Name"]}:")
                print(tabulate([patient], headers="keys",tablefmt="heavy_outline"))
                return index, patient
            
        print(f"Patient Code {code_patient} Is Not Found, Please Insert The Existing Code")
   
def func_yesno(prompt):
    option = pyip.inputYesNo(prompt,
                              blockRegexes=[r"[\d]"],
                              blank= False )
    return option

def list_patient_data(patient_data):
    print("\nList Of Patient Data: ")
    print(tabulate(patient_data, headers="keys",tablefmt="heavy_outline"))

def register_new_patient():
    while True:
        name = func_name("\nInsert The Patient Name: ")
        gender = func_gender("Insert The Patient Gender (M/F): ")
        age = func_num("Insert The Patient Age: ")
        height = func_num("Insert The Patient Height (cm): ")
        weight = func_num("Insert The Patient Weight (kg): ")
        code_patient_baru = func_code(name)

        new_patient_data = {
            "Code": code_patient_baru,
            "Name": name,
            "Gender (M/F)": gender,
            "Age": age,
            "Height (cm)": height,
            "Weight (kg)": weight
        }

        patient_data.append(new_patient_data)
        print(f"\nPatient {name} Has Been Successfully Registered")
        list_patient_data(patient_data)
        confirm_add= func_yesno("\nDo You Wish To Register Another Patient? (Y/N): ")
        if confirm_add == "no":
            break

def sort_patient_data():
    while True:
        print("""
            Display The Sorted Patient Based On These Options:
            1. Name
            2. Gender
            3. Age
            4. Height
            5. Weight
            (Note: These Wont Change The Original Order Of The Patient List)
            """)
        option = func_num("Please Select The Number Of One Of The Options Above (1-5): ")
        if option == 1:
            confim_order = func_yesno("\nDo You Wish The Display Output In Ascending Order? (Y/N): ")
            if confim_order == "yes":
                sorted_name = sorted(patient_data, key = get_name)
                print(tabulate(sorted_name, headers="keys",tablefmt="heavy_outline"))
            else:
                sorted_name = sorted(patient_data, key = get_name, reverse=True)
                print(tabulate(sorted_name, headers="keys",tablefmt="heavy_outline"))
        elif option == 2:
            confim_order = func_yesno("\nDo You Wish The Display Output In The Order Of Female First? (Y/N): ")
            if confim_order == "yes":
                sorted_gender = sorted(patient_data, key = get_gender)
                print(tabulate(sorted_gender, headers="keys",tablefmt="heavy_outline"))
            else:
                sorted_gender = sorted(patient_data, key = get_gender, reverse=True)
                print(tabulate(sorted_gender, headers="keys",tablefmt="heavy_outline"))
        elif option == 3:
            confim_order = func_yesno("\nDo You Wish The Display Output From The Youngest? (Y/N): ")
            if confim_order == "yes":
                sorted_age = sorted(patient_data, key = get_age)
                print(tabulate(sorted_age, headers="keys",tablefmt="heavy_outline"))
            else:
                sorted_age = sorted(patient_data, key = get_age, reverse=True)
                print(tabulate(sorted_age, headers="keys",tablefmt="heavy_outline"))
        elif option == 4:
            confim_order = func_yesno("\nDo You Wish The Display Output From The Shortest? (Y/N): ")
            if confim_order == "yes":
                sorted_height = sorted(patient_data, key = get_height)
                print(tabulate(sorted_height, headers="keys",tablefmt="heavy_outline"))
            else:
                sorted_height = sorted(patient_data, key = get_height, reverse=True)
                print(tabulate(sorted_height, headers="keys",tablefmt="heavy_outline"))
        elif option == 5:
            confim_order = func_yesno("\nDo You Wish The Display Output From The Lightest? (Y/N): ")
            if confim_order == "yes":
                sorted_weight = sorted(patient_data, key = get_weight)
                print(tabulate(sorted_weight, headers="keys",tablefmt="heavy_outline"))
            else:
                sorted_weight = sorted(patient_data, key = get_weight, reverse=True)
                print(tabulate(sorted_weight, headers="keys",tablefmt="heavy_outline"))
        else:
            print("\nInvalid Option, Please Select The Available Option")
            continue

        confirm_display = func_yesno("\nDo You Wish To Display The Patient List Based On Another Option? (Y/N): ")
        if confirm_display == "no":
            break
    
def modify_patient_data():
    list_patient_data(patient_data)

    index, patient = select_patient_code("Insert Patient Code You Wish To Modify: ")
    
    while True:
        print("""
              Select The Following Data That You Want To Modify:
              1. Age
              2. Height (cm)
              3. Weight (kg) 
              """)
        option = func_num("Input Option (1-3): ")

        if option == 1:
            patient_data[index]["Age"] = func_num("Insert The Patient New Age: ")
        elif option == 2:
            patient_data[index]["Height (cm)"] = func_num("Insert The Patient New Height (cm): ")
        elif option == 3:
            patient_data [index]["Weight (kg)"] = func_num("Insert The Patient New Weight (kg): ")
        else:
            print("Invalid Input, Please Input The Available Option")
            continue

        print(f"Patient Data For {patient_data[index]["Name"]} Has Been Successfully Modified:")
        print(tabulate([patient], headers="keys",tablefmt="heavy_outline"))

        modify_confirm = func_yesno("Do You Wish To Modify Another Data? (Y/N): ")
        if modify_confirm == "no":
            break

def delete_patient_data():
    while True:
        list_patient_data(patient_data)

        index, patient = select_patient_code("\nInsert Patient Code You Wish To Delete: ")

        confirm_delete = func_yesno(f"\nDo You Wish To Delete The Data For Patient {patient_data[index]["Name"]}? (Y/N): ")
        if confirm_delete == "yes":
            patient_data.pop(index)
            print(f"\nPatient Data Successfully Deleted")
            if len(patient_data) == 0:
                print("\nList of Patient Data Is Empty")
                break
        else:
            print(f"\nData Removal For Patient {patient_data[index]["Name"]} Is Canceled")
            confirm_del_wish= func_yesno("\nDo You Still Wish To Delete Patient Data ? (Y/N): ")
            if confirm_del_wish == "yes":
                continue
            else:
                break
        
        list_patient_data(patient_data)
        confirm_del_other = func_yesno("\nDo You Still Wish To Delete Patient Data Again? (Y/N): ")
        if confirm_del_other == "no":
            break

def patient_bmi():
    while True:
        list_patient_data(patient_data)

        index, patient = select_patient_code("Please Select The Patient Code You Wish To Calculate The BMI: ")

        height_m = patient_data[index]["Height (cm)"]/100
        weight_kg = patient_data[index]["Weight (kg)"]
        bmi = round(weight_kg/(math.pow(height_m,2)),1)
        
        if bmi < 18.5:
            print (f"""
                   Patient BMI: {bmi} 
                   Patient {patient_data[index]["Name"]} Is Under The Category Of Underweight 
                   Health Condition:
                   Increased Risk: 
                   1. Malnutrition
                   2. Osteoporosis
                   3. Immune System Deficiencies
                   Please Consult With A Nutritionist
                   """)
        elif bmi >= 18.5 and bmi <= 24.9:
            print (f"""
                   Patient BMI: {bmi}
                   Patient {patient_data[index]["Name"]} Is Under The Category Of Normal Weight 
                   Health Condition:
                   Lower Risk Of Health Problems
                   Please Maintain The Diet And Exercise
                   """)
        elif bmi >= 25.0 and bmi <= 29.9:
            print (f"""
                   Patient BMI: {bmi} 
                   Patient {patient_data[index]["Name"]} Is Under The Category Of Pre-Obesity 
                   Health Condition:
                   Increased Risk:
                   1. Cardiovascular Diseases
                   2. High Blood Pressure
                   3. Type 2 Diabetes
                   Please Consult With A Nutritionist
                   """)
        elif bmi >= 30.0 and bmi <= 34.9:
            print (f"""
                   Patient BMI: {bmi} 
                   Patient {patient_data[index]["Name"]} Is Under The Category Of Obesity Class I
                   Health Condition:
                   High Risk:
                   1. Heart Disease
                   2. Type 2 Diabetes
                   3. Cancer
                   Please Consult With A Nutritionist
                   """)
        elif bmi >= 35.0 and bmi <= 39.9:
            print (f"""
                   Patient BMI: {bmi} 
                   Patient {patient_data[index]["Name"]} Is Under The Category Of Obesity Class II
                   Health Condition:
                   High Risk:
                   1. Heart Disease
                   2. Type 2 Diabetes
                   3. Cancer
                   Please Consult With A Nutritionist
                   """)
        elif bmi >= 40:
            print (f"""
                   Patient BMI: {bmi} 
                   Patient {patient_data[index]["Name"]} Is Under The Category Of Obesity Class III
                   Health Condition:
                   High Risk:
                   1. Heart Disease
                   2. Type 2 Diabetes
                   3. Cancer
                   Please Consult With A Nutritionist
                   """)
        else:
            print("BMI Is Invalid, Please Re-Check The Data For Any Errors")
        
        confirm_count = func_yesno("Do You Wish To Assess Another Patient? (Y/N): ")
        if confirm_count == "no":
            break

def main_menu():
    while True:
        print("""
              Welcome Admin! Welcome To The RC Hospital Nutrition Division
              Main Menu:
              1. Display Patient Data List
              2. Register New Patient
              3. Display The Sorted Patient Data List
              4. Modify Patient Data
              5. Delete Patient Data
              6. Assess Patient Health Based On BMI 
              7. Logout
              """)
        menu = func_num ("Please Select One Of The Menu Option (1 - 7): ")
        if menu == 1:
            list_patient_data(patient_data)
        elif menu == 2:
            register_new_patient()
        elif menu == 3:
            sort_patient_data()
        elif menu == 4:
            modify_patient_data()
        elif menu == 5:
            delete_patient_data()
        elif menu == 6:
            patient_bmi()
        elif menu == 7:
            print("Logging Out")
            break
        else:
            print("Invalid Input, Please Select The Available Option")

def login():
    while True:
        login_username = input("\nUsername: ")
        login_password = input("Password: ")

        if login_username == "admin" and login_password == "admin":
            main_menu()
        else:
            print("Username or Password Is Incorrect, Access Denied")

login()