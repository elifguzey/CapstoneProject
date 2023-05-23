import {useState, useEffect} from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route, useNavigate } from "react-router-dom";
import Navbar from './Navbar';
import Home from './Home';
import MyRecipes from './MyRecipes';
// // import RecipeCard from './RecipeCard';
import RecipeList from './RecipeList';
import Profile from './Profile';
import Login from './Login';
import Signup from './Signup';
import CustomizedDialogs from './dialog';



function App() {

  // const navigate = useNavigate();
  const [recipes, setRecipes] = useState([])
  const [currentUser, setCurrentUser] = useState('')


  useEffect(() => {
    fetch("/recipes").then(
      r => r.json()
      ).then(
        response => {
        setRecipes(response)
        console.log(response)
      }
    )
  }, [])

  useEffect(() => {
    fetch("/check_session").then((response) => {
      if (response.ok) {
        response.json().then((currentUser) => setCurrentUser(currentUser));
      }
    });
  }, []);

  function handleLogin(currentUser){
    setCurrentUser(currentUser)
  }

  function handleLogout(currentUser){
    setCurrentUser(null)
  }

  const myRecipes = recipes.filter(recipe => recipe.user_id === currentUser.id)

  // function saveRecipe(recipe) {
  //   const saveRecipe = recipe.map(recipeObj => {
  //     if ((recipeObj.id) === (recipe.recipe_id)) {
  //       recipeObj.my_recipes = true;
  //       recipeObj.user_id = recipe.user_id;
  //       return recipeObj;
  //     } else {
  //       return recipeObj;
  //     }
  //   });
  //   setRecipes(saveRecipe);
  // }


return (
  <Router>
    <div className="App">
      <Navbar currentUser={currentUser} />
      <Routes>
        <Route path="/my_recipes" element={<MyRecipes currentUser={currentUser} myRecipes={myRecipes}/>} />
        <Route path="/profile" element={<Profile currentUser={currentUser} onLogout={handleLogout} />} />
        <Route path="/login" element={<Login handleLogin={handleLogin} />} />
        <Route path="/sign_up" element={<Signup/>} />
        <Route path="/" element={<Home recipes={recipes} currentUser={currentUser} />} />
      </Routes>
    </div>
  </Router>
);
}

export default App;
