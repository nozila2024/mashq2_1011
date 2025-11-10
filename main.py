#1-misol
n = "Salom Nozila"
uz = len(n)
print(n[uz // 2])

#2-misol
n = input("Matn kiriting: ")

if n[0] == "a" or n[0] == "A":
    print("YES")
else:
    print("NO")

#3-misol
n = "Salom Nozila"

count = 0
for i in range(len(n)):
    if n[i] == "a":
        count += 1

print(f"Matnda {count} ta 'a' harfi bor")

#4-misol
n = "Salom Gulshoda"
print(n)

for i in range(len(n)-1, -1, -1):
    print(n[i], end="")

print(n[::-1])

#5-misol
ism = input("Ism kiriting: ")
fam = input("Familya kiriting: ")
n = ism + fam
print(n)
