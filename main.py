from ultralytics import YOLO
#Lien du model https://huggingface.co/melihuzunoglu/human-fall-detection/resolve/main/best.pt
modele = YOLO("best.pt")

def detecter_chute(image_path, confiance=0.25):

    resultats = modele.predict(
        source=image_path,
        conf=confiance,
        save=False,
        verbose=False
    )
    r = resultats[0]
    #names affiche la position de chaque reponse. Si dans r.boxes.cls 0 qui est le code pour fallen se trouve en première position, y a chute
    code_responses=r.names[0]
    resultats_cls=r.boxes.cls
    resultats_cls_str=str(resultats_cls)
    clean_resultats_cls_str=resultats_cls_str.replace("tensor([","").replace(".])","")
    if clean_resultats_cls_str == "0":
        print("Y a chute")


if __name__ == "__main__":

    resultat = detecter_chute("images2.jpeg")
