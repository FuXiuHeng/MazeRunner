import { Config } from 'src/config/maze_config';
import { GridCell, Map, Coord2D } from 'src/maps/map_types';

export class BoardPainter {
  constructor(
    private config: Config,
  ) {
  }

  drawGrid(ctx: CanvasRenderingContext2D, grid: GridCell[][]) {
    for (let row = 0; row < grid.length; row++) {
      for (let col = 0; col < grid[row].length; col++) {
        const cell = grid[row][col];
        this.drawCell(ctx, { row, col }, cell);
      }
    }
  }

  drawPlayer(ctx: CanvasRenderingContext2D, coord: Coord2D) {
    const { gridSize, playerColor } = this.config;
    const x = coord.col * gridSize;
    const y = coord.row * gridSize;
    ctx.fillStyle = playerColor;
    ctx.fillRect(x, y, gridSize, gridSize);
  }

  drawCell(
    ctx: CanvasRenderingContext2D,
    coord: Coord2D,
    cell: GridCell,
  ) {
    const {
      gridSize,
      baseColor,
      wallColor,
      startColor,
      endColor,
    } = this.config;
    const x = coord.col * gridSize;
    const y = coord.row * gridSize;
    switch(cell) {
      case 'S': ctx.fillStyle = startColor; break;
      case 'E': ctx.fillStyle = endColor; break;
      case 'W': ctx.fillStyle = wallColor; break;
      case ' ': ctx.fillStyle = baseColor; break;
      default: throw Error('Unreachabled error');
    }
    ctx.fillRect(x, y, gridSize, gridSize);
  }
}
