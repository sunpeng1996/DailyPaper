---
title: You Really Didn't Get That? Benchmarking Social Pragmatic Inference for Indirect
  and Playful Chinese Online Comments
title_zh: 中文网络间接戏谑评论的社会语用推理能力测评基准
authors:
- Shiwei Hong
- Junjie Ma
- Emma Jiren Wang
- Ethan Z. Rong
- Siying Hu
- Haichang Li
- Ziying Wang
- Zhicong Lu
affiliations:
- George Mason University
- Virginia Tech
- University of Toronto
- City University of Hong Kong
- Duke Kunshan University
arxiv_id: '2609.04384'
url: https://arxiv.org/abs/2609.04384
pdf_url: https://arxiv.org/pdf/2609.04384
published: '2026-09-03'
collected: '2026-09-08'
category: Eval
direction: LLM评测 · 中文语用理解
tags:
- LLM-Evaluation
- Pragmatic-Inference
- Chinese-UGC
- Benchmark
- Natural-Language-Understanding
one_liner: 构建含4735条人工验证样本的中文网络评论语用推理基准 测评8款LLM的语义理解性能
practical_value: '- 电商评论、社媒UGC的情感/语义理解模块可参考本基准的「上下文+多干扰项对比」训练范式，提升反讽、玩梗类内容的识别准确率

  - 直播弹幕、用户评论的实时审核/用户偏好建模场景，可复用基准的难例构造方法优化LoRA微调的训练数据集

  - 电商导购Agent的用户意图理解模块，可引入本基准的评测指标做兜底校验，降低对用户间接表达的误判率'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有LLM语用能力评测多围绕预设类别构造样本，无法反映模型对真实场景下带上下文的中文网络间接、戏谑类评论的实际理解能力，这类内容广泛存在于社媒、电商UGC中，误判会直接影响用户建模、内容审核等模块效果。
### 方法关键点
从20万+公开中文社媒交互记录中筛选构造4735条人工验证的诊断样本，每条包含目标评论、对应上文上下文、合理干扰选项；采用leave-writer-out范式，测评8款LLM分别作为问题生成器与解答器的性能。
### 关键结果
最强模型的leave-writer-out准确率仅为81.42%，8款模型平均准确率68.70%，远低于人类水平的90.8%；模型大多能识别宽泛的讽刺/戏谑属性，但普遍误判其具体表达机制或交互意图。
