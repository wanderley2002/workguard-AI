import os
from datetime import datetime

import cv2
import pygame
from ultralytics import YOLO


class WorkGuardAI:

    def __init__(self):

        print("🤖 Iniciando WorkGuard AI...")

        # Inicializa o sistema de áudio
        pygame.init()

        # Carrega o modelo YOLO
        self.model = YOLO("yolo11n.pt")

        # Cria a pasta para salvar evidências
        os.makedirs("salvos", exist_ok=True)

        # Abre a câmera
        self.camera = cv2.VideoCapture(0)

        # Controla se uma foto já foi capturada
        self.foto_tirada = False

    def iniciar_camera(self):
        """Inicia o monitoramento da câmera."""

        if not self.camera.isOpened():
            print("❌ Não foi possível abrir a câmera.")
            return

        print("📷 Câmera iniciada!")
        print("🚨 Entre na área vermelha para testar o sistema.")
        print("📸 Uma foto será salva quando uma pessoa entrar na área.")
        print("📁 As fotos serão salvas em 'salvos'.")
        print("⌨️ Pressione Q para sair.")

        while True:

            # Captura um frame
            ret, frame = self.camera.read()

            if not ret:
                print("❌ Não foi possível capturar a imagem.")
                break

            # Tamanho da imagem
            altura, largura = frame.shape[:2]

            # Área de risco começa nos últimos 30%
            area_inicio_x = int(largura * 0.70)

            # YOLO analisa a imagem
            results = self.model(frame, verbose=False)

            pessoas = 0
            riscos = 0

            # Analisa as detecções
            for box in results[0].boxes:

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
                    centro_x = (x1 + x2) // 2

                    # Verifica se entrou na área de risco
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

                        # Texto de risco
                        cv2.putText(
                            frame,
                            "RISCO!",
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 0, 255),
                            2
                        )

                        # Captura evidência
                        if not self.foto_tirada:

                            nome_foto = datetime.now().strftime(
                                "pessoa_%Y-%m-%d_%H-%M-%S.jpg"
                            )

                            caminho = os.path.join(
                                "salvos",
                                nome_foto
                            )

                            cv2.imwrite(
                                caminho,
                                frame
                            )

                            self.foto_tirada = True

                            print("📸 FOTO CAPTURADA!")
                            print(f"💾 Salva em: {caminho}")

            # Desenha área de risco
            cv2.rectangle(
                frame,
                (area_inicio_x, 0),
                (largura, altura),
                (0, 0, 255),
                3
            )

            cv2.putText(
                frame,
                "AREA DE RISCO",
                (area_inicio_x + 15, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

            # Define status
            if riscos > 0:

                status = "ALERTA: AREA DE RISCO"
                status_cor = (0, 0, 255)

                print("🚨 ALERTA! Pessoa na área de risco!")

            else:

                status = "SISTEMA NORMAL"
                status_cor = (0, 255, 0)

                self.foto_tirada = False

            # Painel superior
            cv2.rectangle(
                frame,
                (0, 0),
                (largura, 90),
                (20, 20, 20),
                -1
            )

            # Nome do sistema
            cv2.putText(
                frame,
                "WORKGUARD AI",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            # Quantidade de pessoas
            cv2.putText(
                frame,
                f"Pessoas: {pessoas}",
                (20, 65),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )

            # Status
            cv2.putText(
                frame,
                status,
                (300, 55),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.65,
                status_cor,
                2
            )

            # Mostra câmera
            cv2.imshow(
                "WorkGuard AI",
                frame
            )

            # Q encerra
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.encerrar()

    def encerrar(self):
        """Libera os recursos utilizados."""

        self.camera.release()

        cv2.destroyAllWindows()

        pygame.quit()

        print("🛑 WorkGuard AI encerrado.")


if __name__ == "__main__":

    app = WorkGuardAI()

    app.iniciar_camera()