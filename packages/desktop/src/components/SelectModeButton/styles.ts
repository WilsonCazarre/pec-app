import styled from "styled-components";
import { COLORS } from "../../constants";

export const Container = styled.div<{ isDisabled?: boolean }>`
  display: flex;
  background-color: ${COLORS.gray};
  padding: 1rem;
  border-radius: 0.5rem;
  min-width: 100px;
  max-width: 200px;
  opacity: ${({ isDisabled }) => (isDisabled ? "0.5" : "1")};
`;
