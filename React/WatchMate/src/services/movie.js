import { API_BASE_URL } from '../common/api'

export const updateMovie = async (movieID ,movieData) => {
    console.log("movie details:", movieData, movieID)
    try{
        const response = await fetch(API_BASE_URL + "/list/" + movieID, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(movieData)
        });
        if (!response.ok){
            throw new Error('Response status: ${response.status}');
        }
        const result = await response.json();
        console.log(result);
        return result
    }
    catch (error){
        console.error(error.message);
    }
}
export const listMovie = async () => {
    try{
        const response = await fetch(API_BASE_URL + "/list/")
        if (!response.ok){
            throw new Error('Response status: ${response.status}');
        }
        const result = await response.json();
        console.log(result);
        return result
    }
    catch (error){
        console.error(error.message);
    }
}
export const createMovies = async (movieData) => {
    try{
        const response = await fetch(API_BASE_URL + "/list/",
            {method:"POST",
            headers:{listMovie,
                "Content-Type":"application/json"
            },
            body: JSON.stringify(movieData),
        });
        if (!response.ok){
            throw new Error('Response Status: $(response.status)')
        }
            const movie = await response.json();
            return movie
            }
        catch(error){
            console.error(error.message)
        }
        
    }
export const deleteMovie = async (movieID) => {
    try{
        const response = await fetch(API_BASE_URL + "/list/",
            {method:"DELETE",
            body: JSON.stringify(movieID),
        });
        if (!response.ok){
            throw new Error('Response Status: $(response.status)')
        }
            const movie = await response.json();
            return movie
            }
        catch(error){
            console.error(error.message)
        }
        
    }
// export default {listMovie, CreateMovies}; 
