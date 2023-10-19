import init_django_orm  # noqa: F401
import json
import pytest

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as config:
        player_data = json.load(config)

    for player, data in player_data.items():

        race, created = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )

        for skill in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = data["guild"]
        if guild:
            guild, created = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            )

        Player.objects.get_or_create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()

# print(Race.objects.all())
# print(Skill.objects.all())
# print(Guild.objects.all())
# print(Player.objects.all())
