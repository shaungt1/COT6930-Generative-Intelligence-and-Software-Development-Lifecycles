#!/bin/bash

# Step 1: Create and Activate Virtual Environment
if [ ! -d "PROMPTLABENV" ]; then
    echo "Virtual environment 'PROMPTLABENV' not found. Creating it now..."
    python -m venv PROMPTLABENV
    echo "Virtual environment 'PROMPTLABENV' created."
else
    echo "Virtual environment 'PROMPTLABENV' already exists."
fi

echo "Activating virtual environment 'PROMPTLABENV'..."
source PROMPTLABENV/Scripts/activate

# Step 2: Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    python -m pip install --upgrade pip
    python -m pip install --break-system-packages -r requirements.txt
else
    echo "No requirements.txt found. Skipping dependency installation."
fi

# Step 3: Configure the Prompt Engineering Lab
CONFIG_PATH="prompt-eng/_config"
EXAMPLE_CONFIG="prompt-eng/_config.example"

if [ ! -f "$CONFIG_PATH" ]; then
    if [ -f "$EXAMPLE_CONFIG" ]; then
        echo "Copying _config.example to _config..."
        cp "$EXAMPLE_CONFIG" "$CONFIG_PATH"
        echo "_config file created. Please edit it to match your server settings if needed."
    else
        echo "_config.example not found. Please create the configuration file manually."
    fi
else
    echo "_config already exists. Skipping copy."
fi

# Step 4: Display instructions for running Ollama server
echo -e "\nEnvironment setup completed successfully!\n"

echo "To run the Ollama server locally and allow external connections, use:"
echo "export OLLAMA_HOST=0.0.0.0"
echo "ollama server"

echo -e "\nTo test the connection to the Ollama server, run:"
echo "python prompt-eng/_pipeline.py"

echo -e "\nExpected output if successful:"
echo "1 + 1 = 2"
echo "Time taken: 3.111s"

echo -e "\nIf you encounter issues, refer to the Troubleshooting section in the documentation."
