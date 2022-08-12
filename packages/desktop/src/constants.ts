import Home from "./routes/Home";
import DynamicMode from "./routes/DynamicMode";
import { ChartBarIcon, SunIcon } from "@heroicons/react/outline";

export const COLORS = {
  gray: "#334155",
  darkBlue: "#0F172A",
};

export const ROUTES = [
  {
    label: "Estático",
    pathname: "/",
    icon: SunIcon,
    component: Home,
  },
  {
    label: "Dinâmico",
    pathname: "/dynamic",
    icon: ChartBarIcon,
    component: DynamicMode,
  },
  // {
  //   label: "Temporizado",
  //   pathname: "/timed",
  //   icon: ClockIcon,
  //   component: TimedMode,
  // },
];
