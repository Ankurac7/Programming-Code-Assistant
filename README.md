# Programming Code Assistant

This is a AI Programming Code Assitant built on top of [CodeLlama](https://ai.meta.com/blog/code-llama-large-language-model-coding/). CodeLlama is a large language model developed by Meta focussed to run and discuss code. CodeLlama is free for research and commercial use.

I have named this model as Jarvis,and the same has been deployed on Hugging Face Spaces and Gradio. [link](https://huggingface.co/spaces/Ankurac7/Programming_Code_Assistant_App)

## Local Setup
1. Create a virtual environment and install the necessary dependencies from `requirements.txt`.
2. Create the model in Ollama on your terminal at the project directory
    ```sh
    ollama create Jarvis -f modelfile
    ```
3. Run the model on terminal
    ```sh
    ollama run Jarvis
    ```
4. Run the model with the interface
    ```sh
    python app.py
    ```
| title                          | Programming_Code_Assistant |
| ------------------------------ | ------------------------------ |
| app_file                       | app.py                         |
| sdk                            | gradio                         |
| sdk_version                    | 4.21.0                         |

