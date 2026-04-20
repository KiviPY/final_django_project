import { useEffect, useState } from "react"
import "./App.css"

function App() {
  const [apartments, setApartments] = useState([])

  useEffect(() => {
    fetch("http://127.0.0.1:8000/apartments/")
      .then(res => res.json())
      .then(data => {
        console.log(data)
        setApartments(data.results)
      })
  }, [])

  return (
    <div>
      <h1>Apartments</h1>

      {apartments.map(ap => (
        <div key={ap.id}>
          <div className="card">
              <div className="image">{ap.image}</div>
              <div className="info">
                  <h2 className="title">{ap.title}</h2>
                  <p>City: {ap.city}</p>
                  <p className="price"> Price: {ap.price_per_month} €</p>
                  <p>Address: {ap.address}</p>
                  <p>Minimal rent: {ap.min_rent_duration} months</p>
                  <p>{ap.size}</p>
              </div>
          </div>
        </div>
      ))}
    </div>
  )
}

export default App
