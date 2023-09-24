def linear_searchProduct(productList, targetProduct):
    indices = []
    for index, product in enumerate(productList):
        if product == targetProduct:
            indices.append(index)
    return indices

Products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = linear_searchProduct(Products, target)
print(result)
