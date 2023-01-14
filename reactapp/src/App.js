import './style/main.css';
import HomeComponent from './components/home'
import LoginComponent from './components/login'
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginComponent />} />
        <Route path="/" element={<HomeComponent />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
