
# Nesting a list in a dictionary
capitals = {
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"],

}


# Nesting a dictionary in a dictionary 

travel log = {
    "France":{ "Cities Visited" : ["Paris","Lille","Dijon"] , "total_visits" : 12  },
    "Germany":{ "Cities Visited" : ["Berlin","Hamburg","Stuttgart"], "train ride from berline" : [0,12,4] },

}

# Nesting Dictionary in a List
travel log = [
    { 
        "country" : "France" , 
        "Cities Visited" : ["Paris","Lille","Dijon"] ,
        "total_visits" : 12
     },
    {
        "country" : "Germany" ,
        "Cities Visited" : ["Berlin","Hamburg","Stuttgart"] , 
        "total_visits" : 5  
    },

]
