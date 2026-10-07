---
title: Adapting Generative Recommenders for Multi-Turn Interaction
title_zh: 面向多轮交互的生成式推荐适配框架 INTEGER
authors:
- Yu-Chen Den
- Zhi Rui Tam
- Yung-Yu Shih
- Shih-Hsin Wang
- Yun-Nung Chen
- Pu-Jen Cheng
- Eugene Yang
affiliations:
- National Taiwan University
- Johns Hopkins University
arxiv_id: '2610.08136'
url: https://arxiv.org/abs/2610.08136
pdf_url: https://arxiv.org/pdf/2610.08136
published: '2026-10-06'
collected: '2026-10-07'
category: GenRec
direction: 生成式推荐 · 多轮交互适配
tags:
- Generative Recommendation
- Conversational Recommendation
- Multi-turn Interaction
- Semantic ID
- DPO
one_liner: 通过路由令牌、历史重锚、行为回放实现生成式推荐多轮交互适配且不损失推荐精度
practical_value: '- 做对话式生成推荐时可复用「路由令牌+历史重锚」的解码逻辑，生成推荐前自动插入用户行为历史，复用原有生成式推荐的历史到Item映射，避免对话微调侵蚀原有推荐能力

  - 微调阶段可混合多轮对话数据、原推荐任务样本、通用指令数据，通过行为回放机制防止灾难性遗忘，无需额外模块化工具调用，单模型即可同时支持对话交互与商品推荐

  - 用户负反馈的商品替换场景可使用DPO做偏好优化，即使没有细粒度意图标注，也能实现被拒商品下推与相似商品召回，适合电商推荐的负反馈迭代场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐仅能基于固定用户交互历史生成结果，用户无法直接修正推荐偏差；直接给生成式推荐加对话微调会覆盖原有历史到商品的映射，出现对话能力与推荐精度互斥的问题。

### 方法关键点
- 新增`<hist>`路由令牌，模型自动判断当前轮次是闲聊还是生成推荐，无需外部路由模块
- 历史重锚机制：当模型输出`<hist>`后，推理侧自动插入用户行为历史和`<rec>`令牌，再通过前缀trie约束解码生成Semantic ID，还原原生成式推荐的输入格式
- 微调阶段混合多轮对话数据、原序列推荐样本、通用指令数据，通过行为回放保留原有推荐能力，搭配DPO优化用户负反馈后的商品替换效果

### 关键实验
在亚马逊Beauty、Toys两个公开电商数据集上，对比序列推荐、端到端对话推荐、工具调用式模块化三类基线：Beauty数据集上Hit@10达0.051，较最优基线提升13.3%，LLM打分的对话质量Conv.Q达4.77，显著优于模块化基线；Toys数据集上Hit@10达0.057，与最优基线持平，对话质量比纯对话推荐基线PECRS高0.2。

最值得记住的结论：对话应该作为生成式推荐的控制层，而非直接作为推荐的输入信号，才能同时保留原有推荐精度和新增的交互能力。
