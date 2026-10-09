---
title: Reasoning-Informed Visual Editing
title_zh: 推理感知视觉编辑：分级评测基准RISEBench++与免训练Agent框架
authors:
- Xue Yang
- Peiyuan Zhang
- Yilun Zhu
- Qihao Yang
- Mingxin Liu
- Xiangyu Zhao
- Ziqian Fan
- Zhaokai Wang
- Yan Li
- Yifan Yang
affiliations:
- Shanghai Jiao Tong University
- Southeast University
- South China University of Technology
- Microsoft Research Asia
- Fudan University
arxiv_id: '2610.12343'
url: https://arxiv.org/abs/2610.12343
pdf_url: https://arxiv.org/pdf/2610.12343
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: 多模态Agent · 视觉编辑评测体系构建
tags:
- Multimodal LLM
- Visual Editing
- Benchmark
- Agent Framework
- Reasoning
- Evaluation
one_liner: 提出首个推理感知视觉编辑分级基准RISEBench++，及免训练Agent框架，完成58种方案评测
practical_value: '- 电商商品图批量多步编辑场景可复用RISE-Agent的「推理规划-工具执行-验证迭代」免训练架构，无需微调即可适配复杂修图需求

  - 多模态内容生成效果评测可直接复用LMM-as-judge的三维评估逻辑（指令遵循/外观一致性/视觉合理性），大幅降低人工标注成本

  - 多轮复杂交互类生成任务的bad case分析可参考RISEBench++的6维度推理能力拆分方法，实现细粒度能力短板定位'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态大模型在视觉编辑场景下存在复杂指令遵循能力弱、外观一致性难保障、输入格式支持有限等问题，缺乏统一的推理维度评测体系。
### 方法关键点
1. 构建分级评测基准RISEBench++，覆盖时间/因果/空间/逻辑/反事实/混合6大推理维度，拆解为12个子类、65个细粒度任务，包含1000条中英双语人工标注用例，支持多图像条件输入；
2. 设计三维评估框架，结合人工标注与LMM-as-judge模式，从指令推理、外观一致性、视觉合理性三个维度做校准化评估；
3. 提出免训练RISE-Agent，融合推理驱动规划、工具增强执行、验证引导迭代三大模块，无需微调即可适配复杂编辑需求。
### 关键结果数字
完成58种视觉编辑方案评测（34开源、19闭源、5个Agent方法），当前最强方案GPT-Image-2.5 Sunburst准确率仅56.6%，RISE-Agent性能优于多数现有基线。
