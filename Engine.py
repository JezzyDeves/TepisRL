#Import functions
import tcod as libtcod
from input_handlers import handle_keys
from entity import Entity
from render_functions import clear_all, render_all
#Main engine function
def main():
    screen_width = 80
    screen_height = 50
#Player and NPC settings. Defines entities
    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow)
    entities = [npc, player]
#Sets font img
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
#Init for root console(Width, Height, Window name, fullscreen)
    libtcod.console_init_root(screen_width, screen_height, 'TepisRL', False)
#Consoles
    con = libtcod.console_new(screen_width, screen_height)
#Calls key functions
    key = libtcod.Key()
    mouse = libtcod.Mouse()
    #Game loop
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, screen_width, screen_height)

        libtcod.console_flush()

        clear_all(con, entities)
        #Handles recognition of keypresses for movement
        action = handle_keys(key)
        
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()