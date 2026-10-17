---
title: 'Learning to Read Out: Unembedding Dynamics in Language Model Pretraining'
title_zh: 大语言模型预训练阶段Unembedding（读头）的演化动力学研究
authors:
- Matteo He
- William F. Shen
- Alex Iacob
- Andrej Jovanovic
- Xinchi Qiu
- Nicholas D. Lane
affiliations:
- University of Cambridge
- Flower Labs
- Isomorphic Labs
arxiv_id: '2610.21025'
url: https://arxiv.org/abs/2610.21025
pdf_url: https://arxiv.org/pdf/2610.21025
published: '2026-10-13'
collected: '2026-10-17'
category: LLM
direction: LLM预训练机制 · 读头演化分析
tags:
- LLM Pretraining
- Unembedding
- Sparse Autoencoder
- Crosscoder
- Mechanistic Interpretability
one_liner: 提出参数轨迹交叉编码方法，揭示LLM隐层信息编码早于读头表达的时间差
practical_value: '- 电商/行业场景扩展自定义词表（新增商品ID、行业术语）时，可单独给Unembedding层设置更高学习率，加快适配速度且几乎不影响最终模型效果

  - 小模型预训练/冷启动场景，不用仅依赖输出效果判断模型能力，可通过线性探针探测隐层已编码但未表达的能力，提前预判模型潜力，节省训练资源

  - LLM4Rec生成式推荐场景中，若隐层已能编码用户偏好但输出item相关性差，可优先优化Unembedding层的映射关系，无需重新训练全量模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
过往LLM能力演化研究均通过输出token判断能力获得时间，但输出依赖Unembedding（读头）矩阵，而读头本身也在预训练过程中持续更新，导致能力获取时间的评估存在混淆，无法区分是隐层真的未学到对应能力，还是读头未学会将编码信息映射为输出token。

### 方法关键点
- 提出**参数轨迹交叉编码**：直接对所有预训练checkpoint的读头权重拟合全局稀疏字典，无需激活数据或标注，即可跨checkpoint追踪读头的演化过程
- 设计读头交换实验：固定某checkpoint的隐层，用其他checkpoint的读头解码，分离隐层编码和读头表达对输出的贡献
- 用线性探针探测隐层的信息可用性，与原生读头的输出表达准确率做对比，量化二者的时间差

### 关键结果
- Pythia系列模型的读头重组发生在预训练极早阶段（仅0.4%~1.1%总训练步），此时WordNet语义分类已可从读头行中解码
- 隐层信息编码远早于读头表达：Pythia-6.9B在512训练步时，隐层对主谓一致任务的探针准确率已达91%，但原生读头准确率仅为50%（随机水平）
- 单独提升读头的学习率可让读头发育提前、时间差显著缩小，对最终预训练损失的影响小于0.06 nats

### 核心结论
LLM预训练中，表征学习和表达学习是两个独立过程，早期输出效果差不代表隐层没有学到对应能力。
