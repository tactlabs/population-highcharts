import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    
    region = df['region'].tolist()
    population = df['population'].tolist()

    
      
    list_of_tuples = [tuple(row) for row in df.values]
  
    print(list_of_tuples)

    # print(df['quebec'].tolist())

    result_dict = {
        'region': region,
        'population': population,
        'data_list': list_of_tuples,
    }

    # print(result_dict)

    return result_dict

def add_row(region,population):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        'region'       : region, 
        'population'    : population, 
        
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()