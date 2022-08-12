import { contextBridge, ipcRenderer } from "electron";
import { device, jsonToPythonArgs } from "./deviceBridge";

export const api = {
  /**
   * Here you can expose functions to the renderer process
   * so they can interact with the main (electron) side
   * without security problems.
   *
   * The function below can accessed using `window.Main.sendMessage`
   */

  sendMessage: (message: string) => {
    ipcRenderer.send("message", message);
  },

  /**
   * Provide an easier way to listen to events
   */
  on: (channel: string, callback: Function) => {
    ipcRenderer.on(channel, (_, data) => callback(data));
  },

  /**
   * Send static color
   */
  staticSendColor: (color: { r: number; g: number; b: number }) => {
    const parsedColor = jsonToPythonArgs({
      R: color.r,
      G: color.g,
      B: color.b,
    });
    console.log({ parsedColor });
    device.send(`static_send_color(${parsedColor})`);
  },

  sendDynamicInterpolate: (
    points: { x: number; y: number }[],
    color: { r: number; g: number; b: number }
  ) => {
    console.log({ points, color });
    const arg = `dinamic_interpolate(${[
      points.map(p => `{'x': ${p.x}, 'y': ${p.y}},`),
    ]}, ${[color.r, color.g, color.b]}, 2, 1)`;
    console.log({ arg });
    device.send(
      `dinamic_interpolate([${[
        points.map(p => `{'x': ${p.x}, 'y': ${p.y}}`),
      ]}], [${[color.r, color.g, color.b]}], 2, 1)`
    );
  },
};

contextBridge.exposeInMainWorld("Main", api);
