class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed))
        st=[]

        for p,s in cars[::-1]:
            time_taken=(target-p)/s
            if not st or time_taken>st[-1]:
                st.append(time_taken)
        return len(st)
        
            