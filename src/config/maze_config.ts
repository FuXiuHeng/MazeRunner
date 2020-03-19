export type Config = {
  gridSize: number,
  baseColor: string,
  wallColor: string,
  startColor: string,
  endColor: string,
  playerColor: string,
};

export const config: Config = {
  gridSize: 20, // pixels
  baseColor: '#ffffff',
  wallColor: '#000000',
  startColor: '#00ff00',
  endColor: '#bbbbbb',
  playerColor: '#ff0000',
};
