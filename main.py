from random import randint


def attack(char_name, char_class):
    if char_class == 'guerreiro':
        return (f'{char_name} causou {5 + randint(3, 5)} de dano ao inimigo')
    if char_class == 'mago':
        return (f'{char_name} causou {5 + randint(5, 10)} de dano ao inimigo')
    if char_class == 'curandeiro':
        return (f'{char_name} causou {5 + randint(-3, -1)} de dano ao inimigo')
def defense(char_name, char_class):
    if char_class == 'guerreiro':
        return (f'{char_name} bloqueou {10 + randint(5, 10)} de dano')
    if char_class == 'mago':
        return (f'{char_name} bloqueou {10 + randint(-2, 2)} de dano')
    if char_class == 'curandeiro':
        return (f'{char_name} bloqueou {10 + randint(2, 5)} de dano')
def special(char_name, char_class):
    if char_class == 'guerreiro': 
        return (f'{char_name} usou uma habilidade especial "Resistência {80 + 25}"')
    if char_class == 'mago':
        return (f'{char_name} usou uma habilidade especial "Ataque {5 + 40}"')
    if char_class == 'curandeiro':
        return (f'{char_name} usou uma habilidade especial "Defesa {10 + 30}"')




def start_training(char_name, char_class):
    if char_class == 'guerreiro':
        print(f'{char_name}, você é um Guerreiro proficiente em combate corpo-a-corpo.')
    if char_class == 'mago':
        print(f'{char_name}, você é um Mago - um mestre no domínio dos elementos.')
    if char_class == 'curandeiro':
        print(f'{char_name}, você é um Curandeiro, um feiticeiro que cura feridas.')
    print('Treine suas habilidades.')
    print('Insira um dos seguintes comandos: ataque — para atacar um inimigo, defesa — para bloquear um ataque do inimigo, ou especial — para usar seu poder especial.')
    print('Se você não quer treinar, insira pular.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Insira um comando: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defense':
            print(defense(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'O treinamento foi concluído.'

def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Insira a classe do seu personagem: Guerreiro — guerreiro, Mago — mago, Curandeiro — curandeiro: ')
        if char_class == 'warrior':
            print('Guerreiro — um lutador feroz de combate corpo-a-corpo. Forte, resistente e corajoso.')
        if char_class == 'magician':
            print('Mago — um brilhante lutador de longo alcance. Mestre dos poderes mágicos.')
        if char_class == 'healer':
            print('Curandeiro — um poderoso xamã. Adquire forças da natureza, fé e espíritos.')
        approve_choice = input('Pressione (Y) para confirmar sua escolha ou qualquer outro botão para selecionar outra classe').lower()
    return char_class


def main():
    print('Olá, aventureiro!')
    print('Antes de começar a jogar...')
    char_name = input('... diga o seu nome: ')
    print(f'Bem-vindo, {char_name}! '
          'Você tem 80 pontos de resistência, 5 pontos de ataque e 10 pontos de defesa.')
    print(('Você pode escolher uma das três formas da Força:')
    print('Guerreiro, Mago, Curandeiro')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))
    

main()
