#!/bin/bash

# Marine Route Optimization Streamlit App Setup Script
# =====================================================

echo "🚢 Marine Route Optimization Streamlit App Setup"
echo "================================================"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install required packages
echo "📚 Installing required packages..."
echo "   This may take a few minutes..."

# Install packages one by one to handle potential conflicts
pip install streamlit
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install plotly
pip install scikit-learn

# Optional: Try to install TensorFlow (may fail on some systems)
echo "🧠 Attempting to install TensorFlow (optional)..."
pip install tensorflow || echo "⚠️ TensorFlow installation failed - neural network features will be limited"

echo ""
echo "✅ Installation complete!"
echo ""
echo "🚀 To run the Streamlit app:"
echo "   1. Activate the virtual environment: source venv/bin/activate"
echo "   2. Run the app: streamlit run marine_route_optimization_app.py"
echo ""
echo "📝 Alternative: Run the simple demo without dependencies:"
echo "   python3 simple_marine_demo.py"
echo ""
echo "🌐 The Streamlit app will open in your web browser automatically."
echo "   If not, navigate to: http://localhost:8501"