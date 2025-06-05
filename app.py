import streamlit as st
import json
import random

# Streamlit configuration
st.set_page_config(
    page_title="AI Image Prompt Builder", 
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ AI Image Prompt Builder")
st.markdown("Generate comprehensive prompts for AI image generation with visual controls")

# Helper functions
def render_selectbox(label, options, default_val, help_text=""):
    """Render a selectbox with custom option"""
    extended_options = list(options) + ["Custom..."]
    try:
        default_index = extended_options.index(default_val)
    except ValueError:
        default_index = len(extended_options) - 1
    
    selection = st.selectbox(
        label, 
        extended_options, 
        index=default_index,
        help=help_text
    )
    
    if selection == "Custom...":
        return st.text_input(f"Custom {label}:", value=default_val if default_val not in options else "")
    return selection

# Basic prompt controls
col1, col2 = st.columns(2)

with col1:
    st.subheader("Basic Settings")
    
    # Aspect ratio
    aspect_ratios = ["16:9", "1:1", "4:3", "3:2", "9:16"]
    aspect_ratio = render_selectbox(
        "Aspect Ratio", 
        aspect_ratios, 
        "16:9", 
        "Choose the image dimensions"
    )
    
    # Style
    styles = ["photorealistic", "digital art", "oil painting", "sketch", "watercolor", "anime", "comic book"]
    style = render_selectbox(
        "Art Style", 
        styles, 
        "photorealistic",
        "Select the artistic style"
    )
    
    # Environment
    environments = ["studio", "outdoor", "urban", "nature", "indoor", "abstract background"]
    environment = render_selectbox(
        "Environment", 
        environments, 
        "studio",
        "Choose the setting"
    )

with col2:
    st.subheader("Visual Controls")
    
    # Lighting
    lighting_types = ["natural", "dramatic", "soft", "harsh", "golden hour", "blue hour", "neon"]
    lighting = render_selectbox(
        "Lighting", 
        lighting_types, 
        "natural",
        "Select lighting style"
    )
    
    # Color scheme
    color_schemes = ["vibrant", "muted", "monochrome", "warm tones", "cool tones", "pastel", "high contrast"]
    colors = render_selectbox(
        "Color Scheme", 
        color_schemes, 
        "vibrant",
        "Choose color palette"
    )
    
    # Camera angle
    camera_angles = ["front view", "side view", "low angle", "high angle", "close-up", "wide shot"]
    camera_angle = render_selectbox(
        "Camera Angle", 
        camera_angles, 
        "front view",
        "Select camera perspective"
    )

# Custom prompt input
st.subheader("Custom Elements")
custom_prompt = st.text_area(
    "Additional Details", 
    placeholder="Add any specific details, subjects, or modifications...",
    height=100
)

# Generate button
if st.button("🎨 Generate Prompt", type="primary"):
    # Build the prompt
    prompt_parts = []
    
    if custom_prompt:
        prompt_parts.append(custom_prompt)
    
    prompt_parts.extend([
        f"{style} style",
        f"{lighting} lighting",
        f"{colors} color scheme",
        f"{camera_angle}",
        f"set in {environment}",
        f"aspect ratio {aspect_ratio}"
    ])
    
    final_prompt = ", ".join(prompt_parts)
    
    # Display results
    st.success("✅ Prompt Generated!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Generated Prompt")
        st.code(final_prompt, language="text")
        
        # Copy button (simulated)
        st.button("📋 Copy to Clipboard")
    
    with col2:
        st.subheader("Prompt Details")
        prompt_data = {
            "style": style,
            "lighting": lighting,
            "colors": colors,
            "camera_angle": camera_angle,
            "environment": environment,
            "aspect_ratio": aspect_ratio,
            "custom_elements": custom_prompt if custom_prompt else "None",
            "full_prompt": final_prompt
        }
        
        st.json(prompt_data)
        
        # Download JSON
        json_str = json.dumps(prompt_data, indent=2)
        st.download_button(
            "💾 Download JSON",
            json_str,
            file_name="image_prompt.json",
            mime="application/json"
        )

# Randomize button
if st.button("🎲 Randomize All Settings"):
    st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "🎨 AI Image Prompt Builder | Built with Streamlit"
    "</div>", 
    unsafe_allow_html=True
)