import Navbar from './components/Navbar';
import { useEffect } from "react";
import { getTftData } from "./services/api";

export default function App() {
  useEffect(() => {
    getTftData().then(res => console.log(res.data));
  }, []);

  return <h1>Check console for TFT data</h1>;
}
