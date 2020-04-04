   """ r = request.get('https://graph.facebook.com/v4.0/me?fields=id%2Cname%2Cfeed&access_token=EAAFwJhMIpkUBAB7RVKxV9UzCliSIGN8pBcxcfiTzByHu7o0yui9lJWmrNfnvdoKd0v5hQ6v8ZB2QTiZCr7yOETobw9f6rd5icrhuzOue2PStqyfk0V7ZCcUYHMaisdPslWs3lZB5ZAI68DdVt4fvG9k5y4keN0PY0F5X4YwYS6gZDZD')
    json = r.json()
    
    h = request.get('https://graph.facebook.com/v5.0/230231543752378?fields=feed.limit(9)%7Bmessage%2Cpermalink_url%2Cfull_picture%7D&access_token=EAAFwJhMIpkUBAB7RVKxV9UzCliSIGN8pBcxcfiTzByHu7o0yui9lJWmrNfnvdoKd0v5hQ6v8ZB2QTiZCr7yOETobw9f6rd5icrhuzOue2PStqyfk0V7ZCcUYHMaisdPslWs3lZB5ZAI68DdVt4fvG9k5y4keN0PY0F5X4YwYS6gZDZD')"""
    json2 = h.json()
    fb=Feedback.objects.all()

    "fb":fb

    "json":json, "json2":json2,