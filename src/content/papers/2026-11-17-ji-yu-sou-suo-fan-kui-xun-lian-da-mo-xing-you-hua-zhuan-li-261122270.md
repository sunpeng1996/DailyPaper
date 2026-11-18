---
title: Teaching Language Models to Narrow Boolean Patent Searches from Search Feedback
title_zh: 基于搜索反馈训练大模型优化专利布尔查询缩小策略
authors:
- Seiya Kawano
- Koji Marusaki
- Hirofumi Nonaka
- Koichiro Yoshino
affiliations:
- Kyoto Institute of Technology
- RIKEN
- Nagaoka University of Technology
- Aichi Institute of Technology
- The University of Osaka
arxiv_id: '2611.22270'
url: https://arxiv.org/abs/2611.22270
pdf_url: https://arxiv.org/pdf/2611.22270
published: '2026-11-17'
collected: '2026-11-18'
category: QueryRec
direction: 布尔Query生成 · 检索反馈优化
tags:
- Boolean Query Generation
- Patent Retrieval
- LLM Fine-tuning
- Offline Adaptation
- Query Reformulation
one_liner: 提出策略级与行级两种LLM离线适配方法，优化专利布尔查询兼顾召回与结果集可筛选性
practical_value: '- 电商搜索query改写、多轮筛选等迭代式查询场景，可复用行级细粒度奖励设计：仅给保留核心召回结果同时缩小结果集的操作加权，解决全局奖励的credit分配模糊问题

  - 多目标query生成（如搜索suggestion、广告定向query）可参考两种学习方案互补的思路：策略级学习保障召回率，行级学习优化结果集大小、点击率等细粒度业务目标

  - 序列类内容（多轮query、推荐理由链等）的LLM离线适配，可借鉴「过滤无增益rollout + 加权交叉熵」的训练范式，降低无效样本干扰，提升训练效率

  - 电商组合筛选（类目+属性+关键词）的自动query生成场景，可复用NetCapture类评估指标，平衡召回率与用户筛选操作成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有专利布尔查询生成方案仅优化单步召回指标，生成的结果集往往过大，无法满足人工筛选的效率要求；且现有基于全局策略奖励的训练方法无法定位到单步query的有效贡献，难以兼顾召回率与结果集可筛选性的平衡。

### 方法关键点
- 数据层：蒸馏日本专利局38397份专家检索报告，构建包含425405条可执行布尔查询、109717条引用关联的检索策略数据集，配套可复现执行的检索环境
- 训练方案：提出两种互补的LLM离线适配方法：1）策略级学习：基于兼顾召回、结果集大小、query合法性的NetCapture全局评分，用AWR、DPO做偏好优化；2）行级保留引用缩小信用：仅给保留已命中目标引用、同时缩小结果集的query行分配高训练权重，无增益或过窄丢失引用的行仅给极低上下文权重，用加权交叉熵训练
- 迭代流程：先SFT让模型学习布尔query语法，再循环执行「生成检索策略rollout → 检索环境执行打分 → 模型更新」的流程

### 关键实验
基于Qwen3.5-9B+LoRA训练，基线覆盖零样本/少样本GPT-5.4-mini、Qwen3.5/3.6系列模型。迭代后行级信用方案将包含目标引用的结果集中位数从SFT的768降至48.5，<100条结果的召回率超过专家水平；策略级DPO方案召回率达99.23%，接近全覆盖，两者分别适配筛选优先、召回优先的业务场景。

### 核心结论
序列式查询优化任务中，行级细粒度过程反馈比全局结果奖励能更高效地优化可筛选性等细粒度目标，与全局策略级学习结合可覆盖不同业务的目标平衡点
