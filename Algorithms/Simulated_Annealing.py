import random, copy

import math


class SimulatedAnnealing:
    numberOfProduced = 0
    numberOfExpanded = 0
    def __init__(self, logger):
        self.logger = logger
        self.debugMode = True

    def solve(self, problem_instance, type_of_cooling):
        t = 1000
        # if type_of_cooling == 3:
        #     t = 100
        opSolution = self.mainLoop(t, 100, problem_instance, type_of_cooling)

    def mainLoop(self, tempreture, iterationPerTempreture, problem_instance, type_of_cooling):

        bestSolutionEver = None
        bestFitnessEver = -100
        initialTempreture = tempreture
        solution = problem_instance.initial_state()
        fitness = -100
        k = 1

        while tempreture > 0.5 and k < 200:
            # print(fitness)
            if self.debugMode: self.logger.debug("\n\n\n")
            if self.debugMode: self.logger.debug(
                "---------------------  Tempreture: " + str(tempreture) + "  ---------------------")

            for i in range(iterationPerTempreture):
                if self.debugMode: self.logger.debug(
                    "best of all: " + str(bestSolutionEver) + " " + str(bestFitnessEver) + " solution: " + str(
                        solution) + " " + str(fitness))
                self.numberOfProduced += 1
                newSolution = problem_instance.get_random_neighbor(solution[0])
                # print(solution[1])
                # while
                accept = False
                # move to new state or not
                newFitness = problem_instance.fitness(newSolution[0])
                if self.debugMode: self.logger.debug("new sol: " + str(newFitness) + " recent: " + str(fitness))
                if newFitness > fitness:
                    self.numberOfExpanded += 1
                    if self.debugMode: self.logger.debug("new solution is better")
                    accept = True
                    if newFitness > bestFitnessEver:
                        bestFitnessEver = newFitness
                        bestSolutionEver = newSolution
                        if self.debugMode: self.logger.debug("best sol fitness: " + str(newFitness))
                else:
                    if self.debugMode: self.logger.debug("new solution is worse")
                    deviationEnergy = self.computeDeviationEnergy(tempreture, initialTempreture)
                    if fitness - newFitness < deviationEnergy:
                        self.numberOfExpanded += 1
                        if self.debugMode: self.logger.debug("but it was accepted. deviationEnergy: " + str(
                            deviationEnergy) + " fitness - newFitness: " + str(fitness - newFitness))
                        accept = True

                if accept:
                    solution[0] = newSolution[0]
                    solution[1] = solution[1] + "_" + newSolution[1]
                    fitness = newFitness
                    if self.debugMode: self.logger.debug("last accepted solution: " + str(solution))
                    accept = False

            if type_of_cooling == 1:
                # linear
                tempreture -= 50
            elif type_of_cooling == 2:
                # exponential
                tempreture *= 0.8
            elif type_of_cooling == 3:
                # logarithmic
                tempreture = initialTempreture/(1 + 30*math.log10(1+k))
                k += 1

        if self.debugMode: self.logger.debug("best of all: " + str(bestSolutionEver) + " solution: " + str(solution))

        print("solution: ", bestSolutionEver[0], " fitness:", bestFitnessEver)
        print("number of expanded: " + str(self.numberOfExpanded))
        print("number of produced: " + str(self.numberOfProduced))
        # print("moves: ", bestSolutionEver[1])
        return bestSolutionEver

    def computeDeviationEnergy  (self, currentTempreture, initialTempreture):
        return (1/2) * 6 * 9 * (currentTempreture / initialTempreture)
