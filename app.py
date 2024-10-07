import gradio as gr


def greet(name):
    return "Hello, " + name + "!"


with gr.Blocks() as demo:
    gr.Markdown("Welcome to your Gradio application!")

    name = gr.Textbox(label="Name", elem_id="name")
    greeting = gr.Textbox(label="Greeting", elem_id="greeting")
    button = gr.Button("Greet", elem_id="greet")
    button.click(fn=greet, inputs=name, outputs=greeting, api_name="greet")

demo.launch()
