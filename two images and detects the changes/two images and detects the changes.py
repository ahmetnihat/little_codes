from PIL import Image ,ImageChops # PIL lütüphanesin Image ve ImageChops çağırıldı.
import cv2 # OpenCV kütüphanesi çağırıldı.

# Fark bulma fonksiyonu oluşturuldu.
def FarkBulma4RGB(img1,img2): # Fonksiyon içine 2 resim alıyor.

# Kıyaslanan resimler aynı boyutta olduğu varsayılarak

    h = img1.shape[0] # 1. resmin yükseliği h değişkenine atandı.
    w = img1.shape[1] # 1. resmin genişliği w değişkenine atandı.
    
    # Resmin üzerinde, piksellerinde for döngüsü ile geziniyoruz
    for y in range(0, h):   # 0'dan h'a kadar dönüyoruz bulunduğumuz her piksel y koordinatını veriyor.
        for x in range(0, w): # Bulunduğumuz her piksel x koordinatını veriyor.
            # Piksel renklerini değişkenlere atıyoruz.
            b = img1[y, x, 0] # (x,y) koordinatındaki mavi değerini b'ye atandı.
            g = img1[y, x, 1] # Yeşil değer g değişkenine atandı.
            r = img1[y, x, 2] # Kırmızı değer r değişkenine atandı.
            
            bgr = b + g + r # 1. resmin renk kodlarını topluyoruz.
            # Renk kodları 0-255 aralığındaki değerlerden oluşur.
            
            b2,g2,r2 = img2[y, x] # 2. resmin o anki (x,y) koordinatındaki renkleri alıyoruz.
            bgr2 = b2 + g2 + r2 # Aldığımız renk değerlerini topluyoruz.
            
            
            # 1. resmin ve 2. resmin o anki piksel konumlarının renk değerlerinin
            if bgr != bgr2: # toplamı biribirine eşit değilse
                img2[y, x] = (255, 255, 255) # 2. resmin o anki piksellerini
                # (255,255,255) beyaz yap.
    
    return img2 # yeni oluşan 2. resmi döndür.



img1 = cv2.imread("11.jpg") # 1. resmimizi OpenCV kütüphanesindeki imread fonksiyonu
# ile okuyoruz.

img2 = cv2.imread("22.jpg") # 2. resmi de okuyouruz.

cv2.imshow("resim2", img2) # 2. resmi ekrana yansıtıyoruz.

fark = FarkBulma4RGB(img1, img2) # 2 resmi vererek fonksiyonumuzu çalıştırıyoruz.
# 2. resmin üzerinde işaretlenen farklarla dönenecek olan 2. resmimizi fark
# değişkenine atıyoruz.

cv2.imshow("resim1", img1) # 1. resmi ekrana yansıtıyoruz.

cv2.imshow("Fark", fark) # 2. resmi üzerindeki farklar beyaza boyanmış olarak
# ekrana yansıtıyoruz.



image1=Image.open("11.jpg") # PIL kütüphanesi yardımıyla 1. resmi okuyoruz.
image2=Image.open("22.jpg") # PIL kütüphanesi yardımıyla 2. resmi okuyoruz.

fark = ImageChops.difference(image1, image2) # PIL kütüphanesindeki ImageChops içindeki
# difference fonksiyonu ile 2 resim arasındaki farkları buluyoruz.

if fark.getbbox(): # Eğer getbbox() fonksiyonumuz boş dönmüyorsa.
    fark.show() # Farklı olan nesneleri gösteriyoruz.

cv2.waitKey(0) 
cv2.destroyAllWindows() 