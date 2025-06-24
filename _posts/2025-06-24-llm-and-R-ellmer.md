---
title: "Chat with LLMs on your R environment"
author: "[Ozancan Ozdemir](mailto:ozancanozdemir@gmail.com)"
tags: [r]
categories: [r]
author_profile: true  
layout: single         
read_time: true
---

## Chat with LLM's on R

LLM provides many advantages to the users, especially for coding. Once user had to switch the windows from the coding environment to the browser to search for the solution. But now, thanks to the newly advancements, users can chat with the LLM and get the solution for their queries on the same coding environment in R.

There are several packages publicly available in that manner on CRAN and GitHub such as `chattr`, `tidyllm` etc. Among these packages, `ellmer` is the one of most comprehensive one such that you can chat with almost all languages available.

`ellmer` is a package that creates an interface to chat with different language models. The full list alongside the key function is given below.

-   Anthropic’s Claude: chat_claude().
-   AWS Bedrock: chat_bedrock().
-   Azure OpenAI: chat_azure().
-   Databricks: chat_databricks().
-   DeepSeek: chat_deepseek().
-   GitHub model marketplace: chat_github().
-   Google Gemini: chat_gemini().
-   Groq: chat_groq().
-   Ollama: chat_ollama().
-   OpenAI: chat_openai().
-   OpenRouter: chat_openrouter().
-   perplexity.ai: chat_perplexity().
-   Snowflake Cortex: chat_snowflake() and chat_cortex_analyst().
-   VLLM: chat_vllm().

In this tutorial, I'll summarize the steps of using Gemini in R using `ellmer` package since Google allows to use an api key for free.

There is no free account for API keys of OpenAI, the service costs by amount of data that you use. Thus, I am proceeding with Google Gemini in this tutorial, however I also provide the funcitons and instructions that you can also use other language models.

### **Step 1**: Install the package from CRAN

```         
install.packages("ellmer")
```

```{r}
library(ellmer)
```

### **Step 2**: Set Up your Gemini Api Key

In order to get an api key from Google Gemini you need to create an account on Gemini first, which is most probably something you have. Then, you can visit [Google AI Studio](https://aistudio.google.com/app/apikey) and create your api key for **free of charge.**

![image](https://github.com/user-attachments/assets/b608e62c-aad2-4a4f-91df-5250f5a0e8c0)



After your api key, you employ `Sys.setenv()` function to set your api key as follows.

```         
google_api_key = "your_api_key"
Sys.setenv(GOOGLE_API_KEY = google_api_key)
```

If you would like to use other language models, the syntax that you need to use is given below.

-   For Claude models

```         
Sys.setenv(ANTHROPIC_API_KEY = "YOUR-ANTHROPIC-API-KEY")
```

-   For OpenAI

```         
Sys.setenv(OPENAI_API_KEY = "YOUR-OPENAI-API-KEY")
```

-   For Google Gemini

```         
Sys.setenv(GOOGLE_API_KEY = 'YOUR-GOOGLE-API-KEY')
```

-   For Mistral

```         
Sys.setenv(MISTRAL_API_KEY = "YOUR-MISTRAL-API-KEY")
```

-   For groq

```         
Sys.setenv(GROQ_API_KEY = "YOUR-GROQ-API-KEY")
```

-   For Perplexity

```         
Sys.setenv(PERPLEXITY_API_KEY = "YOUR-PERPLEXITY-API-KEY")
```

### **Step 3**: Chat with your model.

After setting up your enviroment with your api key, you should create a chat object by using a function that is related to your model. In this tutorial, I'll use Google Gemini, thus I'll use `chat_gemini()` function.

If I used OpenAI, I would use `chat_openai()` function.

There are three ways of getting a response from the model for your query, but these three ways have one common point; you should create a chat object first.

```{r}
chat <- chat_gemini()
chat
```

With this function, you activate your language model to chat. If you would like to start to get response for your query, you should call the activated model by ```$```
function. 

```{r}
chat$chat("how to create a heatmap in ggplot2", echo = FALSE)
```

### **Step 4**: Get your answers from an interface.

As you may see above, `chat` object provides an answer on your R console, which is not in tidy format so that difficult to follow. If you would like to get your answer in a tidy format, you can use `live_browser` function.

Also see [`live_console()`](https://ellmer.tidyverse.org/reference/live_console.html)

`live_browser()` function opens an interactive dashboard on your viewer screen and enables you to chat with your language as on your browser. To be able to use this function, it is enough to insert your chat object as input to the function as given below.

\``live_browser(chat)`

![image](https://github.com/user-attachments/assets/86b2814d-4948-4630-99c8-772040242a40)


Then, write your query and get your answer.

![image](https://github.com/user-attachments/assets/fe9e49f4-5fdc-4d77-a42b-13df9b27fdc7)


### **Step 5**: Close your chat object

To close your browser, you may either press Esc or click on the red stop button on your viewer screen. 
