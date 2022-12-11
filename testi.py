import var_dump as vd
result = {
    "success": True,
    "query": {
        "from": "EUR",
        "to": "USD",
        "amount": 100
    },
    "info": {
        "timestamp": 1669971543,
        "quote": 1.053685
    },
    "result": 105.3685
}

print(result["result"])

vd.var_dump(result)