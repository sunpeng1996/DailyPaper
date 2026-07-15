---
title: 'JobHop v2: A Large-Scale Career Trajectory Dataset from Unstructured Resumes'
title_zh: JobHop v2：从非结构化简历构建的大规模职业轨迹数据集
authors:
- Iman Johary
- Guillaume Bied
- Alexandru C. Mara
- Tijl De Bie
affiliations:
- AIDA-IDLab, Ghent University
arxiv_id: '2607.11715'
url: https://arxiv.org/abs/2607.11715
pdf_url: https://arxiv.org/pdf/2607.11715
published: '2026-07-13'
collected: '2026-07-15'
category: Other
direction: 职业推荐 · 非结构化信息LLM提取
tags:
- Information Extraction
- LLM Pipeline
- Job Recommendation
- Open Dataset
- Career Trajectory
one_liner: 公开从44万份简历LLM提取的35万条带丰富标注的职业轨迹数据集及高鲁棒性提取pipeline
practical_value: '- 做非结构化文本（用户简历、评价、咨询记录）结构化提取时，可借鉴带重试机制的推理控制LLM推理pipeline，实现100%
  JSON解析率，降低下游数据处理成本

  - 构建业务领域标注数据集时，可参考多基线对照的评估协议，对齐人工标注一致性天花板，量化标注质量

  - 求职/职场类垂直推荐场景下，可直接复用该开源数据集做模型预训练或冷启动验证，降低数据采集成本

  - 多源异构半结构化数据归一化处理时，可参考其将非标准化职业、教育信息映射到标准化编码的schema设计'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有公开职业轨迹数据集普遍规模小、不可独立使用、多为LLM合成文本而非真实自由文本，无法支撑职业推荐、劳动力市场分析等场景的研究与落地。
### 方法关键点
1. 基于弗拉芒公共就业服务局提供的44万份匿名多语言简历，构建端到端LLM非结构化信息提取pipeline
2. 引入带重试机制的推理控制LLM推理模块，配套更丰富的提取schema、多基线对照评估协议
### 关键结果
- 最终公开355315条标注有ESCO职业编码、季度级时间信息、五级归一化教育背景的职业轨迹
- 提取器JSON解析率达100%，效果仅比人工标注一致性上限低1.1~2.7个百分点，数据集与代码全开源
