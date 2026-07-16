---
title: Towards Autonomous and Auditable Medical Imaging Model Development
title_zh: 面向自主可审计的医学影像模型多Agent开发框架
authors:
- Shengyuan Liu
- Jia-Xuan Jiang
- Boyun Zheng
- Cheng Wang
- Zipei Wang
- Wentao Pan
- Hongtao Wu
- Houwen Peng
- Yu Gu
- Lichao Sun
affiliations:
- The Chinese University of Hong Kong
- Institute of Automation, Chinese Academy of Sciences
- Microsoft Research
- Lehigh University
- Independent Researcher
arxiv_id: '2607.10522'
url: https://arxiv.org/abs/2607.10522
pdf_url: https://arxiv.org/pdf/2607.10522
published: '2026-07-11'
collected: '2026-07-16'
category: MultiAgent
direction: 多智体 · 自动化机器学习工作流优化
tags:
- MultiAgent
- LLM Agent
- AutoML
- Model Auditing
- Workflow Automation
one_liner: 提出多Agent框架AMID，实现自主可审计的医学影像建模，性能优于通用MLE系统接近人类方案
practical_value: '- 数据条件驱动的方法规划逻辑可复用：做推荐/广告建模自动化时，先基于业务数据特征（如用户行为、商品属性）缩小方法搜索空间，生成可并行的建模路径，大幅提升调优效率

  - 验证引导的双阶段优化架构可迁移：先广范围探索候选方案，再定向深耕高潜力方案，全程嵌入规则校验（如推荐A/B实验合理性、指标计算正确性校验），避免无效实验，产出可审计的模型产物

  - 多Agent分工自动化MLE的思路可落地到推荐系统自动迭代pipeline：拆分建模、验证、调优等角色为独立Agent，替代部分人工写代码、调参的重复工作'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
通用LLM Agent自动化MLE的能力难适配垂直领域，垂直场景（如医学影像、电商推荐）有专属的实验规则、严格的验证协议与产出物规范，现有通用方案无法满足合规性要求。

### 方法关键点
1. 数据条件驱动的方法规划：基于任务专属数据分析与领域可用资源，将粗粒度任务搜索空间细化为可执行、可并行的方法路径
2. 验证引导的双阶段优化：第一阶段广范围探索多样化方法路径，第二阶段定向优化高潜力候选，全程对验证协议、指标计算、预测产出做严格校验，保障结果可审计

### 关键结果
在覆盖不同模态、预测类型的20个医学影像竞赛任务上，AMID性能优于所有参测通用MLE系统，部分任务性能接近或持平人类专家设计的竞赛方案
