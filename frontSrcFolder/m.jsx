import React from 'react'
import './m.css'

const IMG_BASE_URL = 'https://image.tmdb.org/t/p/w1280/';
function Home({ title, poster_path, vote_average }) {
    return (
        <div className='movie'>

            <button className='home_container'>
                <img src={IMG_BASE_URL + poster_path} alt="영화포스터" />
            </button>
            <div className='movie_info'>
                <div className='movieFont'>{title}</div>
            </div>
        </div>
    );
}

export default Home;