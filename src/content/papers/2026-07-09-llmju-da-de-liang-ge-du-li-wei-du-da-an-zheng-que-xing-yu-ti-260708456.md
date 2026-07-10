---
title: 'Two Axes of LLM Abstention: Answer Correctness and Question Answerability'
title_zh: LLM拒答的两个独立维度：答案正确性与问题可回答性
authors:
- Benedikt J. Wagner
affiliations:
- City, University of London
arxiv_id: '2607.08456'
url: https://arxiv.org/abs/2607.08456
pdf_url: https://arxiv.org/pdf/2607.08456
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: LLM风险控制 · 拒答策略优化
tags:
- LLM Abstention
- Hallucination Detection
- Risk Control
- Hidden State Probing
- Selective Prediction
one_liner: 将LLM拒答拆为两个独立维度，提出带风险认证的双阈值策略性能远超单置信度阈值方案
practical_value: '- 电商智能客服、商品问答等LLM应用的拒答模块不要只用单输出置信度阈值，拆分「问题可回答性」「答案正确性」两个独立维度评估，可分别控制回答虚假预设问题、答错可答问题两类不同业务风险

  - 做用户问题虚假前提检测（如用户提问自带错误商品认知）时，不要依赖prompt让模型自检，输出侧elicitation效果仅接近随机，直接提取LLM hidden
  state训练探针，检测AUROC可比输出信号高15-21个百分点

  - 上线LLM问答模块时可复用本文的双风险预算认证框架，分别为两类错误设置可接受的上线阈值，8B规模模型下正确答案覆盖率可达0.75，是单置信度阈值方案的2倍以上'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM拒答普遍采用单置信度阈值方案，混淆了两类完全不同的失败模式：对可回答问题输出错误答案，以及回答本不该响应的不可答/带虚假预设问题，两类错误的业务影响差异极大，无法通过单阈值实现独立风险控制。

### 方法关键点
- 将拒答问题形式化为三类分类：正确可答(C)、错误可答(W)、不可答(U)，对应两个独立评估轴：正确性轴（区分C/W）、可回答性轴（区分C+W/U）
- 分别用输出置信度作为正确性信号、hidden state探针作为可回答性信号，训练等容量的L2正则化逻辑回归读头
- 提出双阈值因子化拒答策略，同时对两个轴设置阈值，用二项分布上界分别对「回答不可答问题率$R_U$」和「答错可答问题率$R_W$」做独立风险认证，保证上线风险可控

### 关键实验结果
测试覆盖Gemma2、Qwen2.5、Llama3.1三个模型家族2B-14B的5个指令微调模型，在SelfAware构造基准、CREPE真实用户虚假预设基准上验证：
- hidden state读取可回答性的AUROC达0.97-0.99，远高于输出置信度的0.54-0.67；在CREPE真实场景下，hidden state检测虚假预设的AUROC为0.69-0.78，比所有输出侧信号高15-21个百分点
- 在$α_U=0.15$、$α_W=0.5$的风险预算下，8B模型双阈值策略的正确答案覆盖率达0.75，是单置信度阈值（0.31）的2倍以上；14B模型下双阈值策略是唯一能通过风险认证的方案

**最值得记住的一句话**：LLM拒答不是单一问题，输出置信度仅能判断回答是否成功，无法判断问题是否应该被回答，拆分两个维度做独立风险控制是上线可靠LLM应用的核心。
