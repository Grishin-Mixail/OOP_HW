
import pygame

from settings import Settings	
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStat
from button import Button
from scoreboard import Scoreboard


def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_heigth))
	pygame.display.set_caption('Alien Invasion')
		# Создание корабля.
	ship = Ship(ai_settings, screen)
	#здание группы для хранения пуль  и пришельцев.
	bullets = Group()
	aliens = Group()
	# Создание флота пришельцев.
	gf.create_fleet(ai_settings, screen, ship, aliens)
	# Создание кнопки Play.
	play_button = Button(ai_settings, screen, "PLAY")
	# Создание экземпляров GameStats и Scoreboard.
	stats = GameStat(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
		
	# Запуск основного цикла игры.
	while True:
		# Отслеживание событий клавиатуры и мыши.
		gf.check_events(ai_settings, screen, stats, play_button, ship,
			 aliens, bullets)
		if stats.game_active:
			ship.update()
			bullets.update()
			# Удаление пуль, вышедших за край экрана.
			gf.update_bullets(ai_settings, screen, ship, stats, sb,
				 aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
#			print(len(bullets))
			gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
				bullets, play_button)
		
run_game()

 
