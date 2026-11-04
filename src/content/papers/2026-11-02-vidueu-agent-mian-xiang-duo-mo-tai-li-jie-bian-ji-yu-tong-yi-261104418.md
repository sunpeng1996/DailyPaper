---
title: 'VidUEU-Agent: A Data-Curation Agent for Multimodal Understanding, Editing,
  and Unified Tasks'
title_zh: VidUEU-Agent：面向多模态理解、编辑与统一任务的数据生成Agent
authors:
- Tengju Ru
- Weitong Lian
- Zecong Tang
- Lingyi Meng
- Haoran Li
- Zhejun Cui
- Yichen Zhu
- Hangshuo Cao
- Qi Kang
- Yechi Liu
affiliations:
- Zhejiang University
- The University of Hong Kong
- Institute of Automation, Chinese Academy of Sciences
- Huawei Technologies Ltd.
arxiv_id: '2611.04418'
url: https://arxiv.org/abs/2611.04418
pdf_url: https://arxiv.org/pdf/2611.04418
published: '2026-11-02'
collected: '2026-11-04'
category: Agent
direction: 多模态数据生成 · Agent自动化流水线
tags:
- Multimodal Agent
- Data Curation
- Instruction Tuning
- Video Processing
- Synthetic Data
one_liner: 基于四阶段Agent流水线自动从原始视频生成多模态指令数据并支持下游反馈自主迭代
practical_value: '- 多模态内容生成场景可复用四阶段数据处理流水线：全局感知过滤低质内容→关键帧/多模态信号挖掘→结构化元数据构建→分场景指令数据生成，大幅降低人工标注成本，可直接用于电商商品短视频自动化标注、商品图文生成训练数据构建等场景

  - 可复用自主数据迭代机制：基于下游模型训练效果反馈动态调整数据分布、采样权重、过滤规则，适合电商推荐/搜索场景下针对长尾场景、低效果任务定向补充训练数据，提升下游模型迭代效率

  - 多模态数据质量控制可复用三级Gate过滤+证据引用机制：通过多轮VLM校验、规则过滤、要求生成样本引用原始信号ID，大幅降低生成数据的hallucination率，适合电商场景下商品描述、卖点生成等对数据事实性要求高的场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前统一多模态模型（UMM）发展受限于高质量指令数据的稀缺，人工标注成本极高；原始视频是海量多模态知识来源，但冗余、噪声大、非结构化，现有方法无法同时生成覆盖理解、编辑、统一任务的高质量指令数据，制约多模态模型全能力提升。

### 方法关键点
- 四阶段流水线：①全局感知：拆分视频为镜头，生成镜头/章节/视频三级摘要，过滤低质镜头；②关键帧挖掘：间隔采样帧后做质量过滤，结合工具信号打分，用加权设施位置贪心算法选高信息量、低冗余的关键帧；③元数据构建：整合关键帧、多模态信号、帧间变迁、片段摘要生成结构化元数据，做事实性校验；④指令数据生成：过滤低质元数据后按任务类型路由，匹配模板生成覆盖理解、编辑、统一三类任务的指令样本，要求样本引用原始信号ID保障可追溯性
- 自主迭代机制：基于下游模型训练效果反馈，动态调整视频采样偏好、关键帧预算、任务分布，优化数据质量与平衡性

### 关键结果
基于8268条公开/网络视频生成VidUEU-100K数据集，含40K理解、30K编辑、30K统一任务样本。LoRA微调InternVL3-8B后，MMDU得分从53.1提升到61.1，MME从2308提升到2369.3；微调Bagel后，GEdit-Bench编辑综合得分从6.527提升到6.951，WEAVEbench统一任务得分从0.446提升到0.501；经过4轮自主迭代后，三类任务得分均实现稳定上涨。

**最值得记住的一句话**：基于Agent的自动化数据生成+下游反馈迭代的范式，是大幅降低多模态模型训练数据成本、定向提升模型能力的可行路径
