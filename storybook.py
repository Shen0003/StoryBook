##not native library so came out the error, can ignore
import os
from openai import OpenAI
import streamlit as st  #important

#init API key
# REPLACE: client = OpenAI(api_key=os.environ['OPENAI_API_KEY']) to
#Use streamlit Secrets management
client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])


#Story Function
def story_generator(prompt):
    system_prompt = """
  You are a world renowned author for young adults fiction short stories.
  Given a concept, generate a short story relevant to the themes of the concept with a twist ending. The total length of the story should be within 100 words.
  """
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{
            'role': 'system',
            'content': system_prompt
        }, {
            'role': 'user',
            'content': prompt
        }],
        temperature=1.3,  #to be more creative
        max_tokens=2000)

    return response.choices[0].message.content


#Cover art Function
def art_generator(prompt):
    response = client.images.generate(model='dall-e-2',
                                      prompt=prompt,
                                      size='1024x1024',
                                      n=1)
    return response.data[0].url


#Cover prompt design Function
def design_generator(prompt):
    system_prompt = """
  You will be given a short story. Generate a prompt for a cover art that is suitable for the story. The prompt is for dall-e-2.
  """
    response = client.chat.completions.create(model='gpt-4o-mini',
                                              messages=[
                                                  {
                                                      'role': 'system',
                                                      'content': system_prompt
                                                  },
                                                  {
                                                      'role': 'user',
                                                      'content': prompt
                                                  },
                                              ],
                                              temperature=1.3,
                                              max_tokens=2000)
    return response.choices[0].message.content


#Output
prompt = st.text_input("Enter a prompt")
if st.button("Generate"):
    story = story_generator(prompt)
    design = design_generator(story)
    art = art_generator(design)

    st.caption(design)
    st.divider()
    st.write(story)
    st.divider()
    st.image(art)
