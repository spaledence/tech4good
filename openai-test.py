from openai import OpenAI
client = OpenAI()



extract_data = [
{
  "name": "extract_data",  
  "description": "split up job positions that contributed to what the author is grateful for, describing what they each do separately",
  "parameters": {
      "type": "object",
      "properties": {
          "Groups": {
            "type": "string",
            "description": "The job position or group that contributed to the gratitude that is being shown by the author, (e.g. Park Rangers or Landscapers). Keep in mind, these are thank you notes that are appreciating the environment/nature of santa cruz, and the people that work in this realm. So think about how they relate to what the user is grateful for. Before finishing, think about if this 'group or thing' is in a genuine line of work that one can hold"
          },
          "Acknowledgment":{
            "type": "string",
            "description": "How each line of work has played a role in the author's gratitude of the community.  There should be at least one sentence for each acknowledgment group. Each sentence should be in the plural first person (we). Do not include I or Me. Each sentence should be prefaced with a thank you. For example, (Thank you Park Rangers, for helping us appreciate the beautiful nature and wildlife of Santa Cruz)."
            }

      },
      "required": ["groups", "acknowledgment"]      
  
  }
}
]



response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    #response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to extract out the people/jobs that contributed to what the author is grateful for (example: the park rangers that enable us to appreciate the beautiful nature in Santa Cruz). Given a gratitude note, we’d like to get the recipient groups that deserve thanks. We also want a concise yet descriptive explanation of what the recipient group does or has done to receive thanks. Write descriptively and intelligently, but make sure to NOT REUSE WORDS FROM the AUTHOR. Do not include coworkers / colleagues as an Acknowledgment group."},

        {"role": "user", "content": "To live in Santa Cruz is a blessing in and of itself, but the college campus is like the crown jewel of the city. Every time I drive up to campus for work, I almost have to pinch myself because it is hard to believe this is the place that I'm employed. I'm filled with gratitude for the wide open, rolling fields and beautiful redwoods surrounding the quaint buildings. It's the breathtaking view of the ocean and the gorgeous landscape that I'm grateful for mostly. Beyond that, there is plenty to be grateful about among my friendly and super helpful coworkers." }
    ],
    functions = extract_data,
    function_call = "auto"
)



#print(response)
print(response.choices[0].message)


