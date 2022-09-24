import cv2

# Leer imagen
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sol",
            (100, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Mercurio",
            (150, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Venus",
            (200, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Tierra",
            (250, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Marte",
            (300, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Júpiter",
            (350, 150),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Saturno",
            (400, 100),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Urano",
            (450, 100),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Neptuno",
            (500, 100),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )


# Mostrar imagen a color
cv2.imshow("Output",img)

cv2.imwrite(“Solar_systemwithname.jpg”,img)

# Tiempo indefinido
cv2.waitKey(0)