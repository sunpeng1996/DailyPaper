---
title: Large Language Models with At Most One Spike per Neuron
title_zh: 每个神经元至多发放一个脉冲的低能耗大语言模型
authors:
- Zhuoya Zhao
- Parsa Omidi
- Aref Jafari
- Richard Naud
affiliations:
- Huawei
- University of Ottawa
arxiv_id: '2609.05151'
url: https://arxiv.org/abs/2609.05151
pdf_url: https://arxiv.org/pdf/2609.05151
published: '2026-09-04'
collected: '2026-09-07'
category: LLM
direction: 低能耗大语言模型 · 脉冲神经网络
tags:
- SNN
- TTFS
- Energy-efficient LLM
- Neuromorphic Computing
- Spiking LLM
one_liner: 提出参考式TTFS编码实现全链路脉冲LLM，规模达15亿参数，能效优于速率编码脉冲基线
practical_value: '- 端侧推荐/Agent部署参考：该单脉冲架构的超高能效可直接复用在算力受限的端侧场景（比如IoT设备个性化推荐、离线智能导购Agent），降低端侧LLM推理的功耗要求

  - LLM稀疏化优化可复用组件映射思路：将embedding、LayerNorm、Attention等核心LLM组件转换为稀疏计算单元的设计方法，可迁移到常规云侧LLM的推理稀疏化优化，降低推理成本

  - 任务选型参考：脉冲LLM在分类、常识判断、语义匹配类任务上性能接近常规ANN，能效收益最高；生成类任务（如文案生成、多轮对话）目前仍有明显精度gap，业务选型可直接参考该结论'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
常规LLM推理能耗高，脉冲神经网络（SNN）的事件驱动特性天然适配低功耗场景，但传统Time-to-First-Spike（TTFS）编码每个神经元最多发放一个脉冲，稀疏性极强却仅能适配简单MLP结构，无法支持LLM的嵌入、层归一化、注意力等核心组件，制约了脉冲LLM的落地。

### 方法关键点
- 提出参考式R-TTFS编码，引入中间参考时间点实现正负值编码，通过shift-ReLU线性区建立TTFS层与常规ANN层的精确映射
- 完成LLM四大核心组件的TTFS适配：嵌入层用one-hot脉冲触发查表，LayerNorm拆分为均值、减法、平方、开方近似等7步脉冲运算，注意力用膜电位加权脉冲时序完成QKV计算，Dropout随机丢弃脉冲神经元
- 支持端到端训练全TTFS架构的BERT和GPT-2，无需ANN转SNN的近似转换

### 关键实验结果
- GLUE基准上，TTFS-BERT Large平均得分82.3，仅比全精度BERT低3个点，比早期脉冲BERT高17.2分
- 1.5B参数的TTFS-GPT-2 XL在常识推理任务上平均准确率49.5，和同规模GPT-2的51.6基本持平；语言建模困惑度26.6，比SpikeGPT低33%
- 脉冲相关能耗仅0.8Tr/神经元/推理，比速率编码的SpikeLM低33%，比SpikingBERT低75%

### 核心结论
脉冲LLM在非生成类任务上已经具备落地可行性，是未来端侧低功耗大模型的核心技术方向之一
