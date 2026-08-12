
import cv2
from ultralytics import YOLO


class Detector:

    def __init__(self):

        print("🧠 Carregando modelo YOLO...")

        self.model = YOLO("../yolo11n.pt")

        print("✅ Modelo carregado!")


    def detectar(self, frame):

        # Executa o YOLO no frame recebido
        resultados = self.model(
            frame,
            verbose=False
        )

        pessoas = 0
        riscos = 0

        altura, largura = frame.shape[:2]

        # Área de risco começa nos últimos 30%
        area_inicio_x = int(
            largura * 0.70
        )

        # Analisa cada objeto detectado
        for box in resultados[0].boxes:

            classe = int(box.cls[0])

            # Classe 0 = pessoa
            if classe == 0:

                pessoas += 1

                # Coordenadas da pessoa
                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                # Centro da pessoa
                centro_x = (
                    x1 + x2
                ) // 2


                # Verifica área de risco
                if centro_x >= area_inicio_x:

                    riscos += 1

                    # Caixa vermelha
                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 0, 255),
                        3
                    )

                    # Texto
                    cv2.putText(
                        frame,
                        "RISCO!",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2
                    )


        # Desenha área de risco
        cv2.rectangle(
            frame,
            (area_inicio_x, 0),
            (largura, altura),
            (0, 0, 255),
            3
        )


        # Texto da área
        cv2.putText(
            frame,
            "AREA DE RISCO",
            (
                area_inicio_x + 10,
                35
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )


        # Retorna os resultados
        return frame, pessoas, riscos

