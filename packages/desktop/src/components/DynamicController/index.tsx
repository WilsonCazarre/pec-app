import React, { useState } from "react";
import {
  MicrophoneIcon,
  TrendingDownIcon,
  TrendingUpIcon,
} from "@heroicons/react/outline";
import { Container, DynamicControllerButton } from "./styles";
import { SelectModeButton } from "../SelectModeButton";

const Index: React.FC = () => {
  const [activeMode, setActiveMode] = useState<string>();
  const dynamicPresets = {
    low: {
      icon: TrendingDownIcon,
      args: {
        points: [
          { x: 0, y: 1 },
          { x: 1, y: 0 },
        ],
        color: { r: 0, g: 255, b: 0 },
      },
      label: "Reforço de Graves",
    },
    high: {
      icon: TrendingUpIcon,
      args: {
        points: [
          { x: 0, y: 0 },
          { x: 1, y: 1 },
        ],
        color: { r: 0, g: 0, b: 255 },
      },
      label: "Reforço de Agudos",
    },
    vocals: {
      icon: MicrophoneIcon,
      args: {
        points: [
          { x: 0, y: 0 },
          { x: 0.5, y: 1 },
          { x: 1, y: 0 },
        ],
        color: { r: 0, g: 120, b: 120 },
      },
      label: "Reforço de Vocais",
    },
  };

  return (
    <Container>
      {Object.keys(dynamicPresets).map(presetKey => {
        const preset = dynamicPresets[presetKey as keyof typeof dynamicPresets];
        return (
          <SelectModeButton>
            <DynamicControllerButton
              key={preset.label}
              isDisabled={activeMode !== preset.label}
              onClick={() => {
                window.Main.sendDynamicInterpolate(
                  preset.args.points,
                  preset.args.color
                );
                setActiveMode(preset.label);
              }}
            >
              <span>{<preset.icon width={50} height={50} />}</span>
              <span>{preset.label}</span>
            </DynamicControllerButton>
          </SelectModeButton>
        );
      })}
      {!activeMode && <span>Selecione um modo para começar</span>}
    </Container>
  );
};

export default Index;
