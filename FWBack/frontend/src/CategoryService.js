import React, {Component} from 'react';
import axios from 'axios';

const API_URL = 'localhost:8000';

class CategoryService{
    constructor(props) {
        super(props)
    }

    getCategory(){
        const url = `${API_URL}/api/category/`;
        return axios.get(url).then(response => response.data)
    }

    getCategoryByURL(link){
        const url = `${API_URL}${link}`
        return 

    }
}