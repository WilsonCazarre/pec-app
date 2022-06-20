import styled from "styled-components"

export const Container = styled.div`
  padding: 1rem;
`

export const Title = styled.h2`
  text-align: left;
  font-weight: normal;
  font-size: 1.2rem;
`

export const ButtonContainer = styled.div`
  display: flex;
  margin-top: 1.5rem;

  & > * + * {
    margin-left: 1rem;
  }
`
