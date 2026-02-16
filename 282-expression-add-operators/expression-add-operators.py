class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result=[]

        def bt(start,curr_val,last_operand,expression,result):
            if start==len(num):
                if curr_val==target:
                    result.append(expression)
                return
            for i in range(start,len(num)):
                if i>start and num[start]=="0":
                    return
                curr_num=num[start:i+1]
                curr_num_int=int(curr_num)
                if start==0:
                    bt(i+1,curr_num_int,curr_num_int,curr_num,result)
                else:
                    bt(i+1,curr_num_int+curr_val,curr_num_int,expression +"+"+curr_num,result)
                    bt(i+1,curr_val-curr_num_int,-curr_num_int,expression +"-"+curr_num,result)
                    bt(i+1,curr_val-last_operand+last_operand*curr_num_int,last_operand*curr_num_int,expression +"*"+curr_num,result)
        bt(0,0,0,"",result)
        return result