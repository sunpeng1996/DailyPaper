---
title: 'Which Skill to Distill? SGUID: Selecting a Compact Skill Bank for Model-Skill
  Co-Evolution'
title_zh: SGUID：面向模型-技能协同进化的紧凑技能库选择方法
authors:
- Yuhan Liu
- Xiyao Ma
- Zhongkai Sun
- Xu Han
- Chengyuan Ma
- Benjamin Z. Yao
- Chenlei Guo
affiliations:
- New York University
- Amazon
arxiv_id: '2610.12367'
url: https://arxiv.org/abs/2610.12367
pdf_url: https://arxiv.org/pdf/2610.12367
published: '2026-10-08'
collected: '2026-10-09'
category: Training
direction: LLM技能蒸馏 · 模型-技能协同进化
tags:
- Skill_Distillation
- LoRA
- Model-Skill_Coevolution
- On-Policy_Distillation
- LLM_Training
one_liner: 基于训练动态筛选高价值技能，用极小技能库实现更优蒸馏效果与稳定模型-技能协同进化
practical_value: '- 电商/广告Agent技能库迭代可直接复用SGUID的筛选规则：保留训练早期有正向信号、后期衰减不超阈值的技能，砍掉75%+无效技能，降低检索和蒸馏成本

  - 垂直领域LLM蒸馏可参考「小批量全库跑统计信号→选高价值子集正式训练」的范式，相比全量蒸馏效率更高，尤其适合推荐理由生成、客服话术等场景的技能蒸馏

  - 不用盲目堆砌技能库规模：实测4~12个精选技能的蒸馏效果匹敌几十上百个技能的全库，业务上优先做技能质量打磨而非数量扩张

  - 模型-技能闭环迭代必须加入筛选环节：无筛选的迭代会导致效果退化，该结论可直接复用在电商Agent自我进化链路中'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有技能蒸馏直接基于语义检索选技能，忽略单个技能的实际效用，实测不到25%的检索技能能提供有效蒸馏信号；全库蒸馏不仅效率低，还会引入噪声导致多轮迭代时效果退化，无法实现稳定的模型-技能协同进化。

### 方法关键点
- 提出SGUID三阶段协同进化框架：先用当前模型rollout生成候选技能库，再跑一轮全库蒸馏统计训练动态，筛选符合3个条件的技能：早期有正向贡献、late阶段正向信号数≥阈值、贡献率衰减不超过τ倍
- 筛选后取top K个技能构建紧凑技能库，重新蒸馏得到更新后的模型，再用新模型生成下一轮候选技能库，实现闭环迭代
- 蒸馏基于LoRA实现，技能有效性通过验证器对齐的训练信号判断，过滤无效噪声

### 关键实验
在Olmo、Qwen系列4个模型，AIME24、AIME25、HMMT25三个数学推理数据集上验证，对比GRPO、OPSD、SGSD等基线：第一轮仅蒸馏6个精选技能，在3/4模型上均值avg@12超过11倍大小的全库蒸馏效果，Qwen3-4B上性能从64.2%提升到65.1%；第二轮再蒸馏3个新筛选技能，4个模型效果全部超过全库蒸馏，Qwen3-8B性能从64.3%提升到66.3%；无筛选的协同进化会导致Qwen3-4B的HMMT25指标下降0.3个百分点，SGUID则提升1.1个百分点。

### 核心结论
检索只能决定老师能看到哪些技能，不能决定哪些技能真的能教出更好的学生，技能筛选是稳定模型-技能协同进化的核心前提。
