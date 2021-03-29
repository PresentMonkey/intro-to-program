#Patrick Gawel


def ask():
    pop = int(input('Starting population: '))
    growth = float(input('Projected growth rate (.01 = 1%): '))
    if(growth >= 1.0):
        growth = growth / 100
    years = int(input("Number of years to project: "))
    return {
        "pop": pop,
        "growth": growth,
        "years": years
    }

def calculuate(pop, growth, years):
    for year in range(years):
    #Apply the increase in pop AFTER the first year is completled
        if(year > 0):
            pop += (pop * growth)
        print((year+1), '\t\t\t', pop)



userinput = ask()
print("Year Approximate\t\t Population")
print("-----------------------------------------")

calculuate(userinput["pop"], userinput["growth"], userinput["years"])
