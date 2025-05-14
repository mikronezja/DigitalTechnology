import pandas as pd
import logicmin

df = pd.read_csv("excel.csv",sep=';', index_col=0)
t = logicmin.TT(8, 4)

first_variables = ["X3", "X2", "X1", "X0", "Q3", "Q2", "Q1", "Q0"]
second_variables = ["Q3'", "Q2'", "Q1'", "Q0'"]

# Iterujemy po wierszach i kolumnach
for row in df.index:
    for col in df.columns:
        input_bits = str(row).strip().zfill(4) + str(col).strip().zfill(4)
        output_bits = str(df.loc[row, col]).strip()

        if output_bits.lower() == 'x':
            output_bits = "----"
        else:
            output_bits = output_bits.zfill(4) # 4 bitowa liczba binarna
        t.add(input_bits, output_bits)

solution = t.solve()
print(solution.printN(xnames = first_variables,
ynames = second_variables))
# import pandas as pd
# import logicmin

# df = pd.read_csv("konwerter.csv",sep=';', index_col=0)
# t = logicmin.TT(4, 3)

# first_variables = ["Q3", "Q2", "Q1", "Q0"]
# second_variables = ["S2", "S1", "S0"]

# # Iterujemy po wierszach i kolumnach
# for row in df.index:
#     for col in df.columns:
#         input_bits = str(row).strip().zfill(2) + str(col).strip().zfill(2)
#         output_bits = str(df.loc[row, col]).strip()

#         if output_bits.lower() == 'x':
#             output_bits = "---"
#         else:
#             output_bits = output_bits.zfill(3) # 3 bitowa liczba binarna
#         t.add(input_bits, output_bits)

# solution = t.solve()
# print(solution.printN(xnames = first_variables,
# ynames = second_variables))
