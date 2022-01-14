<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Bit68 PRoducts API</h3>
</div>

<!-- ABOUT THE PROJECT -->

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mohamed-menam/Bit68Task.git
   ```
2. Run Project
   ```
   docker-compose up
   ```

<!-- USAGE EXAMPLES -->

## Usage

### Login

` [POST] http://0.0.0.0:8000/api/v1/users/login`

```
body {
    email: "a@ex.com",
    password: "1234567"
}
```

### Register

` [POST] http://0.0.0.0:8000/api/v1/users/register`

```
body {
    name: "Person 1"
    email: "a@ex.com",
    password: "1234567"
}
```

### Get Products

` [GET] http://0.0.0.0:8000/api/v1/peoducst`

```
query params seller={userID} & page=

```

### Create Product

` [POST] http://0.0.0.0:8000/api/v1/products`

```
body {
    name: "Person 1"
    price: 10.5,
    seller: 1 // user id that's already loggedIn
}
```
