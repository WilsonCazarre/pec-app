import React, { useState } from "react";
import { Container, SendButton } from "./StaticController.styles";
import { ColorResult, HuePicker, RGBColor } from "react-color";

const StaticController: React.FC = () => {
  const [color, setColor] = useState<RGBColor>({ r: 255, g: 0, b: 0 });
  const onColorChange = (color: ColorResult) => {
    setColor(color.rgb);
    console.log(color.rgb);
  };
  return (
    <Container>
      <div
        style={{
          width: "100px",
          height: "100px",
          color: "transparent",
          backgroundColor: `rgb(${color?.r}, ${color?.g}, ${color?.b})`,
        }}
      />
      <HuePicker color={color} onChange={onColorChange} />
      <SendButton
        onClick={() => {
          window.Main.staticSendColor(color);
        }}
      >
        Enviar para dispositivo
      </SendButton>
    </Container>
  );
};

export default StaticController;
