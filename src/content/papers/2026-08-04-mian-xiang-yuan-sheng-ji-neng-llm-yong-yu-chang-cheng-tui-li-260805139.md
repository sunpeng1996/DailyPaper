---
title: 'Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon
  Reasoning'
title_zh: 面向原生技能LLM：用于长程推理评测与训练的技能熵方法
authors:
- Yinghui He
- Ling Yang
- Jiarui Liu
- Yongjin Yang
- Lechen Zhang
- Yingcheng Wu
- Zhenfei Yin
- Mengdi Wang
- Sanjeev Arora
affiliations:
- Princeton University
- Carnegie Mellon University
- University of Toronto
- University of Illinois Urbana-Champaign
- Stanford University
arxiv_id: '2608.05139'
url: https://arxiv.org/abs/2608.05139
pdf_url: https://arxiv.org/pdf/2608.05139
published: '2026-08-04'
collected: '2026-08-06'
category: Reasoning
direction: 长程推理 · 技能熵评测与训练
tags:
- Skill Entropy
- Long-Horizon Reasoning
- LLM Benchmark
- RL for LLM
- Skill Switching
one_liner: 提出技能熵衡量跨技能切换难度，构建Skill2-Bench基准，配套RL训练方法提升长程推理性能
practical_value: '- 电商Agent复杂任务（如多轮导购、跨品类活动策划）可参考技能熵思路，先拆解任务技能序列，标注技能切换难度，提前规避高难度切换的任务设计缺陷

  - 做LLM增强的推荐系统（如用户多轮需求理解、定制化方案生成）时，可在RL训练中加入技能序列对齐奖励，提升模型在多步骤任务中不跑偏的能力

  - 业务场景的LLM效果评测可参考Skill2-Bench构建方法，基于业务实际技能库（如推荐话术生成、优惠计算、需求识别）构造跨技能长程任务，更准确衡量模型业务可用性

  - 不需要重新构造训练数据，可通过LLM自动标注现有业务推理trace的技能标签，就能叠加技能熵奖励提升现有RL训练效果，迁移成本低'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM在单技能任务上表现优异，但在跨技能长程推理任务（如先做数学计算、再做路径规划、最后生成文案）中性能下降明显，即使各单独技能模型都掌握，组合后准确率仍出现显著下滑。现有评测基准多聚焦单技能能力，缺乏量化技能切换难度的统一指标，也没有针对性的训练方法来提升模型的跨技能切换能力。

### 方法关键点
- 提出**Skill Entropy**：定向衡量从技能A切换到技能B的难度，基于参考模型在单技能、跨技能任务上的准确率比值计算，值越高切换难度越大；任务级技能熵为整条任务链的平均两两技能熵
- 构建**Skill2-Bench**基准：覆盖9个领域共558种技能，按技能熵将任务分为低/中/高3个难度层级，可量化模型的技能切换gap
- 提出**Skill-Entropy RL**训练框架：要求模型每步输出答案前先预测当前使用的技能，奖励由步骤准确率奖励+技能序列对齐奖励（预测技能熵与黄金技能熵的相似度）加权组成

### 关键结果
- 评测8款前沿闭源模型、4款开源模型发现，模型准确率随任务技能熵升高单调下降，同技能放在跨技能任务中准确率下降4%~13%
- 在Qwen3-4B-Instruct上Skill2-Bench得分从34.4%提升到68.4%，Qwen3-1.7B从14.6%提升到40.1%，效果远超其他技能感知训练基线
- 技能熵奖励可直接接入现有公开训练数据（如OpenR1-Math），相比普通GRPO平均提升1.9%

**最值得记住的一句话**：LLM长程推理的核心瓶颈之一是跨技能切换能力，该能力与单技能熟练度正交，可通过技能熵量化并作为训练信号大幅提升。
