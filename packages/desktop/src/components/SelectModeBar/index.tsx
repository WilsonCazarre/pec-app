import React from "react"
import { Container, Title, ButtonContainer } from "./styles"
import { SelectModeButton } from "../SelectModeButton"

export const SelectModeBar: React.FC = () => {
  return (
    <Container>
      <Title>Modos de Controle</Title>
      <ButtonContainer>
        {[1, 2, 3].map(i => (
          <SelectModeButton>{i}</SelectModeButton>
        ))}
      </ButtonContainer>
    </Container>
  )
}
