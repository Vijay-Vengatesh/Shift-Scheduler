import calendar
import random
import time
def shift_cal(p_yr,p_mth,p_no):
    name_list = ["Vijay Vengatesh","Kavitha Jayakumar","Arasanathan Narasimman",
       "Abirami Muthukumaraswamy","Sasikala Ramalingam","Rajan Sam",
       "Grace Wong"]
    shift_times = ["Morning","Evening","Night"]
    num_days = calendar.monthrange(p_yr,p_mth)[1]
    print(num_days)
    if num_days == 30:
        print('month with 30 days',p_yr,p_mth)
        for a in range(1,31):
            num = p_no+1
            for aa in range(1,num):
                print('Day : ',a)
                if random.choice(shift_times) == "Morning" or random.choice(name_list) == "Grace Wong":
                    print("Grace Wong","Morning")
                elif random.choice(shift_times) == "Evening":
                    print(random.choice(name_list),"Evening")
                elif random.choice(shift_times) == "Night":
                    print(random.choice(name_list),"Night")
    elif num_days == 31:
        print('month with 31 days',p_yr,p_mth)
        for a in range(1,32):
            num = p_no+1
            for aa in range(1,num):
                print('Day : ',a)
                if random.choice(shift_times) == "Morning" or random.choice(name_list) == "Grace Wong":
                    print("Grace Wong","Morning")
                elif random.choice(shift_times) == "Evening":
                    print(random.choice(name_list),"Evening")
                elif random.choice(shift_times) == "Night":
                    print(random.choice(name_list),"Night")
    elif num_days == 28:
        print('month with 28 days',p_yr,p_mth)
        for a in range(1,29):
            num = p_no+1
            for aa in range(1,num):
                print('Day : ',a)
                if random.choice(shift_times) == "Morning" or random.choice(name_list) == "Grace Wong":
                    print("Grace Wong","Morning")
                elif random.choice(shift_times) == "Evening":
                    print(random.choice(name_list),"Evening")
                elif random.choice(shift_times) == "Night":
                    print(random.choice(name_list),"Night")
    elif num_days == 29:
        print('month with 29 days',p_yr,p_mth)
        for a in range(1,30):
            num = p_no+1
            for aa in range(1,num):
                print('Day : ',a)
                if random.choice(shift_times) == "Morning" or random.choice(name_list) == "Grace Wong":
                    print("Grace Wong","Morning")
                elif random.choice(shift_times) == "Evening":
                    print(random.choice(name_list),"Evening")
                elif random.choice(shift_times) == "Night":
                    print(random.choice(name_list),"Night")    
        
yr = int(input('Enter a year : '))
mth = int(input('Enter a month : '))
no = int(input('Enter no. of employees : '))
shift_cal(yr,mth,no)