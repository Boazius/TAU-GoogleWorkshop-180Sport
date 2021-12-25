import i18n from "src/boot/i18n";
import { Quasar } from "quasar";
import axios from "axios";

const serverUrl = "http://127.0.0.1:5000";
const id_token ='eyJhbGciOiJSUzI1NiIsImtpZCI6ImQ5OGY0OWJjNmNhNDU4MWVhZThkZmFkZDQ5NGZjZTEwZWEyM2FhYjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiOTE5NjE5ODQ4MTI3LTBkNWF0YThvaTY0ZzRuZWVzbTd2c3MwY2IzMGV2bnBoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiOTE5NjE5ODQ4MTI3LTBkNWF0YThvaTY0ZzRuZWVzbTd2c3MwY2IzMGV2bnBoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTAzNzc3NjcyNDYwNjM0Mjc3MDg5IiwiZW1haWwiOiJkYW5pZWxsZS5yb3Rob2x0ekBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6IkVRazVrc3FjWFdwSEIyUkt5bGpwRVEiLCJub25jZSI6IjJNeUlGMnVmbkQyaGYzYWVsMU92IiwiaWF0IjoxNjQwMzU3Mjg0LCJleHAiOjE2NDAzNjA4ODR9.Onu261RYM4iSSSPTIQMiJ2wg8f0Dpp9YHjet8s7aaNunZ_4Z7nlpuHgmzPQ08_imKPfJMXpwRVu0FI5cqOW9iasOn3tjIVXJjmGZVUNkVNcXQAUp1VWnBBzUkqmlTPT6Rdqyg98uwm63pqJ3xvOigwH8xklv8C4n4DlxAQa1Aj3ILxTjtbrL3Z3YfXZSBIFVgTm0L2gF3Vq_vDcgLmk-SDNxawoBcgbF4m4vN13dZCFGLO99qi40YsGPLNTsL63DD4_RY-s0326iA2w1kwRXbfdHVRSAo2EjOu9ImHLdOFBAI97zxpwDnqhLVGlligICsWrY0gEbe9U2YZXnbdggcA'

//
//  Getters: Get All Trainees
//
export async function getTrainees () { //***** when a new call of get all trainees is added change to it ******
    const response = await axios
    .get(`${serverUrl}/admin/get_all_users`,{
        headers: { 
            'x-access-token': id_token,
        },
    })
    .then((res)=> res.data)
    .catch((error)=>{
        console.log(error);
        return error;
    });
    console.log(response)
    return response;
}


//
//  Getters: Get All Volunteers
//
export async function getVolunteers (/* state */) {//***** when a new call of get all Volunteers is added change to it ******
    const response = await axios
    .get(`${serverUrl}/admin/get_all_users`,{
        headers: { 
            'x-access-token': id_token,
        },
    })
    .then((res)=> res.data)
    .catch((error)=>{
        console.log(error);
        return error;
    });
    console.log(response)
    
    return response;
}


//
//  Getters: Get All Trainers
//
export async function getTrainers (/* state */) {
    const response = await axios
    .get(`${serverUrl}/admin/get_all_trainers`,{
        headers: { 
            'x-access-token': id_token,
        },
    })
    .then((res)=> res.data)
    .catch((error)=>{
        console.log(error);
        return error;
    });
   // console.log(response)
    
    return response;
}


//
//  Getters: Get All Groups
//
export async function getGroups (/* state */) {
    const response = await axios
    .get(`${serverUrl}/admin/get_all_groups`,{
        headers: { 
            'x-access-token': id_token,
        },
    })
    .then((res)=> res.data)
    .catch((error)=>{
        console.log(error);
        return error;
    });
    //console.log(response)
    return response;
}
