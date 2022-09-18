
This directory inculdes our main implementation code. 


## File Structure
* **./CodeBert** - includes the code for **CodeBert**, which is downloaded from [Microsoft CodeXGLUE](https://github.com/microsoft/CodeXGLUE). 
* **./GPT2** - includes the code for **PyGPT2**, which uses the HuggingFace Library to invoke the [PyGPT2 Model](https://huggingface.co/SIC98/GPT2-python-code-generator).
* **./DeepAPI** - the code for the application of **DeepAPI**, which is downloaded from [DeepAPI](https://github.com/guxd/deepAPI)
* **./wrapper_model.py** - the wrapper model of the mentioned applications.
* **./xai** -the lib that includes the implementation of each explanation methods.
  * **./xai/lemna** - the implementaion of lemna.
  * **./xai/lime** - the implementaion of lime.
  * **./xai/codeexpgen** - the implementaion of our approach.
