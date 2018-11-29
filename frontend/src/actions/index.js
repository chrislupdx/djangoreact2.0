import * as actionType from './types';
import axios from 'axios';

export const FETCH_POSTS ='fetch_posts';
export const CREATE_POST = 'create_post';
export const FETCH_POST = 'fetch_post';
export const DELETE_POST = 'delete_post';

const ROOT_URL = 'http://127.0.0.1:8000/';
const API_KEY = 

export function fetchPost(id) {
  const request = axios.get(`${ROOT_URL}/posts/${id}${API_KEY}`);

  return{
    type: FETCH_POST,
    payload: request
  };
}


export const setToken = (data) => {
  return {
    type: actionType.SET_TOKEN,
    data
  }
}
// file: src/actions/types.js
export const SET_TOKEN = "SET_TOKEN";
