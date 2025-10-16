const API_BASE_URL = "http://localhost:8000"
export const login = async (loginData) => {
    try{
        const response = await fetch(API_BASE_URL + "/account/login/" ,
            {method:"POST",
            headers:{
                "Content-Type":"application/json",
            },
            body: JSON.stringify(loginData),
        });
        // if (!response.ok){
        //     throw new Error('Login Failed')
        // }
            const user = await response.json();
            return user
            }
        catch(err){
            return err;
            // setError("Username or Password herera hal gada")
        }
    }
