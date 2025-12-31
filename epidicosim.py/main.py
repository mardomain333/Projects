import random
class Simulation:
    def __init__(self):
        
        self.day_number=1
        
        print("\n We must know the population of the City:?")
        self.city_population=int(input("Enter the population of city"))

        print("\n We must know how many percentage of population get infected initially:?")
        self.infected_count=float(input("Enter the percentage infection [0-100]"))
        self.infected_count/=100

        print("\n we must know the risk for a person when he exposed to the disease:?")
        self.infection_probabiliy=float(input("Enter the probabiliy that a person got disease"))

        print("\n we must know how long the infection will retain in human body:?")
        self.infection_duration=int(input("Enter the duration in days of disease when it affected"))

        print("\n We must know the mortality rate for the infected person:?")
        self.infected_mortality=float(input("Enter the mortality rate::"))

        print("\n we must know how many days this simulation to run")
        self.sim_day=int(input("Enter the no of days to simulate"))




class Person:
    def __init__(self):
        self.is_infected=False
        self.is_dead=False
        self.day_infected=0

    def infect(self,sim):
        #infection if random number less thatn probabiliy
        if random.randint(0,100)< sim.infection_probabiliy:
            self.is_infected=True
    def heal(self):
        self.day_infected=0
        self.is_infected=False
    def die(self):
        self.is_dead=True
    def update(self,sim):
        if not self.is_dead:
            if self.is_infected:
                self.day_infected+=1
                if random.randint(0,100)<sim.infected_mortality:
                    self.die()
                elif self.day_infected==sim.infection_duration:
                    self.heal()
            


class Population:

    def __init__(self,sim):
        
        self.population=[]
        for i in range(sim.city_population):
            person=Person()
            self.population.append(person)
    def inital_infection(self,sim):

        self.infect_count=int(round(sim.city_population*sim.infected_count,0))
        for i in range(self.infect_count):
            self.population[i].is_infected=True
            self.population[i].day_infected=1

        random.shuffle(self.population)

    def spread_infection(self,sim):

        for i in range(len(self.population)):
            if self.population[i].is_dead == False:
                if self.population[i].is_infected==False:
                    if i==0:
                        if self.population[i+1].is_infected:
                            self.population[i].infect(sim)
                           
                    elif i<len(self.population)-1:
                        if self.population[i-1].is_infected or self.population[i+1].is_infected:
                            self.population[i].infect(sim)
                           
                    elif i==len(self.population)-1:
                        if self.population[i-1].is_infected:
                            self.population[i].infect(sim)
                            
                    
    def update(self,sim):
        sim.day_number+=1
        for person in self.population:
            person.update(sim)   

    def show_statics(self,sim):

        total_infected_count=0
        total_dead_count=0
        for person in self.population:
            if person.is_infected:
                total_infected_count+=1
                if person.is_dead:
                    total_dead_count+=1
        infect_percent=round((total_infected_count/sim.city_population)*100,4)   
        dead_percent=round((total_dead_count/sim.city_population)*100,4)  

        print("---Day # :"+str(sim.day_number)+" %")
        print("---Infected % :"+str(infect_percent)+" %")
        print("---Dead % :"+str(dead_percent)+"%")
        print("---Infected count :"+str(total_infected_count)+" / "+str(sim.city_population))
        print("---Dead count :"+str(total_dead_count)+" / "+str(sim.city_population))
    
    def display(self):
        status=[]
        for person in self.population:
            if person.is_dead:
                chart='X'
            else:
                if person.is_infected:
                    chart='I'
                else:
                    chart="0"
            status.append(chart)
        for letter in status:
            print(letter,end='-')

sim=Simulation()
pop=Population(sim)


pop.inital_infection(sim)
pop.show_statics(sim)
pop.display()

input("Press enter to continues..")
for i in range(1,sim.sim_day+1):
    pop.spread_infection(sim)
    pop.update(sim)
    pop.show_statics(sim)
    pop.display()

    if i!=sim.sim_day:
        input("\nPress enter to advance to next day ...")