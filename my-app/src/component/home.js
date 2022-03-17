import { useState } from "react";
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

  const handleOnChange = (position) => {
    const updatedCheckedState = checkedState.map((item, index) =>
      index === position ? !item : item
    );

    setCheckedState(updatedCheckedState);
  };

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
    </div>
  );
}