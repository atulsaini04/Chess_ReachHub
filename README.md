# Chess Dashboard

This project is a chess dashboard that utilizes React.js for the frontend, FastAPI (Python) for the backend, Axios for API calls, and Recharts for data visualization.

## Features

- View the rating history of a specific player.
- Retrieve a list of top players.
- Download a CSV file containing the rating history of all players.

## Prerequisites

- Node.js (for the frontend)
- Python (for the backend)

## Getting Started

### Frontend

```bash
cd chess-dashboard
npm install
npm start
```
### Backend
```bash
cd fast_project
pip install -r requirements.txt
uvicorn main:app --reload
```
| Endpoint                            | Method | Description                                      | Example                                      |
| ----------------------------------- | ------ | ------------------------------------------------ | -------------------------------------------- |
| `/player/{username}/rating-history`  | GET    | Get player's rating history                     | `curl http://localhost:8000/player/johndoe/rating-history` |
| `/top-players`                      | GET    | Get list of top players                          | `curl http://localhost:8000/top-players`     |
| `/players/rating-history-csv`        | GET    | Download players' rating history as CSV         | `curl http://localhost:8000/players/rating-history-csv` |

