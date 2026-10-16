---
title: 'The Scored Population, the Operating Point, and the Pipeline: Three Objects
  That Decide What an Open-Web Event System Looks Like'
title_zh: 开放网络事件系统效果的三大决定因素：打分样本集、工作点与流水线
authors:
- Shengqi Zhou
- Zhigang Liu
- Wenxiang Zhu
- Boyong Du
- Kairui Yang
- Haicheng Huang
- Weijian Bu
affiliations:
- Northeast Petroleum University
- Tongji University
- Chongqing University
arxiv_id: '2610.17814'
url: https://arxiv.org/abs/2610.17814
pdf_url: https://arxiv.org/pdf/2610.17814
published: '2026-10-13'
collected: '2026-10-16'
category: Eval
direction: 多阶段LLM流水线 · 评估方法论
tags:
- Evaluation Methodology
- LLM Pipeline
- Open Web Processing
- Operating Point
- Coverage-aware Measurement
one_liner: 针对多阶段开放网络系统的评估盲区，提出兼顾打分覆盖、阈值选择与全流决策的评估框架
practical_value: '- 多阶段召回/排序链路评估要覆盖全量输入而非仅过了前序模块的样本，避免误判不同模型的真实效果差异

  - 调整链路中间模块补全缺失打分时，要同步校准后续模块的阈值，避免固定阈值下误召回率大幅上升

  - 跨模型效果对比必须在共有的打分样本子集上执行，才能得到客观的AUC等排序指标差距'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有多阶段Web系统评估存在盲区：流水线不仅决定输入的打分结果，还决定哪些输入能进入打分环节，仅评估被打分样本会导致效果判断严重偏差。
### 方法关键点
以开放网络事件准入为案例，通过共享子集对比、准入损失分解、可控抽取恢复干预三种手段，系统分析打分样本集、工作阈值、全输入流行为三类核心影响因素。
### 关键结果数字
1. Original-302数据集上Qwen仅能对255/302样本打分，在共享子集对比可大幅缩小其与全量准入方案的AUC差距；
2. 固定阈值下补全缺失打分反而会升高误接受率，Mistral的span-safe恢复策略将误接受率从73.1%提升至92.5%；
3. 基于3290条资源中602条人工标注样本，验证了兼顾打分可用性、阈值选择、全流决策的评估框架的有效性。
