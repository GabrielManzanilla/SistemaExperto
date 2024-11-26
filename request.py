import config as cfg
from dictionary import sitios_arqueologicos
def search_coincidences():
	clave=(cfg.cultura,cfg.estado,cfg.geography,cfg.estructura)
	# cfg.cultura = cfg.estado = cfg.geography = cfg.estructura = ""

	(nombre,path_image,descripcion)=sitios_arqueologicos[clave]
	print(f"Nombre: {nombre}")
	print(f"Path de la imagen: {path_image}")
	print(f"Descripción: {descripcion}")
	# Code to search coincidences