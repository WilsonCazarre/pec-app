import styled from "styled-components";
import { Link } from "react-router-dom";

export const Container = styled.div`
  padding: 1rem;
`;

export const Title = styled.h2`
  text-align: center;
  font-weight: normal;
  font-size: 1.2rem;
`;

export const ButtonContainer = styled.div`
  display: flex;
  margin-top: 1.5rem;
  justify-content: center;

  & > * + * {
    margin-left: 1rem;
  }
`;

export const StyledLink = styled(Link)`
  color: white;
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: bold;
  width: 100%;

  & > * + * {
    margin-top: 0.5rem;
  }
`;
