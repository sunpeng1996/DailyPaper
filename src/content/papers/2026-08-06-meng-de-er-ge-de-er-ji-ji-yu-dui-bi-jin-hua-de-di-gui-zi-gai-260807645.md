---
title: 'Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative
  Evolution'
title_zh: 孟德尔哥德尔机：基于对比进化的递归自改进编码Agent
authors:
- Changzhi Liu
- Yilun Liu
- Sikuan Yan
- Volker Tresp
- Yunpu Ma
affiliations:
- University of Electronic Science and Technology of China
- Ludwig Maximilian University of Munich
- Munich Center for Machine Learning
arxiv_id: '2608.07645'
url: https://arxiv.org/abs/2608.07645
pdf_url: https://arxiv.org/pdf/2608.07645
published: '2026-08-06'
collected: '2026-08-12'
category: Agent
direction: Agent自进化 · 递归自改进框架
tags:
- Self-Improving Agent
- Evolutionary Algorithm
- Coding Agent
- LLM Agent
- Recursive Optimization
one_liner: 提出融合三类遗传算子的自改进编码Agent框架，显著提升性能效率与泛化性
practical_value: '- 做推荐/广告系统的自进化Agent（如召回策略迭代、Prompt自动优化、冷启动规则迭代）时，可复用跨场景、跨版本的历史失败轨迹的对比信号，不用仅依赖单次BadCase修复，大幅提升优化的泛化性

  - 自进化算子设计可直接复用：在传统单样本突变基础上，增加「同Agent跨多任务的共性缺陷修复」「同任务跨Agent的优势特性杂交」两类算子，可在相同迭代成本下提升30%以上的进化效率

  - 优化任务采样策略时，可对历史失败任务加权采样，主动制造不同Agent/策略的任务重叠，无需额外标注/评估成本即可获得更多对比优化信号

  - 自进化得到的工作流（如排序规则、用户意图理解流程）可跨LLM backbone迁移，先在小参数模型上完成进化，再迁移到大参数模型，可降低50%以上的大模型迭代成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自改进编码Agent每次仅基于单条失败轨迹修改自身代码，浪费了存档中积累的跨任务、跨谱系的丰富对比信号，进化效率低、泛化性差，难以得到可复用的工作流改进。

### 方法关键点
- 设计三类自修改算子：①克隆突变（单Agent单失败轨迹修改，兼容基线方案）；②反应范数突变（基于同一Agent跨多任务的失败/成功轨迹对比，定位共性缺陷做通用修复）；③跨谱系杂交（基于不同Agent在同一任务上的表现对比，提取可迁移的优势特性融入目标Agent）
- 新增失败任务加权采样机制：历史失败任务放入全局池，采样时给更高权重，主动制造跨Agent的任务重叠，零额外成本获取更多对比信号
- 基于存档的自适应算子选择：根据当前存档的轨迹积累情况，动态选择符合条件的算子执行，保证小存档时也能正常迭代

### 关键实验
在SWE-bench、Polyglot编码基准上对比基线HGM，相同200次评估预算下，以Qwen3.6-35B-A3B为backbone时，Polyglot准确率从初始50.8%提升到93.3%，比HGM高15.4个百分点；SWE-bench准确率从68.3%提升到78.3%，比HGM高5个百分点。进化得到的工作流零样本迁移到DeepSeek-V4-Pro时，Polyglot准确率达到96.9%，超越GPT-5且参数量仅为其1/117。

最值得记住的一句话：对比信号的复用是自改进Agent提升进化效率、降低成本的核心路径，无需额外增加评估预算即可获得显著收益。
