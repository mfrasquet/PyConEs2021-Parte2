import streamlit as st
from page_sidebar import sidebar

def main():

    pages_mapper = {
                        '1. Portada': front,
                        '2. ¿Qué vamos a hacer?': task,
                        '3. Descargar un modelo': download_model,
                        '4. Contexto': context,
                        '5. Preguntas': questions,
                        '6. Resultados': results,
                        '7. Chuleta': cheatsheet,
                        '8. Os toca': your_turn
                    }

    ls_page_name = pages_mapper.keys()
    page_name = sidebar(ls_page_name)

    pages_mapper[page_name]()


if __name__ == '__main__':
    main()