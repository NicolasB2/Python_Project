from . import setup
from . import tools
from . import constants as c


def main():
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {}
    run_it.setup_states(state_dict, c.MAIN_MENU)
    run_it.main()



