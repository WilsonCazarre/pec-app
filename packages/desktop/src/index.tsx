import ReactDOM from "react-dom";
import { App } from "./App";
import { HashRouter } from "react-router-dom";
import "./styles/normalize.css";

ReactDOM.render(
  <HashRouter>
    <App />
  </HashRouter>,
  document.getElementById("root")
);
