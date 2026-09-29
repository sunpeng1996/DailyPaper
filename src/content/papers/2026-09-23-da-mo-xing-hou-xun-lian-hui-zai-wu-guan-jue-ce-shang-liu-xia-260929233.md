---
title: Post-Training Leaves Behavioral Shadows on Unrelated Decisions
title_zh: 大模型后训练会在无关决策上留下可传递能力的行为痕迹
authors:
- Ziyang Zhang
- Yubin Jing
- Yuanhao Zeng
- Yuyao Li
- Haofan Wang
- Yichen Gong
affiliations:
- 北京大学
- Georgia Institute of Technology
- 上海科技大学
- 清华大学
- Lovart AI
arxiv_id: '2609.29233'
url: https://arxiv.org/abs/2609.29233
pdf_url: https://arxiv.org/pdf/2609.29233
published: '2026-09-23'
collected: '2026-09-29'
category: Training
direction: 大模型蒸馏 · 隐性能力迁移
tags:
- Knowledge-Distillation
- Post-Training
- LoRA
- Black-Box-Model
- Subliminal-Learning
one_liner: 提出主动无任务蒸馏ATD方法，仅通过后训练模型在无关prompt上的单字选择实现跨模型能力迁移
practical_value: '- 黑盒大模型对齐场景可直接复用ATD的近边界prompt选择策略：无需获取第三方闭源模型的参数、logits或目标任务训练数据，仅通过少量无关prompt的单token反馈，即可蒸馏得到对齐闭源模型能力的小模型，适合对齐大厂API的推荐文案生成、query理解能力等场景

  - 多能力融合训练可复用论文的信号可组合结论：混合不同能力teacher的行为痕迹样本，可同时为小模型注入多种能力，无需分阶段多轮微调，降低多任务推荐/Agent模型的训练成本

  - 小样本LoRA微调可借鉴RPM边界感知损失：聚焦模型决策边界的梯度更新，相比普通交叉熵损失，可在相同样本量下提升下游任务效果，适合商品标签生成、用户意图识别等标注数据稀缺的场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统认知中后训练的效果仅体现在目标任务上，近年潜意识学习研究发现大模型会在无关文本中传递行为特征，但现有方法需要大量teacher输出，未充分挖掘无关决策中蕴含的可迁移能力信号，也缺乏低成本的提取手段。
### 方法关键点
- 用公共祖先模型筛选近边界无关prompt：仅保留两个普通单token的输出概率差≤0.02的prompt，确保后训练带来的微小偏好变化即可改变输出结果
- 黑盒采样仅获取单token反馈：无需目标任务样本、teacher logits或参数，仅向私有teacher查询每个prompt的最高概率单token
- 学生模型微调：同公共祖先初始化的学生模型，可基于普通交叉熵或边界感知的RPM损失，仅在收集到的prompt-单token对上面微调
### 关键实验
主实验采用Qwen2.5-1.5B模型做代码能力蒸馏，仅用5664个单token训练样本，HumanEval+ pass@1相比打乱配对的对照组提升5.34pp，效果与私有teacher相当；跨7个任务（科学知识、常识推理、阅读理解等）实验均获得0.81~5.03pp的稳定提升，适配LoRA、全参数微调两种模式，在Qwen、Llama多个模型族上均验证有效。
### 核心结论
大模型后训练的能力不会局限在目标任务，其在无关决策上的微小偏好变化，也足以提取出可复用的能力信号。
