import * as React from "react";
import { Board } from './components/board';
import { BoardStore } from './components/board_store';
import { BoardPainter } from './components/board_painter';
import { config } from './config/maze_config';
import { map } from './maps/generated_map';

import styles from './App.css';

export const App = () => {
  const boardStore = React.useMemo(() => new BoardStore(config, map), []);
  const boardPainter = React.useMemo(() => new BoardPainter(config), []);
  return (
    <div className={styles.root}>
      <Board store={boardStore} painter={boardPainter}/>
    </div>
  );
}
