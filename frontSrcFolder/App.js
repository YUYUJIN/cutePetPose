import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Main from './Main';
import Test from './Analyze';
import Album from './Album';
import Analyze from './Analyze';
import 'C:/Users/tmdqj/Desktop/pet_project/pet/src/font/font.css';
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Main/>} />
        <Route exact path="/analyze" element={<Analyze/>} />
        <Route exact path="/album" element={<Album/>} />
      </Routes>
    </BrowserRouter> 
  );
}

export default App;
