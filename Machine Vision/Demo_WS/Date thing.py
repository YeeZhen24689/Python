year = 2005
month = 3
day = 23
 
days_feb = 28
months_in_year = 12
 
current_year = 2024
current_month = 3
current_day = 18
 
days_since = 0
months_since = 0
years_since = 0
 
 
#years
years_since = current_year - year
 
#months
if month < current_month:
    months_since += current_month - month
    
elif month > current_month:
    months_since += (months_in_year - month) + current_month
    years_since = years_since -1
    
elif month == current_month:
    months_since = 0
    
#day    
if day < current_day:
    days_since += current_day - day
       
elif day > current_day:
    days_since += (days_feb - day) + current_day
    if months_since == 0:
        pass
    else:
        months_since = months_since - 1
         
elif day == current_day:
    days_since = 0
    
        
print(str(days_since)+"/"+str(months_since)+"/"+str(years_since))