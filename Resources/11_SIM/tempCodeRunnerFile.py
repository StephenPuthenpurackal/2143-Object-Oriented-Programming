        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()