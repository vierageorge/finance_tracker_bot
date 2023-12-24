from utils.persist import get_categories
from openai import OpenAI

categories = get_categories()

client = OpenAI()

content = """Serás un sistema de clasificación de gastos. Recibirás como entrada, una descripción del gasto realizado
y retornarás una y solo una de las siguientes categorías que listaré a continuación. En la respuesta, lo único que colocarás
será la categoría, la cual siempre tendrá el formato TEXTO1|texto2. Sin importar qué, no usarás una categoría que no esté listada
a continuación. A continuación, las categorías, las cuales son un arreglo separado por punto y coma (;):"""

contexts = [
  "Mayra es quien hace el aseo en la casa"
]

def get_category(entry: str) -> str:
  try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{content} {';'.join(categories)}. Tener en cuenta los siguientes contextos: {'. '.join(contexts)} ENTRADA: {entry}",
            }
        ],
        model="gpt-3.5-turbo",
    )
    openai_response = chat_completion.choices[0].message.content
  except Exception as e:
    print(e)
    openai_response = ""
  return openai_response if openai_response in categories else None