import random

import Character


def begin_new_game():
    character_name = input('Name your character: ')
    new_player = Character.Character(character_name, 33, 7, 15)
    return new_player


def encounter():
    # TODO: Create enemy array

    enemy = Character.Monster('Goblin', random.randint(30, 40), 4, 12, 'Goblin')
    print('You\'ve encountered an enemy!')

    # TODO: roll for initiation
    player_roll = player.roll_dice(20)
    enemy_roll = enemy.roll_dice(20)

    participants = [player, enemy]

    if player_roll <= enemy_roll:
        participants.reverse()

    while enemy.hp >= 0 and player.hp >= 0:
        if attack(participants[0], participants[1]) == 'hit':
            if participants[1].hp <= 0:
                print(participants[1].name + ' is dead!')
                return False
            print(participants[1].name + ' has ' + str(enemy.hp) + ' hp left!')
            participants.reverse()
        else:
            participants.reverse()


def attack(attacker, atackee):
    attack_roll = attacker.attack()
    if attack_roll > atackee.armor:
        print(atackee.name + ' was hit!')
        atackee.takes_damage(attacker.deals_damage())
        return 'hit'
    else:
        print('Attack misses!')
        return 'miss'


player = begin_new_game()

print("You created character " + player.name)

encounter()
