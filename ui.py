import gradio as gr
import convo

# set a custom theme
theme = gr.themes.Default().set(
    body_background_fill="#1111111",
)

with gr.Blocks(theme=theme) as ui:
    with gr.Row():
        message = gr.Audio(source="microphone", type="filepath")
    with gr.Row():
        btn1 = gr.Button("Process Request")
    # with gr.Row():
    #     # audio_response = gr.Audio()
    with gr.Row():
        text_response = gr.Textbox(label="Transcript", max_lines=10)

    # with gr.Row():
    #     with gr.Column(scale=1):
    #         btn2 = gr.Button("Show Transcript")

    btn1.click(fn=convo.respond, inputs=message, outputs=text_response)
    # btn2.click(fn=convo.transcript, outputs=text_response)

ui.launch(server_port=8080)
