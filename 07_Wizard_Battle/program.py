import random
import time

from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('------------------------------')
    print('------------------------------')
    print('--------Wizard-Battle---------')
    print('------------------------------')
    print('------------------------------')


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000),
    ]
    # print(creatures)

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest....'
              .format(active_creature.name, active_creature.level))

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("Wizard runs and hides taking time to recover....")
                time.sleep(5)
                print("Wizard has rested")
        elif cmd == 'r':
            print('The Wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print('Wizard {} takes in the surroundings and sees:'
                  .format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print("OK, exiting game ... bye")
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()


if __name__ == '__main__':
    main()
