import styled from "styled-components";

export const Container = styled.div`
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;

  & > * + * {
    margin-top: 0.5rem;
  }
`;

export const SendButton = styled.button`
  background-color: #334155;
  padding: 0.5rem;
  border-radius: 0.25rem;
`;
