class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start <= destination:
            first_distance = sum(distance[start:destination])
        else:
            first_distance = sum(distance[destination:start])
        return min(first_distance, sum(distance)-first_distance)

