class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        Len_nums1 = len(nums1)
        Len_nums2 = len(nums2)
        if (Len_nums1<=Len_nums2):
            for i in nums1:
                nums2=a.insert_element(i,nums2)
                print(nums2)
            #return nums2
            if (len(nums2)%2==0):
                FMed = (nums2[(len(nums2)-2)/2]+nums2[(len(nums2)-2)/2 +1])/float(2)
            else:
                FMed=nums2[(len(nums2)-1)/2]
            return FMed
        else:
            for i in nums2:
                nums1= a.insert_element(i,nums1)   
                print(nums1)
            #return nums1
            if (len(nums1)%2==0):
                FMed = (nums1[(len(nums1)-2)/2]+nums1[(len(nums1)-2)/2 +1])/float(2)
            else:
                FMed=nums1[(len(nums1)-1)/2]
            return FMed

    def insert_element(self,element,nums):    
        len_nums = len(nums)
        first_ind =0
        last_ind = len_nums-1
        first_ind_p = first_ind
        last_ind_p = last_ind
        nums_org = nums
        if len_nums%2 ==0:
            Med_nums =  Med_nums = (nums[(len_nums-2)/2]+nums[(len_nums-2)/2 +1])/float(2)
        else:
            Med_nums = nums[(len_nums-1)/2]
        i = 0  
        while (last_ind-first_ind>0):
            #print(last_ind,first_ind)
            if element >= Med_nums:
                # need to be compared with the second half of the list
                if ((last_ind-first_ind)+1)%2 ==0:
                    firstFa_ind = ((last_ind-first_ind)+1)/2
                    first_ind = firstFa_ind+first_ind
                    Med_index,Med_nums=a.calc_median(first_ind,last_ind,element,nums)
                    #Med_nums = (nums[Med_index]+nums[Med_index+1])/2
                    
                else:
                    firstFa_ind = (((last_ind-first_ind)+1)+1)/2
                    first_ind = firstFa_ind+first_ind
                   # len_nums = (len_nums-1)/2
                    Med_index,Med_nums=a.calc_median(first_ind,last_ind,element,nums)
                    #Med_nums = nums[Med_index]
            else :
                if ((last_ind-first_ind)+1)%2 ==0:
                    lastFa_ind = ((last_ind-first_ind))/2 
                    last_ind =lastFa_ind +first_ind
                    len_nums = len_nums/2
                    Med_index,Med_nums=a.calc_median(first_ind,last_ind,element,nums)
                    #Med_nums = (nums[Med_index]+nums[Med_index+1])/2
                else:
                    lastFa_ind = (((last_ind-first_ind)) -1)/2 
                    last_ind = lastFa_ind+first_ind
                    len_nums = (len_nums-1) /2
                    Med_index,Med_nums=a.calc_median(first_ind,last_ind,element,nums)
                    #Med_nums = nums[Med_index]
        
        
        
        
        
        if(element>=nums[last_ind]):
            if last_ind!=len(nums)-1 and nums[last_ind]!= nums[last_ind+1]:
                return nums[:last_ind+1]+[element]+nums[last_ind+1:]  
            elif last_ind==len(nums)-1:
                return nums[:last_ind+1]+[element]
            else:
                while(nums[last_ind]!= nums[last_ind+1] and last_ind+1 <len(nums)):
                     last_ind = last_ind+1
                if(last_ind +1==len(nums)):
                    return nums[:last_ind+1]+[element]
                else:
                    return nums[:last_ind+1]+[element]+nums[last_ind+1:] 
        
        else:
            if last_ind!=0 and nums[last_ind]!= nums[last_ind-1]:
                return nums[:last_ind]+[element]+nums[last_ind:]
            elif last_ind==0: 
                return [element]+nums[last_ind:]
            else:
                while(nums[last_ind]!= nums[last_ind-1] and last_ind-1 >=0):
                    last_ind = last_ind-1
                if(last_ind -1<0):
                    return [element]+nums[last_ind:]
                else:
                    return nums[:last_ind]+[element]+nums[last_ind:]
     
        
          
       
       
    def calc_median(self,start, end,element,nums):
        if (end -start) %2 ==0:
            # odd
            return ((end-start)/2)+start ,nums[((end-start)/2)+start]
               
        else:
            return((end-1)-start)/2+start,nums[((end-1)-start)/2+start]
        
        
a= Solution()
List1=[3]
List2=[1,2,4,5]
Med = a. findMedianSortedArrays(List1, List2)
print(Med)