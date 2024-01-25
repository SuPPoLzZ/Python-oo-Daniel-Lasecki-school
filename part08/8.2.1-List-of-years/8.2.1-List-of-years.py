from datetime import date




def vuodet_listaan(vuodet):
    vuodet = [paiva.year for paiva in vuodet]
    vuodet.sort(reverse=False)
    return vuodet


paiva1 = date(2019, 2, 3)
paiva2 = date(2006, 10, 10)
paiva3 = date(1993, 5, 9)

vuodet = vuodet_listaan([paiva1, paiva2, paiva3])
print(vuodet)