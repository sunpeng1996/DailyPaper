---
title: 'UltraX: Refining Pre-Training Data at Scale with Adaptive Programmatic Editing'
title_zh: UltraX：基于自适应程序化编辑的大规模预训练数据精炼框架
authors:
- Xinlong Zhao
- Dongsheng Liu
- Hengyu Zhao
- Zixuan Fu
- Zheng Wang
- Jie Cai
- Jie Zhou
- Qiang Ma
- Xuanhe Zhou
- Xu Han
affiliations:
- Peking University
- ModelBest Inc
- Tsinghua University
- Shanghai Jiao Tong University
arxiv_id: '2607.08646'
url: https://arxiv.org/abs/2607.08646
pdf_url: https://arxiv.org/pdf/2607.08646
published: '2026-07-09'
collected: '2026-07-10'
category: Training
direction: 大模型预训练 · 数据质量优化
tags:
- LLM Pre-training
- Data Curation
- Programmatic Editing
- Function Calling
- Data Efficiency
one_liner: 基于增删改完整函数调用空间实现大规模预训练数据高效高质量精炼
practical_value: '- 垂直领域LLM（如电商导购/Agent决策小模型）预训练时，可复用UltraX的轻量函数调用精炼架构，将大模型的语料清洗能力蒸馏为小模型，比直接用大模型端到端重写语料的成本降低80%以上，同时避免幻觉

  - 处理大规模电商/广告爬取语料（如商品详情、用户评论、竞品文案）时，可直接复用其增删改完整操作空间、滑动窗口预测+全局聚合的执行逻辑，既删去广告、水印等噪声，又保留有效语义信息，提升语料密度

  - 做数据质量分层时可参考其高低质数据分治策略：低质长尾语料用激进编辑策略去噪，高质头部语料用保守保留策略避免过编辑，最大化有效训练信号'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Scaling Law下预训练数据存量接近物理上限，性能增益边际递减，核心优化方向从数据扩容转向数据质量提升。现有数据精炼方法存在明显缺陷：规则法依赖固定启发式，无法处理实例级差异；大模型端到端重写质量高但推理成本高、吞吐低，无法适配大规模预训练语料处理需求；已有的程序化编辑框架存在函数空间不完整、监督质量差、执行不稳定等问题，无法平衡精炼质量和处理效率。
### 方法关键点
- 构建完整编辑函数空间，新增插入操作，覆盖保留全文档、删除全文档、删除指定行、局部字符串替换、指定位置插入5类操作，支持细粒度实例级编辑
- 设计可靠程序监督pipeline：先通过数据集自适应Prompt优化引导专家大模型生成高质量端到端精炼文本，再通过行对齐映射、动态上下文替换将原始-精炼文本对转换为结构化程序监督，配合低置信样本过滤、操作组合比例控制采样提升监督质量
- 推理阶段采用滑动窗口预测、全局操作聚合、系统后处理校验三层逻辑，解决长文本分段处理的语义断裂、重复匹配、操作冲突问题
### 关键实验
基于5类主流预训练语料训练1B参数MiniCPM模型，和Raw语料、ProX-C基线对比：UltraX在所有语料上平均性能最优，相对提升超2%；仅用16B token训练就超过基线20B token的训练效果，数据效率提升20%；人工评估精炼质量得分9.6，低质样本占比仅0.38%。
### 核心结论
预训练数据优化的核心不是删得越多越好，而是通过细粒度可控编辑平衡噪声去除和有效信息保留，用极低的精炼成本最大化语料的有效训练密度。
