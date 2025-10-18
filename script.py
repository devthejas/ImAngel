
import requests
from flask import Flask, render_template, request, jsonify, send_file
import io

app = Flask(__name__)

# Replace with your actual ngrok URL from Colab
COLAB_URL = 'https://_Your_link_/generate'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        prompt = request.form.get('prompt')
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        print(f"Sending request to Colab: {prompt}")
        
        # Forward request to Colab with extended timeout
        response = requests.post(
            COLAB_URL, 
            data={'prompt': prompt},
            timeout=360,  # 6 minutes timeout
            stream=False  # Don't stream, wait for complete response
        )
        
        print(f"Response status: {response.status_code}")
        print(f"Response size: {len(response.content)} bytes")
        
        if response.status_code == 200:
            # Ensure we have the complete image data
            image_data = response.content
            
            if len(image_data) < 1000:  # Suspiciously small for a PNG
                print("Warning: Image data seems incomplete")
                return jsonify({'error': 'Incomplete image data received'}), 500
            
            # Return the complete image
            return send_file(
                io.BytesIO(image_data),
                mimetype='image/png',
                as_attachment=False,
                download_name='generated.png'
            )
        else:
            return jsonify({'error': 'Failed to generate image'}), 500
            
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timeout - generation took too long'}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Connection error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)