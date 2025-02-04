# passives.py

def ethan_use_passive(hero):
    hero.fireAttack *= 1.23

EthanPassive = {
    "name": "Fire Mastery",
    "description": "Increases fire attack by 23%.",
    "usePassive": ethan_use_passive
}

def drew_use_passive(hero):
    hero.lightDefense *= 1.3

DrewPassive = {
    "name": "Light Guard",
    "description": "Increases light defense by 30%.",
    "usePassive": drew_use_passive
}

def jonathan_use_passive(hero):
    heal_amount = hero.health * 0.1
    # Ensure currentHealth does not exceed max health.
    hero.currentHealth = min(hero.health, hero.currentHealth + heal_amount)

JonathanPassive = {
    "name": "Water Healer",
    "description": "Heals the hero by 10% of max health after each attack.",
    "usePassive": jonathan_use_passive
}

def nicholas_use_passive(hero):
    hero.fireDefense *= 1.15
    hero.waterDefense *= 1.15
    hero.lightDefense *= 1.15
    hero.darkDefense *= 1.15

NicholasPassive = {
    "name": "Shield Master",
    "description": "Increases all defense stats by 15%.",
    "usePassive": nicholas_use_passive
}

def conor_use_passive(hero):
    hero.craftingSpeed *= 1.2
    hero.gatheringSpeed *= 1.2

ConorPassive = {
    "name": "Swift Attack",
    "description": "Increases attack speed by 20%.",
    "usePassive": conor_use_passive
}

def mara_use_passive(hero):
    hero.darkAttack *= 1.25

MaraPassive = {
    "name": "Dark Sorcery",
    "description": "Increases dark attack by 25%.",
    "usePassive": mara_use_passive
}

def sav_use_passive(hero):
    hero.craftingSpeed *= 1.3

SavPassive = {
    "name": "Crafting Genius",
    "description": "Increases crafting speed by 30%.",
    "usePassive": sav_use_passive
}

def laine_use_passive(hero):
    hero.gatheringSpeed *= 1.25

LainePassive = {
    "name": "Resilient Gatherer",
    "description": "Increases gathering speed by 25%.",
    "usePassive": laine_use_passive
}

def tom_use_passive(hero):
    hero.health *= 1.1
    print(f"Increased {hero.name}'s health to {hero.health}")

TomPassive = {
    "name": "Party Leader",
    "description": "Increases all party members' health by 10%.",
    "usePassive": tom_use_passive
}

def crisluigy_use_passive(hero):
    hero.fireAttack *= 1.2
    hero.waterAttack *= 1.2
    hero.lightAttack *= 1.2
    hero.darkAttack *= 1.2

CrisluigyPassive = {
    "name": "Elemental Master",
    "description": "Increases all elemental attacks by 20%.",
    "usePassive": crisluigy_use_passive
}

def nik_use_passive(hero):
    hero.fireDefense *= 1.1
    hero.waterDefense *= 1.1
    hero.lightDefense *= 1.1
    hero.darkDefense *= 1.1
    hero.health *= 1.05

NikPassive = {
    "name": "Balanced Defender",
    "description": "Increases defense stats by 10% and increases health by 5%.",
    "usePassive": nik_use_passive
}
