---
title: 'Beyond Sentiment: Structured Information Extraction from Financial News'
title_zh: 超越情感分析：面向财经新闻的结构化信息提取
authors:
- Daohan Zhu
- Sitong Ge
- Ruofei Wang
- Honggu Chen
- Yubo Hou
- Tao Wan
- Zengchang Qin
affiliations:
- Beihang University
- VinUniversity
arxiv_id: '2607.28496'
url: https://arxiv.org/abs/2607.28496
pdf_url: https://arxiv.org/pdf/2607.28496
published: '2026-07-30'
collected: '2026-08-01'
category: Other
direction: 财经NLP · 结构化信息抽取
tags:
- Information Extraction
- LLaMA-3.1
- Financial NLP
- Sentiment Analysis
- Feature Fusion
one_liner: 基于LLaMA-3.1-70B抽取财经新闻多维度结构化特征，融合情感信号提升股价预测性能
practical_value: '- 做电商内容理解（商品评价、客服话术、营销文案分析）时，可参考多维度正交特征抽取思路，不要仅依赖单一情感分，补充事件类型、影响范围、时效、置信度等维度特征，减少信息损失

  - 多源特征融合时可优先验证特征正交性，选择分歧率高的特征组合，能获得更显著的性能增益

  - 垂域信息抽取任务可采用「垂直领域小模型基础特征+大模型抽取结构化特征」的融合方案，平衡效果与推理成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有新闻驱动的股价预测仅将财经新闻压缩为单一情感极性分，丢失事件类型、影响范围、时间 horizon、置信度等多维度正交信息，大幅限制预测性能。
### 方法关键点
基于LLaMA-3.1-70B构建结构化信息抽取框架，从财经新闻中提取6个独立语义维度特征，与FinBERT输出的情感特征融合后输入下游预测模型。
### 关键结果
在FNSPID数据集41618条新闻-股票对测试：① 单独FinBERT情感特征在非线性模型下F1=0.576，线性模型下仅0.230，证明情感与收益为强非线性关系；② LLM抽取的结构化特征与情感特征系统分歧率达53.5%，信息正交性显著；③ 两类特征融合后F1达0.600，较单独使用FinBERT提升ΔF1=+0.019，6个抽取维度的特征贡献占比均衡（14%~21%）。
