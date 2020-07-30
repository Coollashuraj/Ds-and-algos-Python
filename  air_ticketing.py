#!/usr/bin/python
# -*- coding: utf-8 -*-


class Flight:

    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
      return self.capacity - len(self.passengers)
""

flight = Flight(3)

people = ['Bob', 'Micky', 'Larry', 'pat']
for person in people:
    success = flight.add_passenger(person)
    if success:
        print ("Added" + " " + person + "to the flight successfully. ")
    else:
        print ("No available seats for" + " " +person)
