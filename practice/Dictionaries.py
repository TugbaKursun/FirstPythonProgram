monthConversions ={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Jul"])
print(monthConversions.get("Dec"))

monthConversions2 = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

print(monthConversions2.get(11))

currency = {
    "$" : "Dollar",
    "tl": "Turkish Lira",
    "e" : "Euro",
    "inr": "Indian Rupee",
    "cad": "Canadian dollar"
}

print(currency.get("tl"))
print(currency["$"])