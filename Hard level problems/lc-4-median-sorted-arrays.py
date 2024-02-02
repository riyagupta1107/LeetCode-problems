class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m=len(nums1)
        n=len(nums2)
        i,j,k=0,0,0
        arr=list()
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                arr.append(nums1[i])
                i=i+1
            else: 
                arr.append(nums2[j])
                j=j+1
            k=k+1
        while i<len(nums1):
            arr.append(nums1[i])
            i=i+1
            k=k+1
        while j<len(nums2):
            arr.append(nums2[j])
            j=j+1
            k=k+1
        
        if len(arr)%2==0:
            low,high=0, len(arr)-1
            mid=low+(high-low)//2
            value1,value2=arr[mid],arr[mid+1]
            return (value1+value2)/2
        else:
            low,high=0, len(arr)-1
            ans=low+(high-low)//2
            return arr[ans]