import pygame
import sys, time
import snake
import ThingyYouEat


def drawGame(player, pellet, window):
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (18, 173, 42), pygame.Rect((player.HeadX*32), (player.Heady*32), 32, 32))
    for i in range(len(player.BodyParts)):
        pygame.draw.rect(window, (18, 173, 42), pygame.Rect((player.BodyParts[i].x*32), ((player.BodyParts[i].y*32)), 32, 32))
    pygame.draw.rect(window, (255, 62, 51), pygame.Rect((pellet.x*32), (pellet.y*32), 32, 32))
    

def main():
    
    pygame.init()
    pygame.font.init()
    WIN = pygame.display.set_mode([800, 800])
    WIN.fill((0, 0, 0))
    pygame.display.set_caption("Snake")
 
    bigTitle = pygame.font.SysFont('Times', 70, bold=True, italic=False)


    i = 0
    Playing = True
    clock = pygame.time.Clock()
    player = snake.Snake()
    pellet = ThingyYouEat.ThingyYouEat(player)

    while Playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Playing = False
            elif event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if(pressed[pygame.K_UP] and player.Direction != 1):
                    player.Direction = 1
                    if(player.Length > 0):
                        player.ListofDirectionChanges.append((player.HeadX, player.Heady, player.Direction))
                elif(pressed[pygame.K_RIGHT] and player.Direction != 2):
                    player.Direction = 2
                    if(player.Length > 0):
                        player.ListofDirectionChanges.append((player.HeadX, player.Heady, player.Direction))
                elif(pressed[pygame.K_DOWN] and player.Direction != 3):
                    player.Direction = 3
                    if(player.Length > 0):
                        player.ListofDirectionChanges.append((player.HeadX, player.Heady, player.Direction))
                elif(pressed[pygame.K_LEFT] and player.Direction != 4):
                    player.Direction = 4
                    if(player.Length > 0):
                        player.ListofDirectionChanges.append((player.HeadX, player.Heady, player.Direction))

        clock.tick(30)
        if(player.Death()):
            Playing = False
            gameovermsg = bigTitle.render("GAME OVER", False, (255, 0, 0))
            WIN.blit(gameovermsg,(150, 350))
            pygame.display.update()
            time.sleep(3.0)
            pygame.quit()
            sys.exit()
        
        if(player.HeadX == pellet.x and player.Heady == pellet.y):
            player.grow()
            pellet = ThingyYouEat.ThingyYouEat(player)

        if(i == 10):
            player.move()
            i = 0
        i += 1
        drawGame(player, pellet, WIN)
        pygame.display.update()
        

    pygame.quit()
if __name__ == "__main__":
    main()