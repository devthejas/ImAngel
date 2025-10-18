#  ImAngel - Text to Image Generator

A full-stack web application that generates high-quality AI images from text prompts using Stable Diffusion. Built with Flask, powered by Google Colab's free GPU, featuring a modern chat-style interface.

---

## ✨ Features

- 🎯 High-Quality Generation: 768×768 or 1024×1024 resolution images  
- 💬 Chat Interface: Modern, responsive UI with real-time feedback  
- ⚡ Async Processing: Smoothly handles 5-8 minute generation times  
- ☁️ Cloud GPU: Free Google Colab T4/L4 GPU via ngrok tunnel  
- 🎨 Smart Prompts: Auto-enhancement for better quality  
- 🚫 Negative Prompts: Filters blur and low-quality artifacts  

---

## 🏗️ Architecture

Browser (UI) ←→ Flask Server (Local) ←→ Colab Server (GPU/AI)

text

1. User enters prompt in web interface  
2. Flask forwards request to Colab via ngrok  
3. Stable Diffusion generates image on GPU  
4. Image returned and displayed in the browser  

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+  
- Google Account (for Colab access)  
- Ngrok account (free tier supported)  
- Modern web browser  

### Installation

git clone https://github.com/createwithathuldas/ImAngel.git
cd ImAngel

text

---

## ⚙️ Setup Guide

### 1. Setup Ngrok

- Sign up at [ngrok.com](https://ngrok.com)  
- Get your authtoken from [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken)  

### 2. Run the Colab Server

- Open the notebook in `colab_notebooks/` folder on [Google Colab](https://colab.research.google.com/)  
- Replace `YOUR_NGROK_TOKEN_HERE` with your ngrok authtoken in the first cell  
- Run all cells to set up Stable Diffusion, ngrok tunnel, and Flask server on Colab  
- Copy the public ngrok URL (something like `https://xxxx-xx-xxx-xxx.ngrok-free.app`) shown in output  

### 3. Configure Local Flask Server

- Open `script.py` in a text editor  
- Find the line:  
COLAB_URL = 'https://your-ngrok-url.ngrok-free.app/generate'

text
- Replace `'https://your-ngrok-url.ngrok-free.app/generate'` with the ngrok URL copied from Colab plus `/generate` endpoint  
- Save the file  

### 4. Start Local Flask Server

python script.py

text

- Open browser at [http://localhost:5000](http://localhost:5000)  
- Enter a prompt and click "Generate" to see your AI-generated image  

---

## 🎯 Usage Tips

- Be specific with prompts (e.g., "a red apple on a wooden table")  
- Use style keywords ("photorealistic", "oil painting", etc.)  
- Include details about lighting and atmosphere  
- Use quality terms like "highly detailed", "sharp", "8k resolution"  

---

## 📁 Project Structure

ImAngel/
├── script.py # Local Flask server
├── templates/
│ └── index.html # Web UI chat interface
├── colab_notebooks/
│ └──colab_server_high_quality.ipynb # Colab GPU server (768x768)
│ 
├── screenshots/ # Demo images
└── README.md # This file

text

---

## ⚙️ Configurations

Modify generation settings inside Colab's `generate_image()` function:

| Parameter           | Default | Description                               |
|---------------------|---------|-------------------------------------------|
| `width`             | 768     | Image width (512 to 1024)                  |
| `height`            | 768     | Image height (512 to 1024)                 |
| `num_inference_steps` | 50      | Quality/detail level (higher = better)    |
| `guidance_scale`    | 8.5     | Prompt adherence strength                   |

---

## 🔧 Troubleshooting

- **Cannot connect to Colab:** Check Colab notebook is running and ngrok URL is current  
- **Ngrok authentication failed:** Ensure correct ngrok authtoken in notebook  
- **Out of memory:** Use smaller resolution or SD 2.1 model; restart Colab runtime  
- **Slow generation:** 5-8 minutes is normal for quality images  
- **Tunnel closed:** Restart Colab for a new ngrok URL and update local config  

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap  
- **Backend:** Flask, Requests  
- **AI Model:** Stable Diffusion 2.1 / SDXL 1.0  
- **Infrastructure:** Google Colab GPU, Ngrok  

---

## 🤝 Contributing

Contributions welcome!  

1. Fork the repo  
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)  
4. Push to branch (`git push origin feature/AmazingFeature`)  
5. Open a Pull Request  

---

## 📝 License

MIT License (see LICENSE file). Stable Diffusion models have their own licenses.

---

## 🙏 Acknowledgments

- [Stability AI](https://stability.ai/) - Stable Diffusion  
- [Hugging Face](https://huggingface.co/) - Diffusers  
- [Google Colab](https://colab.research.google.com/) - Free GPU  
- [Ngrok](https://ngrok.com/) - Tunneling service  

---

## 📧 Contact

Your Name - [createwithathuldas@gmail.com](mailto:createwithathuldas@gmail.com)  
GitHub: [https://github.com/createwithathuldas/ImAngel.git](https://github.com/createwithathuldas/ImAngel.git)  
LinkedIn: [https://www.linkedin.com/in/athul-das-760105284/](https://www.linkedin.com/in/athul-das-760105284/)  
Portfolio: [https://createwithathuldas.github.io/portfolio/](https://createwithathuldas.github.io/portfolio/)  

<div align="center">
⭐ Star this repo if you find it helpful!  
Made with ❤️ and ☕  
</div>
