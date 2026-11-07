---
title: 'Tools Need Not Speak in Text: Latent Context Compression for Agents'
title_zh: Coca-Cola：面向LLM Agent的隐向量上下文压缩框架
authors:
- Yuetong Liu
- Zhehao Zhou
- Yitong Zhang
- Haorui Chen
- Jia Li
affiliations:
- Tsinghua University
- Tsinghua AI Agent Group
arxiv_id: '2611.06500'
url: https://arxiv.org/abs/2611.06500
pdf_url: https://arxiv.org/pdf/2611.06500
published: '2026-11-03'
collected: '2026-11-07'
category: Agent
direction: Agent 工具输出隐向量压缩优化
tags:
- LLM Agent
- Context Compression
- Latent Token
- Action Alignment
- Efficient Inference
one_liner: 将工具输出压缩为隐向量注入Agent，大幅降本同时提升任务性能
practical_value: '- 电商搜索/导购Agent、多步工具调用场景可直接复用动作保持训练范式：无需重构工具输出全文，仅对齐全量/压缩观测下的Agent下一步动作分布，即可在高压缩比下保持决策准确率，大幅降低token成本与推理延迟

  - 落地时可采用「轻量编码器+LoRA微调+隐向量适配器」架构，压缩后的隐向量直接映射到目标Agent输入嵌入空间，无需修改Agent主模型，改造成本极低

  - 可根据业务对成本/效果的容忍度调整隐向量token数：128个隐token即可实现70%+压缩比，同时性能不降反升，平衡开销与效果

  - 压缩时需拼接当前任务目标、历史推理轨迹作为条件，相比仅压缩观测数据可提升3~5个点的EM准确率，适合多步推理的复杂Agent场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent多步交互中工具输出占上下文比例最高可达96.7%，传统文本剪枝、摘要压缩受限于离散token语义连贯性要求，压缩比上限低，既带来高额token成本，冗余信息还会分散Agent注意力，导致推理效果下降。

### 方法关键点
- 突破“工具输出必须是显式文本”的固有假设，提出Coca-Cola连续隐向量压缩框架，直接将工具输出编码为连续隐向量，突破文本压缩的容量限制
- 架构由上下文感知编码器（轻量小模型+LoRA微调）+ 隐向量适配器组成，压缩后的隐向量直接映射到目标Agent的输入嵌入空间，Agent无需修改即可直接使用
- 采用**Action-Preserving Training**策略：冻结目标Agent，对齐全量观测和压缩隐向量下的Agent下一步动作分布，仅优化编码器和适配器参数，保证保留决策关键信息，无需重构原工具文本

### 关键实验结果
在NQ、TriviaQA、2Wiki、HotpotQA共4个搜索QA基准上，对比无压缩基线、LongLLMLingua、LLM摘要、ICAE等主流压缩方法：
- token总消耗降低70.01%~89.24%，端到端推理耗时下降24.45%~55.97%
- 在8个模型-数据集组合中的6个取得最优EM/F1，最高较无压缩基线提升133.64%的EM准确率

### 核心结论
Agent与工具的交互不需要依赖人类可解释的显式文本，只需传递足够支撑后续决策的隐向量信息即可
