# Nirvana Take Home Project

### Repository for Nirvana challenge

# 📄 Introduction
The purpose of this project is to solve the take-home challenge for Nirvana in order to be part of its engineering team and be awesome together.

# 🐞 Instructions

Suppose you have 3 different APIs you can call with member_id as a parameter.

So example API calls would be:

`https://api1.com?member_id=1`

`https://api2.com?member_id=1`

`https://api3.com?member_id=1`

and you'll get responses from these apis with similar responses:

API1: {deductible: 1000, stop_loss: 10000, oop_max: 5000}

API2: {deductible: 1200, stop_loss: 13000, oop_max: 6000}

API3: {deductible: 1000, stop_loss: 10000, oop_max: 6000}

As you can see above the API's don't always agree. The task is to build an API that calls these APIs and coalesces the responses with a strategy. 

An example strategy could be the average of the response fields. With the average strategy, your coalesce API would respond with:

{deductible: 1066, stop_loss: 11000, oop_max: 5666}

Your API should:

Take in the member_id as a parameter
Make the calls to the different APIs
Coalesce the data returned by the APIs
As a bonus challenge: allow for the coalescing strategy to be configurable

# ⚙️ Setup and Run
To run these project is necessary following the next steps.

## Local environment

### Requirements
* python 3.8+
* pipenv
* make

#### Clone the project
```bash
$ git clone https://github.com/ChrisVidal10/nirvana-challenge.git
```

####  Install dependencies
- To install all the requirements pleas run the next command with make.

```bash
$ make install_deps
```

#### Local execution
- Run the command `Flask run` to start the server (http://localhost:3000)

```bash
$ Flask run
```

### Testing the code
- Run the command `pytest -v` run all the tests

```bash
$  python -m pytest -v
```

### Strategies

- Mean: Arithmetic mean ("average")
- Mode: Most common value
- Median: Middle value
- Max: Maximum value
- Min: Minimum value

### Endpoints

- GET `/coalesce-api?member_id={REQUIRED}&coalescing_strategy={OPTIONAL}`

The default strategy is arithmetic mean ("average").

### Example

- GET `http://127.0.0.1:3000/coalesce-api?member_id=1&coalescing_strategy=max`
```json
{
  "deductible": 1200,
  "oop_max": 6000,
  "stop_loss": 13000
}
```

- If the `member_id` is invalid the API returns a `404` Error and the following text. `http://127.0.0.1:3000/coalesce-api?member_id=t3st`
```json
{
  "error": "Member Id #t3st Not found"
}
```