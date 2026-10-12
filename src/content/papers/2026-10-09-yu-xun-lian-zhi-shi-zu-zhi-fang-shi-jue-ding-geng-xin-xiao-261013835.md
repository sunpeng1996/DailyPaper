---
title: 'Specialists Learn Faster: Knowledge Organization in Pre-training Shapes Knowledge
  Update Efficiency'
title_zh: 预训练知识组织方式决定更新效率：专家模型学习新知识更快
authors:
- Sheng Zhao
- Yuhao Zhu
affiliations:
- University of Rochester
arxiv_id: '2610.13835'
url: https://arxiv.org/abs/2610.13835
pdf_url: https://arxiv.org/pdf/2610.13835
published: '2026-10-09'
collected: '2026-10-12'
category: Training
direction: LLM预训练数据组织与知识更新效率优化
tags:
- Knowledge Update
- Pre-training Data Organization
- LoRA
- Model Editing
- Temporal Knowledge
- LLM Optimization
one_liner: 揭示预训练数据时序排列规律 让LLM新知识更新步数最高减少58%
practical_value: '- 做电商/广告垂直领域LLM预训练时，可将近期高频变更的商品、价格、投放规则等知识按时间顺序排列，历史稳定知识打乱训练，既能保证历史知识准确率，又能减少30%+的新知识更新成本

  - 现有业务LLM需要频繁更新知识时，可加一轮短期增量预训练：将历史知识打乱、最近1-3个月的业务知识按时序排列训练，可在不损失历史知识的前提下，将后续LoRA/模型编辑的更新步数降低1.3-1.8倍

  - 做Agent工具调用的API知识训练时，可将不同版本的API文档按版本号顺序排列最新版本、旧版本打乱训练，可提升新版本API知识的更新效率最高48%

  - 知识更新时优先调整模型中间层参数，该区域梯度贡献占比最高，可进一步降低更新成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM知识更新研究大多聚焦训练后优化（如模型编辑、LoRA微调），忽略预训练阶段的知识组织方式对后续更新效率的影响，而电商、广告等业务场景中LLM需要频繁更新商品、价格、投放规则等动态知识，更新成本高、易遗忘是核心痛点。
### 方法关键点
- 定义两类模型：按时序排列训练动态知识的「专家模型」，对近期知识准确率高；随机打乱时序训练的「通用模型」，全时段知识表现均衡
- 推导知识更新步数定律：更新所需步数=初始知识差/(学习率×初始梯度模长)，专家模型初始梯度是通用模型的1.39~2.82倍，是其更新更快的核心原因
- 提出混合训练策略：历史稳定知识打乱训练保证全时段准确率，近期高频变更知识按时序训练提升更新效率
### 关键结果
- 实验覆盖合成时序传记数据集、Gemma-2-9B真实预训练模型、版本化软件API三类场景，基线为全随机打乱训练的通用模型
- 专家模型比通用模型的知识更新步数少27%~58%，模型规模越大收益越高
- 混合训练策略比全打乱训练更新步数少16%~48%，知识遗忘率低5%~63%；对ROME、MEMIT等现有模型编辑工具也可降低46%更新成本、减少63%遗忘

> 最值得记住的一句话：预训练阶段将高频更新的近期知识按时序排列，是降低后续知识更新成本最简单有效的手段之一
