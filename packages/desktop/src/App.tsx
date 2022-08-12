import { GlobalStyle } from "./styles/GlobalStyle";
import AppHeader from "./components/AppHeader";
import { SelectModeBar } from "./components/SelectModeBar";
import { ROUTES } from "./constants";
import { Route, Routes } from "react-router-dom";

export function App() {
  return (
    <>
      <GlobalStyle />
      <AppHeader />
      <SelectModeBar />
      <Routes>
        {ROUTES.map(routeInfo => (
          <Route
            path={routeInfo.pathname}
            key={routeInfo.pathname}
            element={<routeInfo.component />}
          />
        ))}
      </Routes>
    </>
  );
}
