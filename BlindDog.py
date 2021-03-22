import agents

class Born(agents.Thing):
    pass
class Water(agents.Thing):
    pass
class Food(agents.Thing):
    pass
class WorkingOnPZ(agents.Thing):
    pass
class СompletionPZ(agents.Thing):
    pass
class Die(agents.Thing):
    pass

class BlindDog(agents.Agent):
    location = [0, 0] #location = 1
    #_food, _water = None, None
    def movedown(self): self.location[1] += 1 #self.location += 1

class Park2D(agents.GraphicEnvironment):
    def percept(self, agent): return self.list_things_at(agent.location)

    def execute_action(self, agent, action):
        if action == "йдемо далі":
            print('переходимо в локацію: {}'.format(agent.location))
            agent.movedown()
        else:
            Action = {
                "кушаємо":lambda :self.action(action, "кушаємо", 'кушаємо в локації: {}', agent, Food),
                "п'ємо водичку": lambda :self.action(action, "п'ємо водичку", """п'ємо водичку в локації: {}""", agent, Water),
                "народився":lambda :self.action(action, "народився", 'народився в локації: {}', agent, Born),
                "робимо пз": lambda: self.action(action, "робимо пз", 'робимо пз в локації: {}', agent, WorkingOnPZ),
                "зробили пз": lambda: self.action(action, "зробили пз", 'зробили пз в локації: {}', agent, СompletionPZ),
                "тепер можна і вмерти": lambda: self.action(action, "тепер можна і вмерти", 'Вмираємо в локації: {}', agent, Die)
                      }
            Action[action]()

    def action(self, action, actiontext, text, agent, tclass):
        if action == actiontext:
            items = self.list_things_at(agent.location, tclass=tclass)
            if len(items) != 0:
                if (lambda thing, tclass: True if isinstance(thing, tclass) else False)(items[0], tclass):
                    print(text.format(agent.location))
                    self.delete_thing(items[0])
                    agent.movedown()

    def is_done(self):
        no_edibles = not any(isinstance(thing, Food) or isinstance(thing, Water) or isinstance(thing, Born) or isinstance(thing, WorkingOnPZ)
                             or isinstance(thing, СompletionPZ) or isinstance(thing, Die) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return dead_agents or no_edibles

def program(percepts):
    for p in percepts:
        if isinstance(p, Food): return 'кушаємо'
        elif isinstance(p, Water): return "п'ємо водичку"
        elif isinstance(p, Born): return 'народився'
        elif isinstance(p, WorkingOnPZ): return 'робимо пз'
        elif isinstance(p, СompletionPZ): return 'зробили пз'
        elif isinstance(p, Die): return 'тепер можна і вмерти'
    return 'йдемо далі'

def main():
    park = Park2D(7, 20, color={'BlindDog': (200, 0, 0), 'Water': (0, 200, 200), 'Food': (230, 115, 40), 'Born': (231, 15, 0),
                                 'WorkingOnPZ': (230, 2, 4), 'СompletionPZ': (232, 1, 3), 'Die': (25, 25, 25)})
    dog = BlindDog(program)
    born = Born()
    dogfood = Food()
    water = Water()
    working = WorkingOnPZ()
    pz = СompletionPZ()
    die = Die()
    park.add_thing(born, [0, 2])
    park.add_thing(dog, [0, 0])
    park.add_thing(dogfood, [0, 3])
    park.add_thing(water, [0, 4])
    park.add_thing(working, [0, 5])
    park.add_thing(pz, [0, 6])
    park.add_thing(die, [0, 7])
    park.run(11)

main()