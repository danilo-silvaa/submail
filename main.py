import sys

if len(sys.argv) > 1:
    domain = sys.argv[1]
else:
    print('Digite um domínio valido! \n\nExemplo de uso: python main.py exemplo.com.br')
    sys.exit(1)

def generate_subemails(domain):
    prefixes = [
        'curriculosrh',
        'curriculos',
        'curriculo',
        'rh',
        'vagas',
        'recursoshumanos',
        'talentos',
        'oportunidade',
        'trabalheconosco',
        'recrutamento',
        'selecao',
        'comercial',
        'contato'
    ]

    return [f'{prefix}@{domain}' for prefix in prefixes]

print(f'Sub Emails gerados:\n\n{', '.join(generate_subemails(domain))}')