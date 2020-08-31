import pygame

# TODO Use indexes instead of positions, easier for maintaning and cleaner


class Blocks:
    def __init__(self, index, posx, posy):
        self.index = index
        self.posx, self.posy = posx, posy
        self.rect = pygame.Rect(posx, posy, 62, 62)
        self.available = True

    def __int__(self):
        return int(self.index)

    def draw(self):
        pygame.draw.rect(screen, Green, self.rect, 1)


class King:
    def __init__(self, index, img):
        self.index = index
        self.posx, self.posy = 50, 50   # 248
        self.set_pos()
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.posx, self.posy)
        self.selected = False
        self.available_moves = []       # TODO clean up the availables, too many obsolete variables
        self.available_blocks = []
        self.set_available_moves()      # only for testing, fix after

    # Not needed anymore, delete when done
    def set_index(self):
        for blok in blocks:
            if blok.rect.colliderect(self.rect):
                return int(blok)

    def set_pos(self):
        for blok in blocks:
            if blok.index == self.index:
                self.posx, self.posy = blok.posx, blok.posy
                break

    # TODO Cleaning here
    def set_available_moves(self):
        self.available_moves.extend((self.index+1, self.index-1, self.index+8, self.index-8))
        for blok in blocks:
            for x in self.available_moves:
                if blok.index == x:
                    self.available_blocks.append([blok.posx, blok.posy])

    def is_selected(self, ev):
        if self.rect.collidepoint(ev.pos):
            self.selected = not self.selected
        print(f"king active: {self.selected}")

    def move(self, ev):
        if self.selected:
            for blok in self.available_blocks:     # TODO Wont work untill i fix the setter for av_b
                if ev.pos == blok:
                    print("WORKS")

    def draw(self):
        screen.blit(self.img, self.rect)
        pygame.draw.rect(screen, Red, self.rect, 1)


Black = (0, 0, 0)
Gray = (50, 50, 50)
Green = (0, 255, 0)
Red = (255, 0, 0)
screenWidth, screenHeight = 600, 600
pygame.init()
pygame.display.set_caption("Chess")
screen = pygame.display.set_mode((screenWidth, screenHeight))

blocks = []
bpx, bpy = 50, 50
bxcount = 0
for n1 in range(1, 9):
    for n2 in range(0, 8):
        blocks.append(Blocks((n1 + bxcount), bpx, bpy))
        bpx += 62.5
        bxcount += 1   # It can't be n2 because the value resets every n1 loop
    bpx = 50
    bpy += 62.5


imgBoard = pygame.image.load("assets/board_big.png")
imgBlackKing = pygame.image.load("assets/black_king.png")

# black_king = King(imgBlackKing, 248, 50)
black_king = King(4, imgBlackKing)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            black_king.is_selected(event)
            black_king.move(event)

    screen.fill(Gray)
    screen.blit(imgBoard, (50, 50))
    black_king.draw()
    for block in blocks:
        block.draw()
    pygame.display.flip()
