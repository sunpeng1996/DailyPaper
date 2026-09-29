---
title: Can Generative Retrievers Learn Semantic IDs Without Forgetting How to Speak?
title_zh: 生成式检索学习语义ID时保留原生语言能力的SpeakGR框架
authors:
- Junchen Fu
- Kleomenis Katevas
- Vandana Rajan
- Sofía Celi
- Hamed Haddadi
affiliations:
- University of Glasgow
- Brave
arxiv_id: '2609.35430'
url: https://arxiv.org/abs/2609.35430
pdf_url: https://arxiv.org/pdf/2609.35430
published: '2026-09-28'
collected: '2026-09-29'
category: GenRec
direction: 生成式检索 · Semantic ID训练优化
tags:
- Generative Retrieval
- Semantic ID
- LLM Fine-tuning
- Catastrophic Forgetting
- Regularization
one_liner: 提出双目标训练框架SpeakGR，使生成式检索学习Semantic ID时保留LLM原生语言生成能力
practical_value: '- 做Semantic ID类生成式推荐/检索业务时，可直接复用SpeakGR双目标训练范式，单模型同时支持召回+自然语言回复，无需部署两套模型，降低推理资源开销

  - 语言保留正则化trick可迁移：使用冻结原模型的on-policy distillation+forward KL约束文本词汇分布，比离线回放、权重合并方案的检索-语言保留trade-off更优

  - 自适应权重调整策略可复用：根据观测到的语言漂移动态调整正则化强度，无需手动调试固定权重，降低调参成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式检索通过生成Semantic ID实现端到端检索，但仅面向检索的SFT会让LLM过拟合SID预测，严重扭曲原生语言分布，无法同时支持检索后的自然语言交互（如召回商品后回答用户追问、给出解释）。现有生成式检索方案普遍只关注检索效果，忽略语言能力遗忘问题，也无对应的优化框架。

### 方法关键点
- 双目标训练框架SpeakGR，同时优化SID生成的交叉熵损失、语言保留正则化损失
- 语言保留正则化采用on-policy distillation思路：当前模型生成文本前缀，冻结的原LLM输出相同前缀的下一词分布，用原文本词汇上的forward KL约束学生模型的语言分布漂移
- 自适应版本Adaptive SpeakGR：根据观测到的语言漂移的指数移动平均，动态调整正则化项权重，自动平衡检索效果和语言保留

### 关键结果
在MS MARCO、NQ两个检索数据集，Qwen3-0.6B/1.7B、Gemma-3-1B-IT三个底座上验证：
- 相比纯检索SFT，SpeakGR在MS MARCO上降低WikiText-2正向KL 81.3%~93.8%，NQ上降低81.2%~85.2%，检索效果基本持平
- Adaptive SpeakGR在5/6的实验设置中检索效果优于固定权重的SpeakGR，同时语言漂移远低于纯SFT
- 对比离线回放、ORBIT权重合并等基线，SpeakGR在检索效果和语言保留的trade-off上表现更优

> 最值得记住的结论：生成式检索/推荐的Semantic ID训练无需牺牲LLM原生语言能力，通过目标层正则化即可实现单模型同时支持检索和自然交互，降低系统部署成本
