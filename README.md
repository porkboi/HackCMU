# HackCMU
Hack CMU 2023

## Inspiration
Bearth.ai generates hypothetical scientifically-based planets. It supports the following primary objectives:
- Enable artists to create scientifically plausible fictional worlds
- Spark interest in STEM research through self-directed (planetary) discoveries
- More efficient planetary discovery by predicting existence/location of new planets

## What it does
- Optional user input: Stellar Radius, Stellar Mass, No. of Stars, Orbital Period, Planet Radius
- Extrapolation of features (predict): Star Metallicity, Planet mass
- Identifies likely star system
- Generates visualisation for planet and star
- 3 fun facts about planet based on user input

## How we built it
- AI models (tabgan, SGD) for extrapolation of features, and identification of probable star system
- OpenAI API for visualisation of planet and star, and fun facts about planet
- Front-end app using Kivy

## Challenges we ran into
- GANs: Establishing correct scalars and transformer for pipeline
- Classifying Star Systems: Too many categories prompted us to use a regressor to bootstrap a classification
- Prompt Engineering: SDM does not understand raw data
- Learning many new technical skills within a short time span

## Accomplishments that we're proud of
In 1 day, we built a functioning minimum viable product.  We also acquired and exercised several new skills, such as...

## What we learned
- Training a generative adversarial network
- Stochastic Gradient Descent
- Calling on openai API
- Front-end mobile app development
- Creative problem solving

## What's next for Bearth.ai
More data sets would allow us to increase reliability in predicting and discovering new habitable planets.
