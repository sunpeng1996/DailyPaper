---
title: 'WebRetriever: A Large-Scale Comprehensive Benchmark for Efficient Web Agent
  Evaluation'
title_zh: WebRetriever：面向网页Agent的大规模高覆盖评测基准
authors:
- Wei Dong
- Tianyu Fu
- Zhe Yu
- Hanning Wang
- Anyang Su
- Zhizhou Fang
- Yuyang Chen
- Shuo Wang
- Minghui Wu
- Ping Jiang
affiliations:
- Mininglamp Technology
- University of Chinese Academy of Sciences
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2607.06118'
url: https://arxiv.org/abs/2607.06118
pdf_url: https://arxiv.org/pdf/2607.06118
published: '2026-07-07'
collected: '2026-07-08'
category: Agent
direction: 网页Agent 评测基准与自动化评估
tags:
- WebAgent
- Benchmark
- LLM-as-Judge
- Evaluation
- MultiModal
one_liner: 推出覆盖800个网站1550项任务的网页Agent评测基准及高对齐度自动化评测框架
practical_value: '- 电商Web Agent（自动比价、商品爬取、客服自动化）团队可复用NavEval评测思路，结合请求日志、操作轨迹、截图多源信号做自动化验收，替代高成本人工标注，对齐率达90%+

  - 自研Agent团队可参考三维评测协议，拆解基础导航、知识辅助导航、端到端信息抽取的能力短板，避免「到页即成功」的虚假评估

  - 电商流程自动化Agent（跨平台铺货、订单同步）可参考Protocol II思路，给Agent喂结构化操作手册，实测能提升约8%的任务成功率，减少幻觉'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有网页Agent评测基准存在三大核心缺陷：规模小、域覆盖不足，无法验证跨域泛化能力；LLM-as-Judge方法无法捕捉查询构造、过滤操作等细粒度交互语义；仅关注导航成功率，忽略真实部署要求，导致基准成绩和实际落地效果存在巨大Gap，急需更贴近真实场景的评测体系。
### 方法关键点
- 构建WebRetriever基准：覆盖8大行业800个真实网站、1550个任务，兼顾普通与专业用户意图，按操作步骤分为易中难三级，长期维护保证可用性
- 提出NavEval自动化评测框架：基于Playwright采集交互过程的URL、网络请求、操作序列、最终截图，经规则过滤去噪后输入LLM综合判断，兼顾准确率与效率
- 设计三套互补评测协议：分别评估纯任务引导的基础导航能力、给定操作手册的知识辅助导航能力、导航+信息抽取的端到端任务完成能力
### 关键结果
在7款主流SOTA网页Agent评测中，人工评估平均成功率仅21.1%（基础导航）、29.2%（知识辅助导航）、11.8%（端到端任务），远低于现有基准的虚高成绩；NavEval与人类判断平均对齐率达91.2%，在外部基准Online-Mind2Web上对齐率达97%，显著优于同类方法。
### 核心结论
当前网页Agent的基准成绩远高于实际落地能力，仅导航成功不能代表任务完成，必须结合信息抽取的端到端评估才能反映真实可用性。
