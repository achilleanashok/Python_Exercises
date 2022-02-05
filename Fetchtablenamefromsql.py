

def fetch_tablenm_fromsql(sqlquery):
    lst = sqlquery.split(" ")

    for i in range(len(lst)):
        if lst[i] == "from":
            return lst[i+1]


sqlquery = "select * from tablename"

print(fetch_tablenm_fromsql(sqlquery))