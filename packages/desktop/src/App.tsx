import { GlobalStyle } from "./styles/GlobalStyle"
import AppHeader from "./components/AppHeader"
import { SelectModeBar } from "./components/SelectModeBar"

export function App() {
  return (
    <>
      <GlobalStyle />
      <AppHeader />
      <SelectModeBar />
    </>
  )
}
