import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Login from "./component/Login";
import Reg from "./component/Reg";
import Home from "./component/home";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route exact path='/Login' element={<Login/>}></Route>
          <Route exact path='/Reg' element={<Reg/>}></Route>
          <Route exact path='/Home' element={<Home/>}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
