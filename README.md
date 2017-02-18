# Next-Bigger-Number
參考 https://dotblogs.com.tw/hatelove/2017/02/08/codewars-next-bigger-number-by-tdd 的題目
使用recursive演算法，先忽略陣列及數字的轉換: 

Next(in):
  R = in[0] 
  LA = in[1:]
  L = Next(LA)
  if (L != -1):
    return( R + L)
  else:
    R1=NextOne(R, LA)             #LA陣列中比R大的最小數字
    if (R1 is None): return(-1)   #若無更大的數字
    return (R1 + Sort(LA-R1 + R)) #R1 + 最小序列
