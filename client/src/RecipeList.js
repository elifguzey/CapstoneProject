import React from 'react'
import RecipeCard from './RecipeCard'



function RecipeList({recipe, currentUser, myRecipes, mySavedRecipes}) {
    const recipeCardArray = recipe.map(recipeObj => {
        return <RecipeCard key={recipeObj.id} recipe={recipeObj} currentUser={currentUser} myRecipes={myRecipes} mySavedRecipes={mySavedRecipes}/>
    })

    return (
        <div>
             <section className="mb-20">
                <div className="container mx-auto ">
                    <div className="grid gap-4 2xl:grid-cols-6 2xl:gap-4 xl:grid-cols-5 xl:gap-4 lg:grid-cols-4 lg:gap-4 md:grid-cols-3 md:gap-4 sm:grid-cols-2 sm:gap-4 bg-amber-200">{recipeCardArray}</div>
                </div>  
            </section>
        </div>
        )
}

export default RecipeList;  



