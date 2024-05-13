1. Introduction

a) Programos apžvalga:

ATM finansų sekiklis yra „Python“ programa, skirta simuliuoti Automatizuotos bankomato mašinos (ABM) funkcionalumą su papildomomis funkcijomis asmeninių ir bendrų finansų sekimui.
artotojai gali atlikti įprastinius banko operacijas, tokius kaip pinigų indėliavimas, išėmimas ir sąskaitų balansų tikrinimas iš jų asmeninių sąskaitų. 
Be to, jie gali kurti ir tvarkyti bendravimo sąskaitas, kad kartu tvarkytų lėšas su kitais vartotojais.

b) Programos paleidimas:

Norėdami paleisti programą, įsitikinkite, kad jūsų sistemoje įdiegtas „Python“. Skriptą galite paleisti savo pageidaujamu „Python“ aplinkoje, pvz.: Visual Studio Code programoje paspaude dešiniame kampe programoje mygtuką "Run Python file".

c)Programos naudojimas:

Paleidus programą, bus prašoma įvesti savo vardą. Kai esate tapatintas, pagrindiniame meniu turėsite prieigą prie įvairių parinkčių:

1. Deposit money to personal account
2. Withdraw money from personal account
3. Check balance of personal account
4. Create sharing account
5. Deposit, withdraw, or check balance for sharing account
6. Quit

Tiesiog pasirinkite norimą parinktį įvedę atitinkamą numerį. Sekite nurodymus, kad užbaigtumėte kiekvieną veiksmą, pvz., įvedant indėlio arba išėmimo sumą. Programa teikia grįžtamąjį ryšį ir nurodymus visą procesą.

2. Body/Analysis

Abstraction:
![image](https://github.com/LukasSvederskis/Kursinis_Lukas/assets/144675751/09ff2caf-5558-4470-8adb-5327f49286b2)
Čia panaudotas abstraction: 
Konstruktorius (__init__ metodas).
Duomenų nuskaitymas ir inicializavimas:
Metodai load_current_balances ir load_user_accounts.


Failo skaitymas: 
![image](https://github.com/LukasSvederskis/Kursinis_Lukas/assets/144675751/0f03e0c6-4600-4487-b03c-4a9d5725e558)

Istorijos išsaugojimas:
![image](https://github.com/LukasSvederskis/Kursinis_Lukas/assets/144675751/ba476ea2-8734-4f40-a32b-de4e566faa26)

3. Results and Summary

Results:

Programa sėkmingai valdo asmenines ir bendras sąskaitas.
Vartotojai gali įnešti pinigus į savo asmeninę sąskaitą, iš jos išsiimti ir patikrinti likutį.
Vartotojai gali kurti bendras sąskaitas, pridėti į jas kitus vartotojus ir vykdyti indėlių, išėmimų ir likučio patikrinimo operacijas bendroje sąskaitoje, jei yra jos nariai.
Visos operacijos įrašomos į failą (kita.txt), kad būtų galima saugoti įrašus.
Programa teikia vartotojui draugišką sąsają su aiškiais meniu pasirinkimais.

Summary:

Pinigų išėmimo automatai "Finansų sekiklis" suteikia patogų būdą vartotojams valdyti savo asmenines ir bendras sąskaitas, užtikrinant lengvą prieigą prie finansinių informacijos ir operacijų.
Programa suprojektuota paprastai ir intuityviai, todėl tinkama asmeniniam naudojimui arba mažai apimties bendravimo susitarimams tarp draugų ar šeimos narių.

How it would be possible to extend your application:

Įdiegiant autentifikaciją ir vartotojų sąskaitas: Vartotojų autentifikacijos mechanizmų įvedimas gali pagerinti saugumą ir leisti daugeliui vartotojų gauti prieigą prie programos su savo prisijungimo duomenimis.
Papildomų transakcijų funkcijų įgyvendinimas: Įtraukiant funkcijas, tokiu kaip pinigų pervedimas tarp asmeninių ir bendrų sąskaitų, sąskaitų apmokėjimai ar reguliarių operacijų nustatymas, galima išplėsti programos funkcionalumą.
Gerinant bendros sąskaitos valdymą: Suteikiant galimybę bendros sąskaitos savininkams valdyti vartotojų leidimus, nustatyti išlaidų ribas arba automatizuoti lėšų paskirstymą, galima padaryti bendros sąskaitos funkcionalumą patikimesnį.




