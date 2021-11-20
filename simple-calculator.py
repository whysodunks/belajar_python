
# Fun adds two numbers
def add(x, y):
    return x + y

# Fun subtracts two numbers
def subtract(x, y):
    return x - y

# Fun multiplies two numbers
def multiply(x, y):
    return x * y

# Fun divides two numbers
def divide(x, y):
    return x / y


print("Pilih operasi.")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

while True:
    # take input from the user
    choice = input("Pilihan(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Masukan nilai pertama: "))
        num2 = float(input("Masukan nilai kedua: "))

        if choice == '1':
            print("Hasil dari ", num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print("Hasil dari ", num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print("Hasil dari ", num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print("Hasil dari ", num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Ingin mengulangi perhitungan? (y/n): ")
        if next_calculation == "n":
          break
    
    else:
        print("Masukan tidak valid")