import React from "react";
import { Container } from "./styles";

interface Props {
  children: React.ReactNode;
  isDisabled?: boolean;
}

export const SelectModeButton: React.FC<Props> = ({ children, isDisabled }) => {
  return <Container isDisabled={isDisabled}>{children}</Container>;
};
