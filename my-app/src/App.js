import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Login from "./component/Login";
import Reg from "./component/Reg";
import Home from "./component/home";
import Update from "./component/update";
import Delete from "./component/delete";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route exact path='/Login' element={<Login/>}></Route>
          <Route exact path='/Reg' element={<Reg/>}></Route>
          <Route exact path='/Home' element={<Home/>}></Route>
          <Route exact path='/Update' element={<Update/>}></Route>
          <Route exact path='/Delete' element={<Delete/>}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
