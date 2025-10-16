import { API_BASE_URL } from "../common/api";

export const updateMovie = async (movieID, movieData) => {
  console.log("movie details:", movieData, movieID);
  try {
    const response = await fetch(`${API_BASE_URL}/${movieID}/`, {
      method: "PATCH",
      headers: {
        listMovie,
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("authToken")}`,
        },
      body: JSON.stringify(movieData),
    });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const result = await response.json();
    console.log(result);
    return result;
  } catch (error) {
    console.error(error.message);
  }
};
export const listMovie = async () => {
  try {
    const options = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("authToken")}`,
      },
    };
    console.log("Options:", options);
    const response = await fetch(`${API_BASE_URL}/`, options);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const result = await response.json();
    return result;
  } catch (error) {
    // console.error(error.message);
    console.log("Error:", error);
  }
};
export const createMovies = async (movieData) => {
  try {
    const response = await fetch(API_BASE_URL + "/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("authToken")}`,
      },
      body: JSON.stringify(movieData),
    });
    if (!response.ok) {
      throw new Error(`Response Status: ${response.status}`);
    }
    const movie = await response.json();
    return movie;
  } catch (error) {
    console.error(error.message);
  }
};
export const deleteMovie = async (movieID) => {
  try {
    const response = await fetch(`${API_BASE_URL}/${movieID}/`, {
      method: "DELETE",
      headers: {
        Authorization: `Token ${localStorage.getItem("authToken")}`,
      },
    });
    if (!response.ok) {
      throw new Error(`Response Status: ${response.status}`);
    }
    const movie = await response.json();
    return movie;
  } catch (error) {
    console.error(error.message);
  }
};
// export default {listMovie, CreateMovies};
