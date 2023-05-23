import React from 'react'
import RecipeList from './RecipeList'

function MyRecipes({ currentUser}) {

  return (
      <div className="container mx-auto bg-amber-200 rounded-xl border p-8 drop-shadow-3xl font-bold text-2xl">
        <h1>My Saved Recipes</h1>
        <RecipeList currentUser={currentUser}/>
    </div>
  )
}

export default MyRecipes;