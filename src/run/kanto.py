from src.region.kanto import rock_tunnel, route_2


def run(area: str):
    if area == "rock_tunnel":
        rock_tunnel.run()
    if area == "route_2":
        route_2.run()
