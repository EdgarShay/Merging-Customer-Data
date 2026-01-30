def merge(customerData1, m, customerData2, n):
    """
    Merge sorted arrays:  modify customerDataa in-place to contain the merged sorted values from the first m elements 
    of customerData1 and the first n elements of customerData2.
    """
    i = m -1 # poiter for customerData1
    j = n -1 # pointer for customerData2
    k = m + n -1 # Pointer for merged array

    while 1 >= 0 and j >= 0:
        if customerData1[i] > customerData2[j]:
            customerData1[k] = customerData1[i]
            i -= 1
        else:
            customerData1[k] = customerData2[j]
            j -= 1
            k -=1
            while j >=0:
                customerData1[k] = customerData2[j]
                j -= 1
                k -= 1
                return customerData1

if __name__ == "__main__":
	data1 = [101, 104, 107, 0, 0, 0]
	data2 = [102, 105, 108]
	merge(data1, 3, data2, 3)
	print(data1)
