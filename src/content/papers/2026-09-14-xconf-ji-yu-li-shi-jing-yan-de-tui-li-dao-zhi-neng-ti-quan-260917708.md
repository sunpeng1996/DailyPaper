---
title: 'Confidence Comes from Experience: Experiential Confidence Estimation from
  Reasoning to Agents'
title_zh: 《XConf：基于历史经验的推理到智能体全场景置信度估计方法》
authors:
- Caiqi Zhang
- Xiaochen Zhu
- Chengzu Li
- Yulong Chen
- Dharshan Kumaran
- Nigel Collier
affiliations:
- University of Cambridge
- Google DeepMind
arxiv_id: '2609.17708'
url: https://arxiv.org/abs/2609.17708
pdf_url: https://arxiv.org/pdf/2609.17708
published: '2026-09-14'
collected: '2026-09-17'
category: Agent
direction: Agent 置信度校准与可信优化
tags:
- Confidence Estimation
- LLM Agent
- Experience Bank
- Black-box
- Calibration
one_liner: 提出黑盒无训练的经验驱动置信度估计框架XConf，性能超10次采样自洽性，成本仅为其1/10
practical_value: '- 电商导购、售后、订单处理等Agent可直接复用XConf架构，无需微调模型，仅通过积累历史交互成败数据构建经验银行，即可实现置信度校准，适配闭源LLM
  API场景

  - 生成式推荐场景（AI文案、搭配生成、商品召回结果过滤）可接入XConf，丢弃低置信度输出，降低错误推荐风险，实测筛掉10%最低置信度样本可使交付成功率最高提升8.7个点

  - 经验银行支持跨模型、跨同领域数据集迁移，冷启动阶段可复用同业务其他模型的经验库，仅损失0.03~0.06 AUROC，大幅降低上线初期的数据积累成本

  - 检索key设计可复用：任务语义embedding+初始置信度的组合检索效果最优，比纯语义检索AUROC高0.1左右，适合各类长输出、不可投票的场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM置信度估计方法仅依赖当前单次推理过程，要么需要logit访问（多数闭源API不支持），要么需要多次重采样成本高，在代码、Agent轨迹等长输出场景下校准误差大，无法满足高风险业务的可信部署需求，亟需黑盒、低成本、跨场景的校准方案。
### 方法关键点
- 经验银行：存储历史episode，包含任务、推理反思、初始置信度、真实结果、事后教训5个字段，为业务运行的副产品，无需额外标注
- Recall阶段：以「任务语义embedding + 初始置信度」为检索key，召回Top50相似历史episode，计算历史成功率作为统计置信度
- Reflect阶段：将召回的episode上下文喂给LLM，引导其结合历史失败模式输出主观置信度，最终置信度为统计与主观置信度的平均值
- 全程黑盒、无训练、不改模型权重，支持推理、代码、多模态、Agent等任意输出格式
### 关键实验
覆盖9个基准（推理、代码、多模态、3类Agent任务），4个不同家族的LLM。对比10次采样自洽性（SC@10）基线：23/24个场景下AUROC打平或超过，ECE大幅降低，生成成本仅为SC@10的1/10；选择性预测场景下，丢弃10%最低置信度样本，Agent任务交付成功率最高提升8.7个点；经验银行规模越大校准效果越好，Agent场景下AUROC随经验积累持续上升无饱和。
### 核心结论
置信度的核心来源不是单次推理的自我审视，而是同类任务的历史成败记录，经验驱动的校准是LLM/Agent落地高风险场景的低成本可行路径
