from io import BytesIO
from PIL import Image
import requests
import streamlit as st
import openai

#openai key
openai.api_key = "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"


def main():
    st.markdown(
        """
        <style>
        .main {
            background-color: lightgray;
            padding: 10px;
            border-radius: 10px;
            margin: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("AI Gym Website💪")
    st.write("Welcome to our AI Gym system, we generate your own training schedule depending on your desire of what you want to train today.")
    sentence = "Choose your fitness field, after generating your workout for today, train each exercise 4 sets with 12 reps each. Enjoy it my GymBro.😉 "
    

    # Display the winking emoji
    st.markdown(f"<div class='winking'>{sentence}</div>", unsafe_allow_html=True)

    st.subheader("🔥 Select Your Fitness Programs🔥 ")

    # Define the fitness programs as a list of strings
    fitness_programs = ["Strength training (weightlifting or bodybuilding exercises 🏋️)",
                        "Flexibility (Stretching 🤸‍♀️)",
                        "High-Intensity Interval Training (HIIT) 🚴‍♂️",
                        "CrossFit 🏋️‍♀️"]

    # Create radio buttons for fitness program selection
    selected_program = st.radio("Select a Fitness Program", fitness_programs)

    # Display additional options based on the selected program
    if "Strength training" in selected_program:
        st.subheader("Strength Training Options")
        push_day = st.checkbox("Push Day")
        pull_day = st.checkbox("Pull Day")
        core_day = st.checkbox("Core Day")
    else:
        push_day, pull_day, core_day = False, False, False

    # Button to trigger workout plan generation
    if st.button("Generate Workout Plan"):
        generate_workout_plan(selected_program, push_day, pull_day, core_day)

def generate_workout_plan(selected_program, push_day, pull_day, core_day):
    # Build a prompt based on the selected program and options
    prompt = build_prompt(selected_program, push_day, pull_day, core_day)

    # Make the API call using ChatCompletion.create
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the desired model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Display the generated workout plan
    st.subheader("Generated Workout Plan")
    st.write(response['choices'][0]['message']['content'])

def build_prompt(selected_program, push_day, pull_day, core_day):
    prompt = f"Design a fitness program that includes {selected_program}."

    if "Strength training" in selected_program:
        prompt += "\nSpecific Strength Training Options:"
        if push_day:
            prompt += "\n  - Push Day"
        if pull_day:
            prompt += "\n  - Pull Day"
        if core_day:
            prompt += "\n  - Core Day"

    return prompt
#     message_format = """
#     Your selected fitness program is: {program_name}

# Here are six exercises for {program_name}:
# 1. {exercise_1}
# 2. {exercise_2}
# 3. {exercise_3}
# 4. {exercise_4}
# 5. {exercise_5}
# 6. {exercise_6}

# Additional details and recommendations:
# {additional_details}
# """


   



st.markdown(
    """
    ----
    [AI GymBro] | Copyright © 2023
    """
)
if __name__ =="__main__":
    main()