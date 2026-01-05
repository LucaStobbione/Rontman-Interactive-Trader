# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 23:47:44 2025

@author: Luca
"""

import requests, json, time

API_KEY={"X-API-Key":"OX85NG5K"}

api=requests.Session()
api.headers.update(API_KEY)



def bidask(ticker):
    
    par={"ticker":ticker,
            "limit":50}
    
    data=api.get("http://localhost:9999/v1/securities/book", params=par).json()
    
    bid=[(x["price"],x["quantity"])for x in data["bids"]]
    ask=[(x["price"],x["quantity"])for x in data["asks"]]
    
    

    return (bid, ask)



def tick():
    
    case=api.get("http://localhost:9999/v1/case").json()
    tick=case["tick"]
    
    return tick




def strategy():
    ###
    tenders=api.get("http://localhost:9999/v1/tenders").json()
    if not tenders:
        return
    
    
    tend=[(t["ticker"],t["action"],t["price"],t["quantity"],t["tender_id"])for t in tenders]

    print(tend[0])

    ticker=tend[0][0]
    price=tend[0][2]
    volume=tend[0][3]
    action=tend[0][1]
    tenderid=tend[0][4]
    bid,ask=bidask(ticker)


    if action=="BUY":
        if price<bid[0][0]:
            amountre=0
            amount=0
            for i in range(len(bid)):
                if bid[i][0]>price:
                    amountre=amountre+bid[i][1]
            
            amount=amountre-4000
            if amount>volume:
                resp=api.post(f"http://localhost:9999/v1/tenders/{tenderid}")
                print("tender acceptaded",amount," ",volume)
            else:
                print("tender declined", amount," ",volume)
            
        else:
            print("buy at higher price ", price," than in the mkt ",bid[0][0])
            
    elif action=="SELL":
        if price>ask[0][0]:
            amountre=0
            amount=0
            for i in range(len(ask)):
                if ask[i][0]<price:
                    amountre=amountre+ask[i][1]
            
            amount=amountre-4000
            if amount>volume:
                resp=api.post(f"http://localhost:9999/v1/tenders/{tenderid}")
                print("tender acceptaded",amount," ",volume)
            else:
                print("tender declined", amount," ",volume)
            
        else:
            print("sell at lower price ", price," than in the mkt ",ask[0][0])
            
            
    ###
tick=tick()
while tick>5 and tick<295:
    strategy()
    time.sleep(1)     
        
        