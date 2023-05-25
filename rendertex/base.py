import os
import cv2
import matplotlib.pyplot as plt
from pdf2image import convert_from_path


class LatexString:
    def __init__(self, formula: str) -> None:
        self.__formula = formula
        self.__image = self.latex_to_image(self.__formula)

    @staticmethod
    def latex_to_image(text: str) -> str:
        figure = plt.figure()
        plt.axis("off")
        plt.text(0.5, 0.5, f'${text}$')

        pdf_output = os.path.join(os.getcwd(), "temp.pdf")
        plt.savefig(pdf_output, format="pdf", bbox_inches="tight", pad_inches=0.3)
        plt.close(figure)

        image_output = os.path.join(os.getcwd(), "result.png")
        image = convert_from_path(pdf_output)[0]
        image.save(image_output, "PNG")
        return image_output

    def display(self) -> None:
        try:
            image = cv2.imread(self.__image, cv2.IMREAD_UNCHANGED)
            cv2.imshow('Image', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except FileNotFoundError:
            print(f'No image found: {self.__image}')
