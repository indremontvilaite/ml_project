def are_columns_identical(df, col1, col2):
    return (df[col1] == df[col2]).all()

def find_identical_columns(df):
    columns = df.columns
    identical_columns = []
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            if are_columns_identical(df, columns[i], columns[j]):
                identical_columns.append((columns[i], columns[j]))
    return identical_columns