import config as cfg
from dictionary import sitios_arqueologicos
def search_coincidences():
	clave=(cfg.cultura,cfg.estado,cfg.geography,cfg.estructura)
	# cfg.cultura = cfg.estado = cfg.geography = cfg.estructura = ""
	if clave in cfg.respuestas:
		pass
	else:
		(nombre,path_image,descripcion)=sitios_arqueologicos[clave]
	print(f"Nombre: {nombre}")
	print(f"Path de la imagen: {path_image}")
	print(f"Descripción: {descripcion}")
	# Code to search coincidences

def second_search():
	clave=(cfg.cultura,cfg.estado,cfg.geography,cfg.estructura, cfg.adition_info)
	(nombre,path_image,descripcion)=sitios_arqueologicos[clave]
	cfg.nombre=nombre
	cfg.path_image=path_image
	cfg.descripcion=descripcion
	