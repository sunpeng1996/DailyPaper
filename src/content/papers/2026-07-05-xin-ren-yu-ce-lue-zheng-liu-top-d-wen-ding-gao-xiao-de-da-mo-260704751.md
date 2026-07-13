---
title: Trust Region Policy Distillation
title_zh: 信任域策略蒸馏（TOP-D）：稳定高效的大模型在策略蒸馏范式
authors:
- Zhengpeng Xie
- Li Lyna Zhang
- Zeke Xie
- Mao Yang
affiliations:
- Xingyunzhili
- Hong Kong University of Science and Technology (Guangzhou)
- Microsoft
arxiv_id: '2607.04751'
url: https://arxiv.org/abs/2607.04751
pdf_url: https://arxiv.org/pdf/2607.04751
published: '2026-07-05'
collected: '2026-07-13'
category: Training
direction: 大模型在策略蒸馏 · 训练稳定性优化
tags:
- Policy Distillation
- On-Policy Training
- Trust Region
- LLM Alignment
- Training Stability
one_liner: 提出零额外开销的信任域策略蒸馏TOP-D，解决OPD训练不稳定样本效率低问题，具备理论收敛保证
practical_value: '- 做LLM4Rec、导购Agent的小模型蒸馏时，可直接将现有OPD的token reward替换为TOP-D的平滑奖励（α取0.1-0.3即可），零额外开销就能大幅提升训练稳定性和效果，无需依赖reward
  clipping等经验trick

  - 现有GRPO/DAPO等RLHF训练推荐/Agent模型时，可复用TOP-D的近端教师插值+离策略数据复用设计，提升样本效率，减少训练步数降低算力成本

  - 做电商query改写、商品文案生成的小模型蒸馏时，可直接套用TOP-D的token级优势归一化逻辑，避免生成过长/过短的无效输出，提升业务侧实用性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
标准On-Policy Distillation（OPD）是大模型后训练的主流范式，既能避免SFT的灾难性遗忘，又比带可验证奖励的RL（RLVR）样本效率更高，但实际训练时存在严重的优化不稳定问题，核心瓶颈是师生模型的能力差导致对数概率奖励无下界，梯度方差爆炸，现有缓解方法都是经验启发式，缺乏理论保证。

### 方法关键点
- 外部近端教师：将目标教师和当前学生的概率分布插值生成动态近端教师，把原来无下界的OPD reward转换为严格下界的平滑奖励$	ilde{r}_k = log(\alpha \rho_k + 1-\alpha)$，无需显式构造近端教师，零额外计算开销
- 内部信任域迭代：解耦行为策略和目标策略，支持离策略数据复用，采用token级优势归一化，避免生成长度偏差，同时保证策略单调提升
- 理论层面严格证明了梯度方差有界、全局收敛、策略单调提升三大特性

### 关键结果
在数学推理任务上验证，以Qwen3-30B为教师，8B学生模型在AIME24基准上avg@32准确率达50.42%，较标准OPD提升25.84个百分点，较SOTA RLVR方法DAPO提升17.5个百分点；1.7B小模型在AIME24上较OPD提升11.35个百分点，α取值在0.1-0.3区间效果鲁棒性极强。

### 核心结论
TOP-D是完全即插即用的OPD drop-in替换方案，零额外开销就能同时实现训练稳定性、样本效率、最终效果的三重提升，且具备完整理论收敛保证
