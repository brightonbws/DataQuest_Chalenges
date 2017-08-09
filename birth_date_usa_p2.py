
# coding: utf-8

# In[9]:


f = open("US_births_1994-2003_CDC_NCHS.csv", 'r')
reader = f.read()
date_splt = reader.split('\n')


print(date_splt[0:10])


# In[2]:


def read_csv(file):
    f = open(file)
    reader = f.read()
    string_list = reader.split('\n')
    string_list = string_list[1:]
    
    final_list = []
    
    for i in string_list:
        int_fields = []
        string_fields = i.split(',')
        for i in string_fields:
            int_fields.append(int(i))
        final_list.append(int_fields)
        
    return final_list
        

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
print(cdc_list[:10])


# In[4]:


def month_births(new_list):
    births_per_month = {}
    
    for i in new_list:
        m_date = i[1]
        birth_count = i[4]
        
        if m_date in births_per_month:
            births_per_month[m_date] += birth_count
        else:
            births_per_month[m_date] = birth_count
    return births_per_month
            
print(month_births(cdc_list))


# In[5]:


def dow_births(new_list):
    births_per_dow = {}
    
    for i in new_list:
        dow_date = i[3]
        birth_count = i[4]
        
        if dow_date in births_per_dow:
            births_per_dow[dow_date] += birth_count
        else:
            births_per_dow[dow_date] = birth_count
    return births_per_dow

print(dow_births(cdc_list))


# In[10]:


def calc_counts(data, column):
    column_counts = {}
    
    for i in data:
        col = i[column]
        col_count = i[4]
        if col in column_counts:
            column_counts[col] += col_count
        else:
            column_counts[col] = col_count
    return column_counts

cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)

print(cdc_year_births)
print(cdc_month_births)
print(cdc_dom_births)
print(cdc_dow_births)
        


# In[ ]:




