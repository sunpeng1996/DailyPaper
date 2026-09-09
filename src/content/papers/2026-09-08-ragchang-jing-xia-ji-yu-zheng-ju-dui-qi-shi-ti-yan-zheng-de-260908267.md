---
title: Evidence-Aligned Entity Verification for Hallucination Detection in Retrieval-Augmented
  Generation
title_zh: RAG场景下基于证据对齐实体验证的幻觉检测方法
authors:
- Runsong Jia
- Zhen Fang
- Mengjia Wu
- Jie Lu
- Yi Zhang
affiliations:
- University of Technology Sydney
arxiv_id: '2609.08267'
url: https://arxiv.org/abs/2609.08267
pdf_url: https://arxiv.org/pdf/2609.08267
published: '2026-09-08'
collected: '2026-09-09'
category: RAG
direction: RAG幻觉检测 · 实体级验证
tags:
- Hallucination Detection
- Entity Alignment
- Counterfactual Analysis
- RAG
- Factual Verification
one_liner: 提出多维度实体证据对齐+反事实稳定性分析的RAG幻觉检测框架，在多基准上取得SOTA性能
practical_value: '- 电商商品问答、客服RAG系统可直接复用实体级验证逻辑，对商品名、价格、参数等关键实体做三重对齐检测，避免虚假信息输出，降低客诉

  - 反事实稳定性分析的4种扰动策略可直接迁移到RAG faithfulness评估流程，解决检索片段与生成内容表面匹配但事实不符的问题，提升评估准确率

  - EAEV的SFT数据构造方法（给幻觉实体加标签+加权交叉熵训练）可低成本适配业务场景，无需人工标注即可训练轻量幻觉检测器，部署成本远低于多轮采样类方案'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG幻觉检测方法多依赖模型内部不确定性或粗粒度文本一致性校验，易漏检实体级（名称、数值、日期等）细粒度错误，且无法区分检索片段与生成内容的表面匹配和真实事实对齐，在高事实要求场景存在严重风险。

### 方法关键点
- 实体级对齐框架：提取生成内容中的实体、数值、名词短语三类候选，分别从字面匹配、语义相似度、数值/逻辑一致性三个维度做适配性加权对齐，不同类型实体侧重不同校验维度（数值类侧重一致性，实体类侧重字面+语义）
- 反事实稳定性分析：通过留一证据移除、标点大小写归一化、空格压缩、仅保留字母数字四种扰动，验证实体对齐的鲁棒性，过滤表面匹配的伪关联
- 实体聚合与SFT训练：对同实体多提及结果做保守聚合，将校验结果转化为带幻觉实体标签的训练数据，通过加权交叉熵微调LLM获得端到端检测器

### 关键实验
在RAGTruth、HotpotQA、DelucionQA三个基准上测试，对比SelfCheckGPT、RAGAS、TSV等11种SOTA基线，在LLaMA2-13B上平均AUROC达87.55%，较最优基线TSV提升3.34个百分点，推理速度是SelfCheckGPT的7.3倍，GPU/CPU内存占用更低。

### 核心结论
RAG场景下的幻觉多集中在实体级，实体对齐+反事实扰动的校验效果远优于粗粒度语义一致性校验，且可解释性、部署效率更高
