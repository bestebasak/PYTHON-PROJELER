def spormenu():
print("╔══════════════════════════╗")
print("║      SPOR TÜRLERİ        ║")
print("║ 1-Voleybol               ║")
print("║ 2-Futbol                 ║")
print("║ 3-Hentbol                ║")
print("║ 4-Güreş                  ║")
print("║                          ║")
print("║         SEÇİNİZ          ║")
print("╚══════════════════════════╝")
secim = int(input("Seçiminizi yapın: "))
    if secim == "1" : print("Voleybol, file ile ikiye bölünmüş bir oyun alanı üzerinde altı kişilik iki takım ile oynanan, 
                        voleybol topuna eller ve kollarla vurarak file üzerinden karşı tarafın oyun alanına gönderme ve yere değmesini sağlama esasına dayalı bir takım sporudur.")
    elif secim == "2" : print("Futbol, on bir oyuncudan oluşan iki takımın sahada topu rakip takımın kalesine atma mücadelesinin verildiği bir spor dalıdır.
                           Futbol, iki takım, bir futbol sahası ve hakemlerin varlığında oynanabilmektedir. Her takımda kaleci, savunma, orta saha ve hücum oyuncuları farklı pozisyonda bulunur.")
    elif secim == "3" : print("Hentbol, altısı saha içinde, biri kalede olmak üzere yedi oyuncuyla oynanan bir takım sporudur. Oyun süresi otuz dakikalık iki devreden oluşur.
                               İlk yıllarında futbol stadyumlarında 11 kişilik takımlar halinde çim üzerinde oynanan hentbol, 1950'lerden sonra yaygın bir salon sporu haline dönüşmüştür.")                        
    else secim == "4" : print("Güreş, uygulayıcılarının birbirlerine vurmaksızın rakiplerini yenmeye çalıştıkları bir dövüş sporu türü. Güreş tarihteki en eski sporlardan biridir ve zamanla farklı stil ve formları geliştirilmiştir.
                               Güreş genellikle dövüş sanatları arasında değerlendirilir.")                           
input()
