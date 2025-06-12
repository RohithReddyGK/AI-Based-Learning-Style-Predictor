import streamlit as st 
import joblib 
import json 
import numpy as np

# Must be the first Streamlit command
st.set_page_config(page_title="Learning Style Quiz", layout="centered")

# Load model once per session
@st.cache_resource 
def load_model(path): 
    return joblib.load(path)

# Load questions once per session
@st.cache_data 
def load_questions(path): 
    with open(path, "r") as f: 
        return json.load(f)

# Load the model and questions
model = load_model("learning_style_model.pkl") 
questions = load_questions("questions.json")

# App Title & Instructions
st.title("🎓 Discover Your Learning Style") 
st.markdown("Take this quick quiz to identify your dominant learning style: **Visual, Auditory, or Kinesthetic**!")

responses = []

# Display quiz form
if questions:
    with st.form("quiz_form"):
        for i, question in enumerate(questions):
            val = st.slider(f"{i+1}. {question}", 1, 5, 3)
            responses.append(val)
        submitted = st.form_submit_button("🎯 Predict My Learning Style")

# When form is submitted
if submitted and model:
    input_array = np.array(responses).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    # Explanations dictionary
    explanations = {
        0: {
            "style": "👁️ Visual Learner",
            "description": (
                "You're a **Visual Learner**, which means your brain processes and retains information more effectively through **images, diagrams, colors, and spatial understanding**. 🧠✨\n\n"
                "You love to see things mapped out – whether it’s **mind maps, flowcharts, infographics, or whiteboards**. You’re likely to recall how a page looked rather than what it said.\n\n"
                "Visual learners often prefer reading instructions over hearing them and find it easier to understand abstract concepts when they’re presented visually. You may also think in pictures!"
            ),
            "tips": [
                "📊 Use diagrams, charts, mind maps, and color-coded notes.",
                "🖼️ Visualize concepts using infographics and sketches.",
                "📸 Take screenshots or photos of important material.",
                "🧠 Create mental images while studying complex topics.",
                "📝 Organize study material spatially (e.g., use flashcards)."
            ],
            "links": [
                "[🌐 Visual Learning Strategies – Education Corner](https://www.educationcorner.com/visual-learning.html)",
                "[🎨 Tips for Visual Learners – Mind Tools](https://www.mindtools.com/a4wo118/visual-learning-style)",
                "[📹 YouTube: Visual Learner Study Tips THAT WORK!](https://www.youtube.com/watch?v=IN-_S_jj3gE)"
            ]
        },
        1: {
            "style": "🎧 Auditory Learner",
            "description": (
                "You are an **Auditory Learner** – your brain is wired to learn best through **listening, speaking, and hearing**. 🗣️🎙️\n\n"
                "You understand and retain information when it’s **spoken or heard aloud**. Whether it’s through lectures, podcasts, discussions, or music, auditory learners like you thrive on **sound-based input**.\n\n"
                "You probably enjoy reading aloud, talking through problems, and may find it easier to recall conversations than written instructions. You’re an excellent listener, communicator, and verbal explainer!"
            ),
            "tips": [
                "🔊 Record and listen to lectures or your own voice notes.",
                "🧑‍🤝‍🧑 Engage in group discussions and verbal explanations.",
                "🎧 Use audio-based study tools like podcasts or explainer videos.",
                "📢 Recite key points or read your notes out loud.",
                "🎵 Turn facts into rhymes, jingles, or songs for memory boosts."
            ],
            "links": [
                "[🔉 Understanding Auditory Learning – Education Corner](https://www.educationcorner.com/auditory-learning.html)",
                "[🧠 Tips for Auditory Learners – Learning Styles Online](https://www.learning-styles-online.com/style/auditory-verbal/)",
                "[🎥 YouTube: Auditory Learner Study Tips THAT WORK!](https://www.youtube.com/watch?v=bgIXy2dVXdc)"
            ]
        },
        2: {
            "style": "🤸 Kinesthetic Learner",
            "description": (
                "You are a **Kinesthetic Learner**, also known as a **tactile or hands-on learner**. 🙌 Your learning style is action-oriented – you learn best by **doing, touching, and physically engaging** with content.\n\n"
                "You’re most likely to retain information when it’s experienced through **movement, experiments, simulations, or real-life application**. Sitting still for long periods may make it harder for you to concentrate.\n\n"
                "Kinesthetic learners often excel in **lab activities, building models, role-playing, using flashcards physically**, and even learning while walking or exercising. 🏃"
            ),
            "tips": [
                "🧪 Engage in experiments, models, or real-life demos.",
                "🎭 Act out scenes or simulate concepts physically.",
                "📝 Use textured study materials or hands-on flashcards.",
                "🚶 Walk around while reviewing material (movement-based memory).",
                "🕹️ Try educational games or simulations to stay active."
            ],
            "links": [
                "[🤲 Kinesthetic Learning Techniques – Learning Styles Online](https://www.learning-styles-online.com/style/kinesthetic-tactile-learning/)",
                "[🧠 Hands-on Learning Ideas – Resilient Educator](https://resilienteducator.com/classroom-resources/hands-on-learning/)",
                "[🎮 YouTube: Study Tips for Kinesthetic Learners](https://www.youtube.com/watch?v=kib7Pn6qOGA)"
            ]
        }
    }

    # Display result
    info = explanations.get(prediction)
    if info:
        st.success(f"Your Learning Style: {info['style']}")
        st.markdown(f"### 📘 Description\n{info['description']}")
        st.markdown("### ✅ Study Tips")
        for tip in info['tips']:
            st.markdown(f"- {tip}")
        st.markdown("### 🔗 Learn More")
        for link in info['links']:
            st.markdown(link)
    else:
        st.error("Something went wrong while determining your learning style.")