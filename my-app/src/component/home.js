import { useState } from "react";
import Button from "react-bootstrap/esm/Button";
import { selectList } from "./selectList";
import "./style.css";


export default function Home() {

  const [checkedState, setCheckedState] = useState(new Array(6).fill(false));
  var [movieName, setMovieName] = useState("");
  var [movieYear, setMovieYear] = useState(""); 
  var [director, setDirector] = useState(""); 
  var [writer, serWriter] = useState(""); 
  var [rating, setRating] = useState(""); 
  var [genres, setGenres] = useState("");
  var [error,setError] = useState('');
  const [returnVal, setReturnVal] = useState(new Array());

  const handleOnChange = (position) => {
    const updatedCheckedState = checkedState.map((item, index) =>
      index === position ? !item : item
    );
    setCheckedState(updatedCheckedState);
  };

  function handleSubmit(event) {
    event.preventDefault();
    const postBody = {method: 'Post', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({
      "movieName": ( checkedState[0]=== true ? movieName : null),
      "movieYear":checkedState[1] == true ? movieYear : null ,
      "director": checkedState[4] == true ? director : null,
      "writer":checkedState[5] == true ? writer : null,
      "rating":checkedState[2] == true ? rating : null,
      "genres":checkedState[3] == true ? genres : null
    })};
    console.log(postBody);
    fetch('http://localhost:8999/select', postBody)
    .then(response => response.json()
    .then(data => {
        console.log(data)
        setReturnVal(data)
        })
    )
}
// function onchange1(event) {
//   setMovieName(event.target.value)
//   console.log(movieName)
// }

  return (
    <div className="home">
      <h3>Select item</h3>
      <ul className="select-list">
        {selectList.map (({ name, price }, index) => {
          return (
            <li key={index}>
              <div className="select-list-item">
                <div className="left-section">
                  <input
                    type="checkbox"
                    id={`custom-checkbox-${index}`}
                    name={name}
                    value={name}
                    checked={checkedState[index]}
                    onChange={() => handleOnChange(index)}
                  />
                  <label htmlFor={`custom-checkbox-${index}`}>{name}</label>
                </div>
              </div>
            </li>
          );
        })}
      </ul>
      <div className="put">
        <div>
          <input className="e-input"  onChange ={(e) => setMovieName(e.target.value)} type="text" placeholder="moviename" disabled={checkedState[0]== false}/>
        </div>
        <input className="e-input1" onChange ={(e) => setMovieYear(e.target.value)} type="text" placeholder="range" disabled={checkedState[1]== false}/>
        <div>
        <input className="e-input3" onChange ={(e) => setRating(e.target.value)} type="text" placeholder="rating" disabled={checkedState[2]== false}/>
        </div>
        <div>
        <input className="e-input4" onChange ={(e) => setGenres(e.target.value)} type="text" placeholder="genre" disabled={checkedState[3]== false}/>
        </div>
        
      </div>
      <div className="button">
      <button onClick={handleSubmit}> Check </button>
      </div>
      {returnVal.map(function(item, i){
        return <h3 className="error"> {item} </h3> 
        // {<h3 className="error"> {i} </h3> }
      })}
      
    </div>
  );
}