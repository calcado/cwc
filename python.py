def searchIndex(headers,name):
    variable = 0
    for element in (headers):
        if element == name:
            return variable
        variable = variable + 1

def maxCBK(valueById,type):
    highestCBK = 0
    highestId = 0
    for id, incidents in valueById.items():
        if highestCBK < incidents[type]:
            highestCBK = incidents[type]
            highestId = id

    return highestId, highestCBK    
    

with open("transactional-sample.csv") as file:
    headers = file.readline().strip().split(",")
    ## analyzing headers to understand possible patterns
    ## print(headers)
    cbkIndex = searchIndex(headers, "has_cbk")
    merchantIndex = searchIndex(headers, "merchant_id")
    transactionIndex = searchIndex(headers, "transaction_amount")
    userIndex = searchIndex(headers, "user_id")
    totals = {"count":0, "amount":0}
    moneySpent = 0
    statsByMerchant = {}
    statsByUser = {}
    totalAmount = 0
    for rawRow in file.readlines():
        row = rawRow.strip().split(",")
        merchantId = row[merchantIndex]
        userId = row[userIndex]
        transactionAmount = float(row[transactionIndex])
        statsByMerchant.setdefault(merchantId, {"count":0, "amount":0})
        statsByUser.setdefault(userId, {"count":0 , "amount":0})
        if row[cbkIndex] == "TRUE":
            ## every row that a fraud has been commited
            ## print(row)
            totals["amount"] = totals["amount"] + transactionAmount
            totals["count"] = totals["count"] + 1
              
            statsByMerchant[merchantId]["count"] = statsByMerchant[merchantId]["count"] + 1
            statsByMerchant[merchantId]["amount"] = statsByMerchant[merchantId]["amount"] + transactionAmount
            
            statsByUser[userId]["count"] = statsByUser[userId]["count"] + 1
            statsByUser[userId]["amount"] = statsByUser[userId]["amount"] + transactionAmount
            
        
    
    ## total os incidents and money lost
    print(totals["count"], totals["amount"])
    ## merchant with more incidents    
    print(maxCBK(statsByMerchant, "count"))
    ## merchant that lost more money
    print(maxCBK(statsByMerchant, "amount"))
    ## user with more incidents
    print(maxCBK(statsByUser,"count"))
    ## user that caused more lost
    print(maxCBK(statsByUser,"amount"))


    
