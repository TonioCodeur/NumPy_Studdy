import numpy as np

# Découverte de NumPy
arr = np.array([1, 2, 3])

print("Version de NumPy :", np.__version__)
print("Array            :", arr)
print("Type             :", arr.dtype)
print("Dimensions       :", arr.ndim)
print("Forme (shape)    :", arr.shape)
print("Somme            :", arr.sum())
print("Moyenne          :", arr.mean())
print("Array * 2        :", arr * 2)

arr2 = np.ones((4, 3))
print("Array 2          :")
print(arr2)

arr3 = np.zeros((9, 7))
print("Array 3          :")
print(arr3)
print(arr3[: , 5])  # Affiche la 6ème colonne de arr3

x = np.array([_/100 for _ in range(300)])
print("Array x          :")
print(x)
print(np.exp(x))  # Affiche l'exponentielle de chaque élément de x
print(np.cos(x))  # Affiche le cosinus de chaque élément de x
print(np.sin(x))  # Affiche le sinus de chaque élément de x
print(np.log(x))  # Affiche le logarithme de chaque élément de x
print(np.round(np.exp(x), decimals=2))  # Affiche l'exponentielle arrondie à 2 décimales