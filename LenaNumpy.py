from PIL import Image
import numpy as np

def salvar_negativo(img: 'np.ndarray'):

    img = np.array(Image.open('lena.jpg'))
    #print(img.shape) # vai dar pixels, pixels, canais de cores

    negativo = 255 - img
    Image.fromarray(negativo).save('lena_negativo.jpg')

def salvar_canal_cor(img: 'np.ndarray', cor: str):
    img_copia = img.copy()
    if cor == 'vermelho':
        img_copia[:, :, (1, 2)] = 0
    elif cor == 'verde':
        img_copia[:, :, (0, 2)] = 0
    else: #cor azul
        img_copia[:, :, (0, 1)] = 0
    Image.fromarray(img_copia).save(f'lena_{cor}.jpg')

img = np.array(Image.open('lena.jpg'))

salvar_negativo(img)

salvar_canal_cor(img, 'vermelho')
salvar_canal_cor(img, 'verde')
salvar_canal_cor(img, 'azul')

print('Imagens salvas com sucesso!')