
import recursiveReadDir from 'fs-readdir-recursive';
import * as fs from 'fs-extra';
import * as path from 'path';

export class AssetLoader {

  private enemies: any[] = [];
  private items: any[] = [];

  public get enemyNames(): string[] {
    return [...new Set(this.enemies.map(x => x.Name_29_7A62483740A6D0DF1414CB9963F7CF87))];
  }

  public get itemNames(): string[] {
    return [...new Set(this.items.map(x => x.Name))].map(x => x.split('::')[1]);
  }

  constructor() {
    this.init();
  }

  private init(): void {
    this.enemies = recursiveReadDir(
        path.resolve(path.join(__dirname, '..', '..', 'gamefiles'))
      )
      .filter(f => f.includes('.json') && !f.includes('ItemDataBase'))
      .map(f => `${__dirname}/../../gamefiles/${f}`)
      .map(f => require(f))
      .flat()
      .map(f => f.Value);

    this.items = require(`${__dirname}/../../gamefiles/items/ItemDataBase.json`)
      .map((f: any) => ({ Name: f.Key, ...f.Value.ItemData_3_CF780DE6460B8A55C91157B702A6BFA1 }));
  }

  public flush(): void {
    fs.outputJsonSync(`build/data/enemynames.json`, this.enemyNames, { spaces: 4 });
    fs.outputJsonSync(`build/data/itemnames.json`, this.itemNames, { spaces: 4 });
  }

}