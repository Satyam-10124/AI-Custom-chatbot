

AI-Custom-Chatbot 🚀

An AI-powered customizable chatbot for engaging and motivational conversations!

This project uses advanced AI tools and platforms to create a customizable learning chatbot. Designed to motivate and inspire audiences, the chatbot can easily be adapted to other roles by modifying its configuration.

🔧 Built Using:

	•	GROQ Free API: For seamless AI processing.
	•	Google Colab Notebook: To train and test the model effortlessly.
	•	Hugging Face: For deployment and easy accessibility.
	•	Gradio: For a user-friendly web interface.

🌟 Key Features:

	1.	Customizable Roles:
Modify the chatbot’s behavior by editing these lines:
	•	System Role: Line 13
	•	User Role: Line 14
(Default Role: Motivator for the audience)
	2.	Efficient Integration:
Utilizes openai==0.28 for powerful AI interactions.
	3.	Simple Deployment:
Host the chatbot on Hugging Face with minimal setup.

🚀 Deployment Guide:

Follow these steps to deploy the chatbot on Hugging Face:

	1.	Create a Space:
Log in to Hugging Face and create a new Space for the chatbot.
	2.	Add Files:
Upload the following files to the Space:
	•	app.py
	•	requirements.txt
	3.	Set Up Requirements:
Add the following dependencies to requirements.txt:

gradio
openai==0.28


	4.	Store API Key:
Save your GROQ API Key in the Secrets section of Hugging Face under the variable:

GROQ_API_KEY


	5.	Run and Deploy:
Launch the Space and watch your chatbot come to life!

💡 Contribution Guide:

We welcome contributions to make this project better!
Here are some ideas to get started:

	•	Add more roles and use cases.
	•	Improve the interface with Gradio components.
	•	Optimize performance for broader audiences.

Feel free to submit pull requests or open issues for suggestions.

🌍 Join the Community:

This project thrives on collaboration and creativity. Let’s work together to inspire audiences through AI!

🎉 Start your journey with the AI-Custom-Chatbot now!
