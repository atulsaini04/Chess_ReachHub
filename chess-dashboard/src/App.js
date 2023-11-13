import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Code from "./Code";
import RatingHis from "./RatingHis";
import Game from "./Game";


export default function App() {
 
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Code />} />
        <Route path="/player/:player" element={<RatingHis/>} />
        <Route path="/rating-history/:player/:game" element={<Game/>} />

        </Routes>
    </BrowserRouter>
  );
}