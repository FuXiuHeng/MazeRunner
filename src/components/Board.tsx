import classNames from 'classnames';
import * as mobxReact from 'mobx-react';
import * as React from "react";
import { BoardStore } from './board_store';
import { BoardPainter } from './board_painter';
import styles from './Board.css';
import { Coord2D } from "src/maps/map_types";

export type Props = {
  store: BoardStore,
  painter: BoardPainter,
};

@mobxReact.observer
export class Board extends React.Component<Props> {
  private boardRef: React.RefObject<HTMLCanvasElement> = React.createRef();
  private keyRef: React.RefObject<HTMLDivElement> = React.createRef();

  componentDidMount() {
    const { store, painter } = this.props;
    painter.drawGrid(this.ctx, store.grid);
    painter.drawPlayer(this.ctx, store.playerCoord);
    this.keyRef.current.focus();
  }

  get ctx(): CanvasRenderingContext2D {
    return this.boardRef.current.getContext('2d');
  }

  handleKeys = (e: React.KeyboardEvent<HTMLDivElement>) => {
    const { store, painter } = this.props;
    const { playerCoord } = store;
    let dst: Coord2D | undefined;
    if (dst = store.validMove(e.key)) {
      painter.drawCell(this.ctx, playerCoord, store.getCell(playerCoord));
      store.movePlayer(dst);
      painter.drawPlayer(this.ctx, playerCoord);
    }
  }

  render() {
    const { boardRef } = this;
    const { store } = this.props;
    
    return (
      <div>
        <div className={classNames(styles.winBanner,{[styles.hidden]: !store.gameWon})}>
          You Win!
        </div>
        <div onKeyDown={this.handleKeys} ref={this.keyRef} tabIndex={0}>
          <canvas
              className={styles.board}
              width={store.boardWidth}
              height={store.boardHeight}
              ref={boardRef}
          />
        </div>
      </div>
    );
  }
}