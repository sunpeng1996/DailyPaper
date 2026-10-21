---
title: 'Asymmetric Looped Transformers: Fixed Global Representations for an Iterative
  Decoder'
title_zh: 非对称循环Transformer：面向迭代解码器的固定全局表征
authors:
- Cheng Liang
- Tengfei Zhang
- Wenjie DU
- Jianyu Wu
- Changlian Ma
- Shuchen Pu
- Ya Zhang
- Yanfeng Wang
- Zhouhan Lin
affiliations:
- Shanghai Jiaotong University
- University of Science and Technology of China
- Nanyang Technological University
- Nanjing University
arxiv_id: '2610.28489'
url: https://arxiv.org/abs/2610.28489
pdf_url: https://arxiv.org/pdf/2610.28489
published: '2026-10-20'
collected: '2026-10-21'
category: LLM
direction: LLM架构优化 · Looped Transformer
tags:
- Looped-Transformer
- KV-cache
- Layerwise-Learning-Rate
- Transformer-Architecture
- Reasoning
one_liner: 拆分上下文编码与循环状态优化，通过固定Global KV联合注意力提升Looped Transformer性能
practical_value: '- 做LLM4Rec/多轮推理Agent时，可复用非对称拆分设计：用户/物品上下文单趟编码生成固定Global KV，迭代阶段仅更新Local
  KV，降低KV cache开销同时保留上下文信息

  - 训练带参数共享的循环模块（如多步召回、多轮Agent决策）时，可直接复用重尾引导的分层学习率方法，无需手动调参即可提升训练稳定性与最终效果

  - 长序列推荐/多轮对话场景下，可复用Global+Local联合注意力机制，同时兼顾原始上下文语义与迭代中间状态，提升多步推理/决策的准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Looped Transformer采用全栈循环设计，将上下文构建与迭代状态优化耦合在同一循环计算中，未区分两者功能定位，导致上下文信息在多轮迭代中丢失，无法充分发挥循环深度带来的算力红利，训练不稳定且效果提升有限。
### 方法关键点
- 架构非对称拆分：将Transformer物理层对半分为单趟运行的因果编码器与权重共享的递归解码器，编码器输出映射为层粒度固定Global KV cache，跨所有迭代复用
- 全局-局部联合注意力：解码器每层在单个softmax下同时计算对固定Global KV与当前迭代生成的动态Local KV的注意力，无缝融合全局上下文与中间迭代状态
- 重尾引导分层学习率：基于权重矩阵的谱指数自适应分配不同模块的学习率，编码器与解码器按各自的谱统计特征自动调整学习率，无需手动设置模块间学习率比例
### 关键实验结果
在FineWeb-Edu数据集上从60M到1B四个规模训练，同等有效深度、训练token预算下对比Dense、Full Loop基线：135M、350M规模验证困惑度分别降低0.98、0.30；1B规模7个常识推理零-shot平均准确率从49.58%提升至50.85%，GSM8K微调准确率提升1.52个百分点；5倍Chinchilla训练预算下效果优势依然保持。
### 核心结论
循环Transformer的效率提升核心来自上下文编码与状态迭代的功能拆分，固定全局KV缓存+动态状态迭代的组合能以不到15%的额外开销同时提升训练效果与推理效率。
