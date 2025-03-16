import pandas as pd

# initalise data of lists

data = {'Name': ['Tom', 'nick','krish', 'jack'],
        'Age': [20, 21, 19, 18]}

print(data)
# output: {'Name': ['Tom', 'nick', 'jack'], 'Age': [20, 21, 19, 18]}

# Create DataFrame

df = pd.DataFrame(data)
print(df)

#experienced error because each row (in this case, Name and Age) in a DataFrame must have the same number of elements


"""
output of the DataFrame:

    Name  Age
0    Tom   20
1   nick   21
2  krish   19
3   jack   18



"""