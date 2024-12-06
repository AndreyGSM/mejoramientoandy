import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import current_app

def configurar_cloudinary():
    """Configura Cloudinary usando las credenciales del archivo de configuración."""
    cloudinary.config(
        cloud_name=current_app.config.get('CLOUDINARY_URL').split('@')[1],
        api_key=current_app.config.get('CLOUDINARY_URL').split('://')[1].split(':')[0],
        api_secret=current_app.config.get('CLOUDINARY_URL').split(':')[2].split('@')[0]
    )

def subir_imagen(imagen, carpeta=None):
    """Sube una imagen a Cloudinary.
    
    Args:
        imagen: Un archivo de imagen (por ejemplo, request.files['archivo']).
        carpeta: La carpeta en Cloudinary donde se guardará la imagen.
    Returns:
        dict: Información sobre la imagen subida (incluyendo la URL).
    """
    configurar_cloudinary() 
    opciones = {"folder": carpeta} if carpeta else {}
    resultado = cloudinary.uploader.upload(imagen, **opciones)
    return resultado
