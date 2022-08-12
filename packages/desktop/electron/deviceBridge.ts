import { PythonShell } from "python-shell";

export const device = new PythonShell(
  "C:\\Users\\wilso\\projects\\unifesp\\pec-app\\packages\\device\\parser.py"
);

device.on("message", message => {
  console.log("Message from device:", message);
});
export function jsonToPythonArgs<T extends {}>(args: T) {
  console.log({ args });
  return Object.keys(args)
    .map(
      argName =>
        `${argName}=${JSON.stringify(args[argName as keyof typeof args])}`
    )
    .join(", ")
    .replace(/\\/g, '');
}
