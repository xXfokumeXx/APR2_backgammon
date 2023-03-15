# APR2_backgammon

Detailní přehled pravidel ke hře k náhlednutí [zde] (https://www.hazardni-hry.eu/kostky/vrhcaby-backgammon.html)

Zadání seminární práce KI/(K)APR2 LS 2023
deadline September 2023.
------------------------------------------------------------
Vytvořte implementaci hry vrhcáby, která podporuje hru dvou hráčů či hru proti jednoduché umělé inteligenci.

**povinně implementovaná funkčnost:**
- generování hodu kostkami
- výpis všech možných tahů hráče
- jednoduchá umělá inteligence, která náhodně volí jeden z platných tahů
- trasování chodu každého jednotlivého kamene (od vstupu z baru po vyhození/vyvedení), herní pole se chovají jako zásobník.
- uložení a obnova stavu hry (s návrhem vlastního JSON formátu pro uložení)

**co musí zobrazovat displej (výpis na standardním vstupu)**
- výsledky hodů kostkami
- pozice všech kamenů na desce (včetně těch "na baru")
- stručný komentář toho, co se ve hře událo a nemusí být zřejmé ze zobrazení na desce (kámen vstoupil do hry, byl "vyhozen", opustil hru, hráč nemůže hrát tj. ani házet, pod.)
- počet vyvedených kamenů
- po výhře typ výhry
- po ukončení se zobrazí statistika o všech kamenech ve hře (zvlášť pro bílého a černého),
- například:   - počet kamenů vyhozených, vyvedených a opuštěných
               - průměrná životnost kamene v tazích

**nepovinná funkčnost:**
- GUI rozhraní
- inteligentnější AI

**implementované třídy:**
- Hra (Herní deska)
obsahuje:  
1. HerníPole (modifikovaný zásobník, lze vkládat jen kameny stejných barev)  
2. Dvojkostka (vrací seznam možných dvojic či čtveřic)  
3. Bar (továrna na herní kameny, s řízenou produkcí)  
- Herní kámen (s pamětí, kde se postupně nacházel)
- Hráč: odvozené třídy:  
1. KonzolovýHráč  
2. AIHráč
