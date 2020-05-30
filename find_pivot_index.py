class Sol:
    def find_pivot_index(self,nums):
        for i in range(1,len(nums)-1):
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
        return -1

if __name__ == '__main__':
    p=Sol()
    print(p.find_pivot_index([1, 7, 3, 6, 5, 6]))
