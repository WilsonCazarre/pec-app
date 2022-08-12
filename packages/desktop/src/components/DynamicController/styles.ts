import styled from "styled-components";

export const Container = styled.div`
  margin-top: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;

  & > * + * {
    margin-top: 0.5rem;
  }
`;

export const DynamicControllerButton = styled.button<{ isDisabled?: boolean }>`
  color: white;
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  opacity: ${({ isDisabled }) => (isDisabled ? "0.5" : "1")};

  & > * + * {
    margin-top: 0.5rem;
  }
`;
