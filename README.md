
# Meme Generator

Meme Generator je preprosta spletna aplikacija za ustvarjanje
memov iz fotografij.

Uporabnik lahko naloži fotografijo, vnese zgornje in spodnje
besedilo ter ustvari novo sliko z besedilom.

## Uporabljene tehnologije

- Python
- Flask
- Pillow
- HTML
- Docker

## Funkcionalnosti

- Nalaganje fotografije
- Vnos zgornjega besedila
- Vnos spodnjega besedila
- Generiranje mema
- Prikaz ustvarjene slike v brskalniku

## Zagon aplikacije z Dockerjem

### 1. Gradnja Docker slike

```bash
docker build -t meme-generator .
```

### 2. Zagon Docker kontejnerja

```bash
docker run -p 5000:5000 meme-generator
```

### 3. Dostop do aplikacije

V brskalniku odprite:

http://localhost:5000

## Delovanje aplikacije

1. Uporabnik izbere fotografijo.
2. Vnese zgornje in spodnje besedilo.
3. Klikne gumb "Ustvari meme".
4. Flask prejme podatke iz obrazca.
5. Pillow doda besedilo na fotografijo.
6. Ustvarjena slika se prikaže v brskalniku.
