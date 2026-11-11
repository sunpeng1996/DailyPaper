---
title: 'onóna: Twin Embeddings with Tied Unembeddings'
title_zh: 《onóna：支持权重共享的双嵌入绑定输出头语言模型架构》
authors:
- Cheng Luo
- Xinnan Dai
- Zhongzhu Zhou
- Zefan Cai
- Ruijie Zhu
- Tianyu Zhang
- Junjie Hu
affiliations:
- Independent Researcher
- Michigan State University
- Together AI
- University of Wisconsin–Madison
- University of California, Santa Cruz
arxiv_id: '2611.10556'
url: https://arxiv.org/abs/2611.10556
pdf_url: https://arxiv.org/pdf/2611.10556
published: '2026-11-06'
collected: '2026-11-11'
category: LLM
direction: 大语言模型 · 嵌入与输出头优化
tags:
- WeightTying
- Embedding
- SoftmaxBottleneck
- LanguageModel
- EfficientInference
one_liner: 保留输入输出权重共享的前提下，通过双嵌入加token级门控提升语言模型输出表达能力
practical_value: '- 推荐系统的用户/物品ID嵌入层可直接借鉴双嵌入平均方案，在不增加推理输入侧开销的前提下缓解embedding塌陷问题，提升召回/排序模型的表达能力

  - 生成式推荐/Agent所用的小尺寸垂直LLM可复用onóna架构，仅增加少量参数即可降低预训练困惑度、提升下游任务准确率，温度1无截断采样场景下可将额外投影开销降为0

  - 多模态推荐的文本/图像token映射层可借鉴token级门控混合策略，针对不同token类型自适应分配输出权重，无需额外上下文计算即可提升分布拟合效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
常规权重绑定方案通过共享输入嵌入和输出头矩阵大幅降低LLM参数量，但仅用单softmax输出头存在秩上限约束（softmax瓶颈），限制了多模态下一个token分布的拟合能力；而现有方案要么放弃权重共享增加大量参数，要么混合多上下文单表输出效果不佳，亟需兼顾参数效率和表达能力的优化方案。
### 方法关键点
- 双绑定表设计：维护A、B两个形状相同的嵌入表，输入侧取两表平均作为Transformer输入，完全不改动原有Transformer主体架构
- 输出混合策略：输出层分别用A、B表计算两个softmax分布，基于当前输入token的平均嵌入计算门控值，自适应混合两个分布的结果
- 推理优化：门控值可全vocabulary预计算，输入侧直接合并为平均表，温度1无截断采样时仅需计算单表投影即可得到准确采样结果
### 关键实验结果
在ClimbMix数据集上训练142M、330M、1B三个尺寸的Qwen3风格Decoder，对比单绑定表基线，12组对比中11组降低验证集损失，10组提升8个下游任务平均准确率；142M Dense模型验证损失降低0.0285 nats，LAMBADA PPL降低4，8任务平均准确率提升1.38个百分点；仅1B MoE模型损失略涨但下游准确率仍有提升。
### 核心结论
双嵌入的输入输出协同优化增益远高于单独优化输入或输出侧，在小尺寸垂直模型上的性价比高于单纯增加Transformer层数。
