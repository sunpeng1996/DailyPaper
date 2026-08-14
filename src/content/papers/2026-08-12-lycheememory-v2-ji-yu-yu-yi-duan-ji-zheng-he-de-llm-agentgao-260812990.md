---
title: 'LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level
  Consolidation'
title_zh: LycheeMemory V2：基于语义段级整合的LLM Agent高效长期记忆框架
authors:
- Dongfang Li
- Zixuan Liu
- Junmai Wang
- Jiahe Huang
- Fuhao Li
- Bonian Jia
- Baotian Hu
- Min Zhang
affiliations:
- 哈尔滨工业大学（深圳）
arxiv_id: '2608.12990'
url: https://arxiv.org/abs/2608.12990
pdf_url: https://arxiv.org/pdf/2608.12990
published: '2026-08-12'
collected: '2026-08-14'
category: Agent
direction: Agent长时记忆 · 语义段级整合优化
tags:
- LLM Agent
- Long-term Memory
- Semantic Segmentation
- Memory Consolidation
- Retrieval Augmentation
one_liner: 用语义段级替代逐轮记忆整合，大幅降低LLM调用成本同时提升长时记忆问答精度
practical_value: '- 电商客服/个性化导购Agent的记忆系统可替换原有逐轮记忆更新逻辑，采用语义段级整合方案，通过embedding做语义边界检测，无需每轮对话调用大模型提取记忆，可降低80%左右的记忆构造token成本

  - 用户长期偏好建模可参考其结构化记忆记录设计，将用户交互历史抽取为带实体、主题、时间戳、溯源信息的结构化记录，支持多维度索引检索，大幅提升多跳推理、时序类需求的准确率

  - RAG/记忆检索模块可复用其单步查询规划+多路径召回+RRF融合的方案，无需实现迭代多轮检索逻辑，在提升召回准确率的同时不会增加查询侧大模型开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent长时记忆多采用逐轮eager整合机制，每轮交互都调用LLM提取/更新记忆，随对话规模增长构造token成本快速累积；粗粒度摘要压缩虽能降本，但易丢失细粒度上下文证据，而扩大检索上下文、多跳LLM推理等优化又会将开销转移到查询侧，无法兼顾精度与全链路成本。

### 方法关键点
- 在线语义分割：基于对话embedding的语义惊讶度、内聚度下降、token/轮数压力计算边界阈值，将多轮对话聚合为语义连贯的段，仅在段结束时调用1次LLM编码，大幅降低编码频率
- 段级记忆编码：每个段结合少量跨段消歧上下文，编码为带类型、实体、主题、归一化时间、溯源链接的上下文无关记忆记录，输出轻量消歧状态维持段间一致性
- 结构化索引：基于记录元数据自动构建实体、主题、时序、事件帧等多维度索引，无额外LLM开销
- 多路检索：仅调用1次LLM做查询规划生成多检索路径，并行召回向量、结构化索引、原始对话片段，经RRF融合得到证据上下文，无迭代检索开销

### 关键结果
在LoCoMo、LongMemEval-S两个长时记忆基准上测试，对比Mem0、A-Mem、TiMem等SOTA系统：使用GPT-4.1-Mini时，LoCoMo准确率达89.22%、LongMemEval-S达92.20%，均为当前SOTA；相比A-Mem，LoCoMo构造token降低86.0%、LongMemEval-S降低75.9%，同时查询token分别降低27.9%、42.6%，无查询侧开销上升。

> 最值得记住：长时Agent记忆的精度-成本权衡不仅取决于保留什么信息，还取决于整合的粒度
