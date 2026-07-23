---
title: 'EduPanel: A Three-Agent LLM Judge for Teaching Videos -- Reliability, Complementarity,
  and Human Trust Calibration'
title_zh: EduPanel：面向教学视频的三智能体LLM评测框架及信任校准方案
authors:
- Jia-Kai Dong
- Yi-Cheng Lin
- Hung-yi Lee
affiliations:
- National Taiwan University
- NTU Artificial Intelligence Center of Research Excellence
arxiv_id: '2607.18529'
url: https://arxiv.org/abs/2607.18529
pdf_url: https://arxiv.org/pdf/2607.18529
published: '2026-07-19'
collected: '2026-07-23'
category: Agent
direction: Agent 多智体协同内容评测优化
tags:
- LLM-Judge
- Multi-Agent
- Content-Evaluation
- Human-AI-Collaboration
- Trust-Calibration
one_liner: 提出三专业化Agent协同的LLM评测框架，教学视频评测可靠性接近中等人类专家
practical_value: '- 可复用三专用Agent分工的架构设计，对电商商品讲解视频、广告素材、种草内容等做分维度自动评测，降低人工审核成本

  - 引入目标人群画像的评测逻辑可迁移，做分人群的内容/商品适配性打分，优化个性化推荐池的人群匹配质量

  - 人类-AI协同校准方案可复用：保留人工对低可靠性AI输出的识别干预入口，既提效又避免AI错误传导到业务'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
在线教学视频规模爆发，现有自动评测方法未覆盖多模态证据、未适配目标学习者差异，人工基于教学标尺的评测成本极高、难以规模化。

### 方法关键点
1. 提出EduPanel三Agent协同评测框架，基于明确评测标尺做维度拆解，每个智能体聚焦单一评测维度输出结果；
2. 引入学习者画像作为评测条件，输出人群适配的可解释评测结论；
3. 设计人类信任校准机制，明确标注AI输出的可靠性置信度，支持专家干预修正。

### 关键结果
1. 评测可靠性达到中等人类专家水平；
2. 辅助专家评测时可将打分MAE从0.87降至0.73，专家识别不可靠AI输出的AUC达0.77，避免盲目信任AI结果。
