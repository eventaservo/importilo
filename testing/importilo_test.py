import vcr
import importilaj_funkcioj

# tiel vcr kreas kaseton samnoman kiel la funkcio
@vcr.use_cassette()
def test_meetup():
    url_meetup = "https://www.meetup.com/Esperanto-Toronto/events/nbplfqyzmbfb/"
    evento = importilaj_funkcioj.importas_el_meetup(url_meetup)
    expected = {
        "titolo": "Esperanto-Toronto: Socia kunveno",
        "urbo": "Toronto",
        "ligilo": "https://www.meetup.com/Esperanto-Toronto/events/nbplfqyzmbfb/",
        "reta": False,
        "landa_id": "ca",
        "latitudo": 43.66590881347656,
        "longitudo": -79.38521575927734,
        "adreso": "Aroma Espresso Bar,  618 Yonge Street",
        "horzono": "Canada/Eastern",
        "komenco": "2019-09-03 18:00",
        "fino": "2019-09-03 19:30:00",
        "enhavo": "English below Ni kunvenas unufoje monate por trinki kafon kaj ĝui "
        "konversacion en Esperanto pri io ajn. Je 19:30 kelkaj el ni iras al "
        "unu el la apudaj restoracioj por manĝi kaj daŭrigi la konversaciojn. "
        "Se vi vizitos nin el eksterurbe kaj vi ne povas trafi unu el ĉi tiuj "
        "kunvenoj, bonvolu sendi retmesaĝon al esperanto.toronto(ĉe)gmail.com, "
        "por ke ni eventuale povu ŝanĝi la daton de unu kunveno, aŭ aldoni "
        "kroman. We meet once a month to drink coffee and enjoy conversation "
        "in Esperanto about anything. At 7:30 some of us go to one of the "
        "nearby reastaurants to eat and continue the conversations. If you "
        "are visiting us from out of town and can’t make one of these "
        "meetings, please send an email to esperanto.toronto(at)gmail.com so "
        "that we can change the date of one meeting or add another one in "
        "order to accommodate you. Ĉe la okcidenta flanko de Yonge Street, "
        "unu strato norde de Wellesley Street (metroo Wellesley) / On the west "
        "side of Yonge Street, one block north of Wellesley Street "
        "(Wellesley subway)",
        "priskribo": "Socia kunveno",
    }
    assert evento == expected


@vcr.use_cassette()
def test_duolingo():
    url_duolingo = (
        "https://events.duolingo.com/events/details/"
        "duolingo-guadalajara-esperanto-presents-tria-renkontigon/"
    )
    evento = importilaj_funkcioj.importas_el_duolingo(url_duolingo)
    expected = {
        "titolo": "Guadalajara Esperanto: Tria renkontiĝon",
        "urbo": "Guadalajara, Jalisco",
        "ligilo": "https://events.duolingo.com/events/details/"
        "duolingo-guadalajara-esperanto-presents-tria-renkontigon/",
        "reta": False,
        "landa_id": "MX",
        "adreso": "El gato Calle Francisco I. Madero 833, Col Americana, Americana",
        "horzono": "America/Mexico_City",
        "komenco": "2020-03-07 17:00",
        "fino": "2020-03-07 21:00",
        "enhavo": "Vamos a tener otra reunión, esta vez vamos a hablar sobre el futuro "
        "del esperanto en gdl.No se preocupe si su nivel de esperanto es bajo."
        " Cualquier nivel es bienvenido",
        "priskribo": "Saluton al ĉiuj. "
        "ni tuj havos alian renkontigxo.\n"
        "Via nivelo de esperanto ne estas problemo Aliĝu al ni",
    }
    assert evento == expected
