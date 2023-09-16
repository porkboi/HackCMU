import openai
import random

def getFunFacts(sy_snum, pl_orbper, pl_rade, st_rad, st_mass):
  openai.api_key = "YOUR_API_KEY"
  response = openai.Completion.create(
      engine = "text-davinci-003",
      prompt = f"tell me 3 fun facts about a hypothetical planet with {sy_snum} stars, orbital period of {pl_orbper} days, {pl_rade} times earth radius, stellar radius of {st_rad} and stellar mass of {st_mass}.",
      #prompt = text,
      temperature = 0.6,
      max_tokens = 300,
      )
  return response.choices[0].text

def getDallEPrompt(pmass, prad, st_met):
    planet_color = random.choice(["whitish-yellow", "brownish", "reddish", "bluish", "grayish"]) 
    texture = None # rocky or gaseous
    star_color = None # bluish or reddish
    
    texture_ratio = pmass/(prad**3)
    if texture_ratio < 0.5: 
        texture = "rocky"
    else:
        texture = "gaseous"

    if st_met > 0:
        star_color = "reddish"
    else:
        star_color = "bluish"

    return texture, planet_color, star_color
    

def getPlanetImage(texture, planet_color, star_color):
    openai.api_key = "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"
    response = openai.Image.create(
      prompt=f"whole photo of {planet_color}, {texture} exoplanet",
      n=1,
      size="256x256"
    )
    planet_image_url = response['data'][0]['url']
    response = openai.Image.create(
      prompt=f"astronomy photo of {star_color} star",
      n=1,
      size="256x256"
    )
    star_image_url = response['data'][0]['url']
    
    return planet_image_url, star_image_url
