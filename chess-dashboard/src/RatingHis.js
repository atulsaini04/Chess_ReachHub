import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'

const RatingHis = () => {
  const {
    player
  }=useParams()
  const [ratingHistory, setRatingHistory] = useState([]);
  const [Chessname, setname] = useState([]);

  useEffect(()=>{
    const rating=async ()=>{
      try {
        const response = await axios.get(`http://localhost:8000/player/${player}/rating-history`);
        setRatingHistory(response?.data?.rating_history);
        // console.log(response)
      } catch (error) {
        console.error('Error fetching top players:', error);
      }
    }
    rating()
  },
  []) 
  useEffect(()=>{
    const games=ratingHistory.length>0&&ratingHistory.map((game)=>({"name":game.name}))
    // console.log(games);
    setname(games)


  },
  [ratingHistory])
  return (
    <div>{
      Chessname?.length>0&&Chessname.map((gameName)=>(
        <Link key={gameName.name} to={`/rating-history/${player}/${gameName.name}`} style={{display:'block'}}>
          {
            gameName.name
          }
          </Link>
      ))
      }</div>
  )
}

export default RatingHis