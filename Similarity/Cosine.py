''' 余弦相似度Cosine '''


def cos(vector1, vector2):
    dot_product, normA, normB = 0.0, 0.0, 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return dot_product / ((normA * normB) ** 0.5)


vector1 = [(1, 2, 5), (2, 3, 6), (1, 7, 5)]
vector2 = [(3, 4, 5), (1, 2, 5), (3, 10, 15)]
for i in vector1:
    for n in vector2:
        print(cos(i, n))
