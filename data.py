import csv
import requests
import time

colegios = [] # Id;name;long;lat;capacidad
personas = [] # id;padron;long;lat
# distances = [] # 4605x63

with open('colegios.csv') as colegios_csv:
    csv_reader = csv.reader(colegios_csv, delimiter=';')
    line_cnt = 0
    for row in csv_reader:
        if line_cnt > 0:
            id = int(row[0])
            name = row[1]
            lat = float(row[2])
            lon = float(row[3])
            capacidad = int(row[4])
            colegios.append((id, name, lon, lat, capacidad))
        line_cnt += 1

with open('cuadras_maipu.csv') as personas_csv:
    csv_reader = csv.reader(personas_csv, delimiter=';')
    line_cnt = 0
    for row in csv_reader:
        if line_cnt > 0:
            id = int(row[0])
            padron = int(row[4])
            lon = float(row[5])
            lat = float(row[6])
            personas.append((id, padron, lon, lat))
        line_cnt += 1

# 1 to many
with open('distances_final.csv', mode='w') as distances_file:
    distances_writer = csv.writer(distances_file, delimiter=';')

    for person in personas:
        print("Persona ID: ", person[0])
        src_coord = str(person[2]) + "," + str(person[3]) + ";"
        dst_coord = ""

        for colegio in colegios:
            # print("\tColegio ID: ", colegio[0])
            dst_coord += str(colegio[2]) + "," + str(colegio[3]) + ";"

        url =  'http://127.0.0.1:3333/table/v1/driving/' + src_coord + dst_coord[:-1] + "?sources=0&annotations=distance"
        # print(url)
        
        response = requests.get(url)
        data = response.json()
        distances_writer.writerow(data["distances"][0][1:])


# 1 by 1
# with open('distances_final.csv', mode='w') as distances_file:
#     distances_writer = csv.writer(distances_file, delimiter=';')

#     for person in personas:
#         print("Persona ID: ", person[0])
#         src_coord = str(person[2]) + "," + str(person[3]) + ";"
#         dist_aux = []
#         time.sleep(0.01)
#         for colegio in colegios:
#             print("\tColegio ID: ", colegio[0])

#             dst_coord = str(colegio[2]) + "," + str(colegio[3])
#             # url =  'http://router.project-osrm.org/route/v1/driving/' + src_coord + dst_coord
#             url =  'http://127.0.0.1:3333/route/v1/driving/' + src_coord + dst_coord
#             # print(url)
#             response = requests.get(url)
#             data = response.json()
#             dist_aux.append(data["routes"][0]["distance"])

#         # distances.append(dist_aux)
#         distances_writer.writerow(dist_aux)