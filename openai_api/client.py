import openai


def get_car_ai_bio(model, brand, year):
    prompt = ''''
        Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. 
        Fale coisas especificas desse modelo de carro.
        Descreva especificações ténicas sobre esse carro.
    '''
    openai.api_key = ''
    prompt = prompt.format(brand, model, year)
    response = openai.Completion.create(
        model = 'gpt-5.6-luna',
        prompty = prompt,
        max_tokens = 100,
    )
    return response['choices'][0]['text']