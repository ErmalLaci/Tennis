from models.grid import Grid

if __name__ == '__main__':
    # test code
    grid = Grid()

    grid_options = {}
    grid.generate(**grid_options)
    grid.visualise()
