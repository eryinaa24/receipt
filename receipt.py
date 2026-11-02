#S=item name
#Q=quantity
#U=price

S=str(input())
Q, U=input().split() #input() ambil dua nilai yang ditaip, manakala split() pisahkan nilai ikut ruang untuk Q dan U.
Q=int(Q)
U=float(U)

Total=Q*U

print(f"{S:<12}", f"{Q:>4}", f"{Total:>10.2f}")
#or print(f"{S:<12}{Q:>4}{Total:>10.2f}")  #cara lain untuk print tanpa ruang antara nilai.





#IPO
#Input: S,Q,U
#Process: total = Q*U
#Output: S(width=12, left-aligned), Q(width=4, right-aligned), Total(width=10, right-aligned, 2 decimal places)






#pseudocode
#START
#   Input S
#   Input Q, U
#   Total=Q*U
#   Print S(width=12, left-aligned), Q(width=4, right-aligned), Total(width=10, right-aligned, 2 decimal places)
#END

#YEAYY BALIK BOLEH TIDO
