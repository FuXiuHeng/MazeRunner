export type Coord2D = {
  row: number,
  col: number,
};

export type GridCell =
  | 'S' // Start
  | 'E' // End
  | 'W' // Wall
  | ' ' // None

export type Map = {
  width: number,
  height: number,
  grid: GridCell[][],
};
