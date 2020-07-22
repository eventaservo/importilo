import requests
import time

# ekzempla evento
# url = 'https://www.meetup.com/Esperanto-Calgary/events/qnqmgpybckbbc/'
# url = 'https://www.meetup.com/Austin-Esperanto/events/tflctrybclbcb/'


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
                                          res_json['duration'])/1000)
    )
    evento["enhavo"] = res_json["description"] + res_json.get("how_to_find_us", "")
    evento["priskribo"] = res_json["name"]


    return evento

