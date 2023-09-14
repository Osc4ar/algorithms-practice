class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        destination_dictionary = self.build_destination_dictionary(tickets)

        itinerary = ["JFK"]

        while len(destination_dictionary) > 0:
            latest_stop = itinerary[-1]

            possible_next_destinations = destination_dictionary[latest_stop]
            next_destination = None
            if len(possible_next_destinations) > 1:
                next_destination_index = self.get_next_destination_index(possible_next_destinations, destination_dictionary)
                next_destination = possible_next_destinations.pop(next_destination_index)
            else:
                next_destination = possible_next_destinations.pop()

            if len(possible_next_destinations) == 0:
                destination_dictionary.pop(latest_stop)

            itinerary.append(next_destination)

        return itinerary


    def build_destination_dictionary(self, tickets: List[List[str]]):
        destination_dictionary = {}

        for ticket in tickets:
            origin = ticket[0]
            destination = ticket[1]

            if origin in destination_dictionary:
                destination_dictionary[origin] = self.add_destination(origin, destination, destination_dictionary)
            else:
                destination_dictionary[origin] = [destination]

        return destination_dictionary

    def add_destination(self, origin: str, destination: str, destination_dictionary) -> List[str]:
        possible_destinations = destination_dictionary[origin]
        possible_destinations.append(destination)
        return sorted(possible_destinations)
        
    def get_next_destination_index(self, possible_next_destinations: List[str], destination_dictionary) -> int:
        for i, destination in enumerate(possible_next_destinations):
            if destination in destination_dictionary:
                return i