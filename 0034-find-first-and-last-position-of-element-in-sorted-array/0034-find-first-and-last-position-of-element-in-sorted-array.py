class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first():
            low=0
            high=len(nums)-1
            ans=-1
            while low <=high:
                mid=(low+high)//2
                if target ==nums[mid]:
                    ans=mid
                    high=mid-1
                elif target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            return ans
        def sec():
            low=0
            high=len(nums)-1
            ans=-1
            while low <=high:
                mid=(low+high)//2
                if target ==nums[mid]:
                    ans=mid
                    low=mid+1
                elif target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            return ans
        return [first(),sec()]




        