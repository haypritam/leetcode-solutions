class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        total_moves = 0
        n = len(seats)
        for i in range(n):
            total_moves += abs(students[i] - seats[i])
        
        return total_moves