export class Hero {
  constructor(heroData) {
    Object.assign(this, {
      name: heroData.name,
      heroNumber: heroData.heroNumber,
      image: heroData.image,
      spriteSheet: heroData.spriteSheet,
      heroClass: heroData.heroClass,
      heroGroup: heroData.heroGroup,
      passive: heroData.passive,
      health: heroData.stats["Health"],
      fireAttack: heroData.stats["Fire Attack"],
      waterAttack: heroData.stats["Water Attack"],
      lightAttack: heroData.stats["Light Attack"],
      darkAttack: heroData.stats["Dark Attack"],
      fireDefense: heroData.stats["Fire Defense"],
      waterDefense: heroData.stats["Water Defense"],
      lightDefense: heroData.stats["Light Defense"],
      darkDefense: heroData.stats["Dark Defense"],
      attackSpeed: heroData.stats["Attack Speed"],
      attackBar: 0,
      level: heroData.level || 1,
      experience: heroData.experience || 0,
      requiredExperience: heroData.requiredExperience || 100,
      x: heroData.x || 0,
      y: heroData.y || 0,
      sprite: heroData.sprite || null
    });
  }

  // Modify serialize() to return a plain object
  serialize() {
    return {
      name: this.name,
      heroNumber: this.heroNumber,
      image: this.image,
      spriteSheet: this.spriteSheet,
      heroClass: this.heroClass,
      heroGroup: this.heroGroup,
      passive: this.passive,
      stats: {
        "Health": this.health,
        "Fire Attack": this.fireAttack,
        "Water Attack": this.waterAttack,
        "Light Attack": this.lightAttack,
        "Dark Attack": this.darkAttack,
        "Fire Defense": this.fireDefense,
        "Water Defense": this.waterDefense,
        "Light Defense": this.lightDefense,
        "Dark Defense": this.darkDefense,
        "Attack Speed": this.attackSpeed
      },
      level: this.level,
      experience: this.experience,
      requiredExperience: this.requiredExperience,
      x: this.x,
      y: this.y,
      sprite: this.sprite
    };
  }

  // Adjust deserialize() to work with objects
  static deserialize(data) {
    if (!data) return null;
    try {
      return new Hero({
        ...data,
        stats: {
          "Health": data.health,
          "Fire Attack": data.fireAttack,
          "Water Attack": data.waterAttack,
          "Light Attack": data.lightAttack,
          "Dark Attack": data.darkAttack,
          "Fire Defense": data.fireDefense,
          "Water Defense": data.waterDefense,
          "Light Defense": data.lightDefense,
          "Dark Defense": data.darkDefense,
          "Attack Speed": data.attackSpeed
        }
      });
    } catch (e) {
      console.error("Deserialization error: ", e);
      return null;
    }
  }
}
