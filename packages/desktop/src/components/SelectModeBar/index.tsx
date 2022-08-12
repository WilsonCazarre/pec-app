import React, { useEffect } from "react";
import { Container, Title, ButtonContainer, StyledLink } from "./styles";
import { SelectModeButton } from "../SelectModeButton";
import { ROUTES } from "../../constants";
import { useLocation } from "react-router-dom";

export const SelectModeBar: React.FC = () => {
  const location = useLocation();

  useEffect(() => {
    console.log({ location });
  }, [location]);
  return (
    <Container>
      <Title>Modos de Controle</Title>
      <ButtonContainer>
        {ROUTES.map(routeInfo => (
          <SelectModeButton
            key={routeInfo.pathname}
            isDisabled={location.pathname !== routeInfo.pathname}
          >
            <StyledLink to={routeInfo.pathname}>
              <div>
                <routeInfo.icon width={32} height={32} />
              </div>
              <div>{routeInfo.label}</div>
            </StyledLink>
          </SelectModeButton>
        ))}
      </ButtonContainer>
    </Container>
  );
};
