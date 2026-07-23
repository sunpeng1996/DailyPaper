---
title: Understanding the Impact of Linguistic Realization Choices on LLM Stance with
  Causal Tracing
title_zh: 语言表达结构选择对LLM立场判断的影响分析及因果定位
authors:
- Langchen Huang
- Sebastian Padó
- Franziska Weeber
affiliations:
- Institute for Natural Language Processing, University of Stuttgart
arxiv_id: '2607.20115'
url: https://arxiv.org/abs/2607.20115
pdf_url: https://arxiv.org/pdf/2607.20115
published: '2026-07-22'
collected: '2026-07-23'
category: LLM
direction: LLM鲁棒性 · 因果追踪分析
tags:
- LLM Robustness
- Causal Tracing
- Activation Patching
- Stance Detection
- Linguistic Structure
one_liner: 针对6类语义控制改写场景，用激活补丁定位LLM立场偏移核心作用模块为解码器中后层
practical_value: '- 做LLM驱动的用户意图识别、商品评价极性判断、合规审核等任务时，需提前做句式扰动测试，避免语义等价的不同表达导致输出漂移

  - 针对语义不变性要求高的业务场景微调LLM时，可针对性对解码器中后层增加监督约束，提升模型对等价表达的鲁棒性

  - 激活补丁的因果定位方法可直接复用在业务LLM的bad case根因分析上，快速定位错误输出对应的模型模块，降低调试成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM输入鲁棒性研究多聚焦词汇层面改写，忽略句法结构选择对输出的影响，语义等价的不同表达常导致LLM判断偏移，且缺乏对这类偏移内部作用机制的定位方法。
### 方法关键点
以立场判断为语义敏感测试场景，构建6类受控语言改写数据集（含语义保留、语义反转两类），在4个开源大模型上测试立场稳定性；采用激活补丁技术，将原句激活值替换进改写句的前向传播过程，定位影响立场偏移的核心模块。
### 关键结果
语义保留和语义反转的改写都会引发LLM立场不稳定；解码器中后层、尤其是prompt最后位置的Transformer块输出对恢复原立场分布的信号最强，是立场偏移的核心作用区域。
