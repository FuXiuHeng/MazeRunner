import * as mobx from 'mobx';
import { Config } from 'src/config/maze_config';
import { GridCell, Map, Coord2D } from 'src/maps/map_types';

export class BoardStore {
  boardWidth: number;
  boardHeight: number;
  grid: GridCell[][];
  numRows: number;
  numCols: number;
  @mobx.observable
  playerCoord: Coord2D;

  constructor(config: Config, map: Map) {
    this.boardWidth = map.width * config.gridSize;
    this.boardHeight = map.height * config.gridSize;
    this.grid = map.grid;
    this.numRows = map.grid.length;
    this.numCols = map.grid[0].length;
    for (let row = 0; row < this.grid.length; row++) {
      for (let col = 0; col < this.grid.length; col++) {
        if (this.grid[row][col] === 'S') {
          this.playerCoord = { row, col };
          return;
        }
      }
    }
  }

  @mobx.computed
  get gameWon(): boolean {
    const { grid, playerCoord } = this;
    const { row, col } = playerCoord;
    return grid[row][col] === 'E';
  }

  getCell = (coord: Coord2D): GridCell => {
    return this.grid[coord.row][coord.col];
  }

  validMove = (key: string): Coord2D | undefined => {
    let dst: Coord2D;
    const { playerCoord } = this;
    switch(key) {
      case 'ArrowUp':
        dst = { row: playerCoord.row - 1, col: playerCoord.col };
        break;
      case 'ArrowDown':
        dst = {  row: playerCoord.row + 1, col: playerCoord.col };
        break;
      case 'ArrowLeft':
        dst = { row: playerCoord.row, col: playerCoord.col - 1 };
        break;
      case 'ArrowRight':
        dst = { row: playerCoord.row, col: playerCoord.col + 1 };
        break;
      default:
        // Not an arrow key
        return;
    }

    const { row, col } = dst;
    if ( col < 0 || col >= this.numCols 
      || row < 0 || row >= this.numRows
      || this.grid[row][col] === 'W'
    ) {
      return undefined;
    }

    return dst;
  }

  movePlayer = (dst: Coord2D): void => {
    this.playerCoord.row = dst.row;
    this.playerCoord.col = dst.col;
  }
}
