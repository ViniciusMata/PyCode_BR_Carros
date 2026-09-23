from openai import OpenAI

client = OpenAI(
        api_key = 'KEY_API'
    )


def get_car_ai_bio(model, brand, year):
    message = ''''
        Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. 
        Fale coisas especificas desse modelo de carro.
        Descreva especificações ténicas sobre esse carro.
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens = 100,
        model = 'gpt-5-mini',
    )
    return response.choices[0].message.content