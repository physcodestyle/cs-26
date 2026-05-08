from controllers.navigation_controller import NavigationController, NavigationCode


def run():
    navigator = NavigationController(data=None, state=-1, default_controller=NavigationCode.DEFAULT_CONTROLLER)
    while navigator.next() >= 0:
        print("=======")
    


if __name__ == '__main__':
    run()