import pandas as pd
import pdfplumber
pdf = pdfplumber.open(r'test.pdf')
df = pd.DataFrame()
table_settings={"vertical_strategy": "text", 
    "horizontal_strategy": "lines","intersection_y_tolerance": 8}
df = pd.DataFrame(pdf.pages[3].extract_table(table_settings))
df.to_csv(r'test.csv')

df = pd.read_csv('test.csv')
df.fillna(0, inplace = True)

deposit = list(df['2'])
deposit_list = []
for i in range(1, len(deposit)):
    if isinstance(deposit[i], int):
        deposit_list.append(deposit[i])
    else:
        new = deposit[i].replace('$', "", 1)
        sub = "."
        new2 = new[:new.index(sub) + len(sub)]
        new2 = new2.replace('.', '', 1)
        new2 = new2.replace(',', '', 1)
        deposit_list.append(int(new2))

sum_deposit = sum(deposit_list)
avg_deposit = sum_deposit/len(deposit_list)

Withdrawals = list(df['3'])
Withdrawals_list = []
for i in range(1, len(Withdrawals)):
    if isinstance(Withdrawals[i], int):
        Withdrawals_list.append(Withdrawals[i])
    else:
        new = Withdrawals[i].replace('$', "", 1)
        sub = "."
        new2 = new[:new.index(sub) + len(sub)]
        new2 = new2.replace('.', '', 1)
        new2 = new2.replace(',', '', 1)
        Withdrawals_list.append(int(new2))

sum_withdrawals = sum(Withdrawals_list)
avg_Withdrawals = sum_withdrawals/len(Withdrawals_list)

print("average of deposit : ", avg_deposit)
print('average of withdrawals : ', avg_Withdrawals)
