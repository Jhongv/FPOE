import requests
respuesta= requests.get("http://localhost:8000/")
print(respuesta.content)

data= {
	"nombre": "Victor",
	"apellido": "Tabares",
	"estatura": 154,
	"peso": 34
}
respuesta= requests.post("http://localhost:8000/v1/persona", data=data)
print(respuesta.status_code)
print(respuesta.content)

