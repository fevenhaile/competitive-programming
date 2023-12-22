class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        count = 0
        if len(arr) < 3:
            return False
        while i < len(arr) - 1:
            if arr[i] == arr[i+1]:
                return False
            elif arr[i] > arr[i+1]:
                    break
            count += 1
            i += 1
        if count == 0:
            return False
        count = 0
        while i < len(arr) - 1:    
            if arr[i] <= arr[i+1]:
                return False
            count += 1
            i += 1
        if count == 0:
            return False

        print(i)
        return True


                        
        
        

                                                                            

            
        
        