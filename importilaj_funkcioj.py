import requests
import time
from bs4 import BeautifulSoup


def importas_el_meetup(url):
    '''
    Funkcio trovas informojn pri evento en meetup.com
    Uzas API laux tiu priskribo:
    https://www.meetup.com/meetup_api/docs/:urlname/events/:id/#get
    :param url: ligilo al la pagxo de la evento en meetup
    :return: vortarobjekto kun informoj
    '''
    evento = {}

    idx = url.split("/")

    grupo = idx[3]
    id = idx[5]

    res = requests.get(f"https://api.meetup.com/{grupo}/events/{id}")
    res_json = res.json()
    if res.status_code != 200:
        code = res_json["errors"][0]["code"]
        message = res_json["errors"][0]["message"]
        retrokuplo = f"{code} {message}"

        if res.status_code == 404:
            if code == "event_error" and message == "invalid event":
                retrokuplo = f"evento '{id}' ne ekzistas"
            elif code == "group_error" and message.startswith("Invalid group urlname"):
                retrokuplo = f"grupo '{grupo}' ne ekzistas"

        return f"importado ne sukcesis: {retrokuplo}"

    evento["titolo"] = grupo + ": " + res_json["name"]
    evento["urbo"] = res_json["venue"].get("city")
    evento["ligilo"] = res_json["link"]
    evento["reta"] = res_json["is_online_event"]
    evento["landa_id"] = res_json["venue"].get("country")
    evento["latitudo"] = res_json["venue"].get("lat")
    evento["longitudo"] = res_json["venue"].get("lon")
    evento[
        "adreso"
    ] = f"{res_json['venue'].get('name')}, {res_json['venue'].get('address_1')}"
    evento["horzono"] = res_json["group"]["timezone"]
    evento["komenco"] = res_json["local_date"] + " " + res_json["local_time"]
    evento['fino'] = time.strftime(
        '%Y-%m-%d %H:%M:%S', time.gmtime((res_json['time'] + res_json['utc_offset'] +
                                          res_json['duration']) / 1000)
    )
    evento["enhavo"] = BeautifulSoup(res_json["description"] + res_json.get("how_to_find_us", ""),
                                     'html.parser').get_text()

    evento["priskribo"] = res_json["name"]

    return evento


def importas_el_duolingo(url):
    '''
    Trovas detalojn de la evento en duolingo
    :param url: str, ligilo al la detala pagxo de la evento
    :return: vortarobjekto kun informoj
    '''
    evento = {}
    idx = url.split("/")

    if idx.count('events') == 0:
        return evento, "importa URL. Bezonata formato estas 'https://events.duolingo.com/events/details/:id/'"

    res = requests.get(url)
    if res.status_code != 200:
        return f"importado ne sukcesis: {res.status_code} {res.reason}"

    pagxo = BeautifulSoup(res.text, 'html.parser')

    # trovu la eventan id
    eventa_id = pagxo.form['eventid']
    # prenu la json el API
    res_api = requests.get(f'https://events.duolingo.com/api/event/{eventa_id}')
    res_api_json = res_api.json()
    if res_api.status_code != 200:
        return f"importado ne sukcesis: {res.status_code} {res.reason}"

    # trovu koordinatoj
    # adreso = f"{res_api_json.get('venue_address')}, {res_api_json.get('venue_city')},
    # {res_api_json['chapter']['country']}"
    # koordinatoj = uzu geopy?

    evento["titolo"] = res_api_json['chapter']['title'] + ': ' + res_api_json['title']
    evento["urbo"] = res_api_json.get('venue_city')
    evento["ligilo"] = res_api_json['url']
    if res_api_json['event_type'] == 5:
        evento["reta"] = True
    else:
        evento["reta"] = False
    evento["landa_id"] = res_api_json['chapter']['country']
    # evento["latitudo"]  = koordinatoj['latitudo']
    # evento["longitudo"] = koordinatoj['longitudo']
    try:
        evento["adreso"] = res_api_json.get('venue_name') + ' ' + res_api_json.get('venue_address')
    except TypeError:
        if evento['reta'] == True:
            evento['adreso'] = 'Rete'
    evento["horzono"] = res_api_json['chapter']['timezone']
    evento["komenco"] = res_api_json['start_date_naive'].replace('T', ' ')[:-3]
    evento['fino'] = res_api_json['end_date_naive'].replace('T', ' ')[:-3]
    evento["enhavo"] = BeautifulSoup(res_api_json['description'], 'html.parser').get_text()
    evento["priskribo"] = res_api_json['description_short']

    return evento
