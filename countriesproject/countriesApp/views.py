from django.shortcuts import render
import requests
def countryDetails(request):
    name=request.POST.get("country")
    url=f"https://restcountries.com/v3.1/name/{name}"
    response=requests.get(url)
    resp=response.json()
    # print(resp)
   


    payload={
        "countryName":resp[1]["name"]["official"],
        "population":int(resp[0]['population']),
        "flag":resp[0]['flags']['svg'],
        "Continent":resp[0]["continents"],
        "Capital":resp[1]['capital'],
        "Languages":resp[1]["languages"]
        
        
    }
    context={
        "resp":payload
    }
    return render(request,"index.html",context)