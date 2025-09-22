def divisorSubstrings(num, k):
        s = str(num)
        val_check = s[:k]
        
        for i in range(len(s) - k + 1):
                val_check = int(s[i: i+k])
                if val_check != 0 and num % val_check == 0:
                        count += 1



      