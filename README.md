# Sillabusz


A környezet összeállítása. Az előadás Python 3.9-et használ, a requirements.txt fájlban megadott csomagokkal. Az előadás fóliák lefuttathatók az abban levő csomagok telepítése után. Ehhez tehát szükséges:
* Egy Python 3.9 környezet létrehozása. Ez történhet `venv`-vel, de az egyszerűség kedvéért egy Anacondával könnyen lehet megadott Python verziójú környezetet létrehozni. Pl. `conda create -n python-course python==3.9` a parancssorból, Windowson pedig az Anaconda Navigator GUI-ból is lehet.
* A létrehozott környezetben telepítsük a szükséges csomagokat: `pip install -r requirements.txt`

Hogy milyen gyorsan fogok tudni haladni, azt nem tudom előre, ott a helyszínen fog eldőlni.


## 1. óra


A Python nyelvről röviden, a szokásos buzzword-ok felsorolása: erősen típusos, dinamikus, (fordított és) interpretált, több programozási paradigmát támogató, garbage collected nyelv.
Az utóbbi években az egyik legnépszerűbb programozási nyelvvé vált. Könnyen tanulható, gyorsan lehet kódot írni benne, nagy felhasználóbázisa van, sok könyvtár, rengeteg online tutorial, kurzus, papír alapú könyv elérhető, az adatelemzés, gépi tanulás, deep learning lingua franca-ja (Azaz a gyakran C-ben, C++-ban írt kód köré tett Python wrapper kód teszi tömegek számára elérhetővé ezeket a területeket). "Hello, world!", változók, aritmetikai műveletek, nevezéktan.

## 2. óra

Logikai értékek, összehasonlító operátorok, `a == b` vs. `a is b`, if-elif-else, értékadás, if-else-kifejezés (a Python-os ternáris operátor-szerűség), sztringek. Metódusok sztringeken, immutable adatszerkezet, indexelés. Range, for-ciklus, while-ciklus, (break, continue). Ez utóbbi kettő általában nem szükséges, de azért elmondom.


## 3. óra

Függvények, függvényparaméterek átadása pozíció és név alapját, visszatérési érték. Rekurzív függvények, névtér és érvényességi kör. A Python beépített lineáris adatszerkezetei: lista és tuple. Egy lista logikai értéke, hogyan tesszük feltételbe, hogy egy lista (string, tuple, stb.) üres-e? Lambda-függvény, list comprehension, slicing.


## 4. óra

További alapvető adatszekezetek: dictionary, set, frozenset. A collections könyvtár néhány adatszerkezete: defaultdict, namedtuple, Counter.

Kivételek kezelése, fájlbeolvasás, adat beolvasása standard inputról.


## 5. óra

Néhány algoritmustervezési módszer: rekurzió, memoization (cache-elés), dinamikus programozás(-szerűség), brute-force. A
2-SUM feladat burute-force megoldása. Mese programozási paradigmákról, bevezetés az OOP-be. Osztály, példány. Osztályok
alkalmazása: 1) állapotot akarunk fenntartani, pl. bankszámla vezetés, 2) adatot tárolunk és manipulálunk úgy, hogy a részleteket elrejtjük a felhasználó elől (encapsulation, abstraction), a verem adatszerkezet (esetleg hashtábla implementálása kézzel). Operátor túlterhelés, a
beépített Python függvények és operátorok kiterjesztése általunk definiált adatszerkezetre. A racionális számokra és a velük való műveletekre készítsük osztályt.

## 6. óra

További fejezetek az OOP-ből, egyéb mágikus osztálymetódusok: rendezés, a callable osztály. Öröklődés (csak érintőlegesen), a Python sztenderd könyvtár néhány modulja.


### 7. óra

A funkcionális programozási paradigma, map és filter. Generátorok, next és yield. Az itertools könyvtár. Végtelen sorozatok kezelése. Imperatív vs. funkcionális stílus.

A Numpy alapjai. Vektorok és mátrixok készítése, indexelés.

### 8. óra

Numpy második rész. Vektor és mátrixműveletek, mátrix determináns, inverz, lineáris egyenletrendszerek megoldása. Egyszerű matplotlib ábrák készítése, egyszerűbb alkalmazások képfeldolgozásból.

### 9. óra

A pandas könyvtár, egy táblázatos adatsor elemzése. (Még nem tudom milyen adaton)

### 10. órától

Algoritmikus gondolkodás. Számelméleti algortimusok, prímszámok, gráfelméleti algoritmusok: gráfok bejárása, szélességi keresés, összefüggő komponensek, rendezések (insertion sort, merge sort), stb.
