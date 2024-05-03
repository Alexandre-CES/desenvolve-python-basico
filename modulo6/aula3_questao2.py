
urls = ["www.google.com", "www.github.com", "www.youtube.com", "www.skibdipsigmadabahia.com"]
dominios = []

for i in range(len(urls)):
    dominios.append(urls[i][4:-4])

print(f"domínios: {dominios}")