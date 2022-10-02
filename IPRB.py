from itertools import product

k, m, n = 21, 18, 26
population = (k*['AA']) + (m*['Aa']) + (n*['aa'])

products = []
for first_organism in population:
    excluded_population = population.copy()
    excluded_population.remove(first_organism)

    for second_organism in excluded_population:
        products.extend(list(product(first_organism, second_organism)))

dominants = 0
for product in products:
    if product[0] == 'A' or product[1] == 'A':
        dominants += 1

probability = dominants/len(products)
print(probability)
