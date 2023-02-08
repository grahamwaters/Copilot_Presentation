# example three
def capitalize_list_of_strings(list_of_strings):
    return [i.capitalize() for i in list_of_strings]
# example four
def get_aapl_price():
    #* get the data for AAPL
    aapl = yf.Ticker('AAPL')
    #* get the last price
    last_price = aapl.history(period='1d')['Close'][0]
    return last_price
# example two
def get_csv_column_types(csv_file):
    #* read in the csv file as a dataframe
    df = pd.read_csv(csv_file)
    #* get the column names
    column_names = list(df.columns)
    #* convert the dataframe to a list of lists
    df = df.values.tolist()
    #* initialize a list to hold the types of the first row
    column_types = []
    #* loop over the first row to get the types
    for i in df[0]:
        column_types.append(type(i))
    return df, column_names, column_types