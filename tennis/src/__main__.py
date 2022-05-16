from models.grid import Grid

if __name__ == '__main__':
    # Test code
    grid = Grid()

    # TODO: Configure options here for now - will make a CLI at some point.
    grid_options = {
        'void_probability': 0.5,
    }
    grid.generate(**grid_options)
    grid.visualise()
