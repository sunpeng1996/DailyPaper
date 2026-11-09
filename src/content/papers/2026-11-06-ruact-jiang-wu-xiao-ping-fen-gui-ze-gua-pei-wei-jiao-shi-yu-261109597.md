---
title: 'RuACT: Recovering Inactive Rubrics as Adaptive Critics and Teachers'
title_zh: RuACT：将无效评分规则适配为教师与批评家的RL优化框架
authors:
- Yijun Li
- Zhengxi Lu
- Zhipiao Liu
- Jinzheng Yu
- Xutao Weng
- Jian Shao
- Yongliang Shen
affiliations:
- Zhejiang University
- Huawei
arxiv_id: '2611.09597'
url: https://arxiv.org/abs/2611.09597
pdf_url: https://arxiv.org/pdf/2611.09597
published: '2026-11-06'
collected: '2026-11-09'
category: Training
direction: LLM对齐 · 评分规则RL训练优化
tags:
- GRPO
- Rubric-based RL
- RLHF
- Self-Distillation
- Reward Engineering
one_liner: 针对rubric-based RL的无效评分规则问题，自适应分配角色恢复缺失监督信号
practical_value: '- 做垂类Agent/生成式推荐的规则对齐（如文案合规性、应答规范）时，可复用无效规则判定逻辑：全组不满足的规则做引导蒸馏、全组满足的规则做细粒度拆分，避免训练信号浪费

  - 自蒸馏的奖励门控机制可直接迁移：仅当加规则引导的生成结果总奖励超过原生结果时执行蒸馏，避免单一规则优化破坏整体效果

  - 多维度业务指标（如推荐的相关性、合规性、多样性）优化可借鉴饱和规则拆分思路：对低区分度指标拆解为细粒度子项，保留原权重预算的同时提升区分度

  - 该方法在跨域任务上的增益验证了自适应规则复用的可行性，可迁移到电商客服、导购等多场景垂类Agent的对齐任务'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
基于评分规则（rubric）的RL是开放域LLM对齐的主流方案，但在GRPO等组相对优化范式下，Qwen3-4B医学训练中60.88%的query-rubric对会进入无效状态：25.19%为所有采样响应都不满足的不可达规则，35.69%为所有响应都满足的饱和规则，两类规则均无法提供有效梯度，现有重加权、规则更新等方法均无法恢复其监督信号。

### 方法关键点
- 每轮rollout按通过率对rubric做状态判定：通过率0为不可达，0<通过率<1为有效，通过率1为饱和
- **Rubric as Teacher**：对不可达rubric，将其作为特权信息加入prompt生成引导响应，仅当引导响应总奖励超过所有原生响应时，对最优原生响应的token分布做前向KL蒸馏，引导模型推理时无需显式加规则也能满足要求
- **Rubric as Critic**：对饱和rubric生成子规则，筛选出有区分度的子项，父子规则共享原权重预算，既保留原规则权重占比，又恢复奖励区分度
- 有效规则沿用原生GRPO损失，与蒸馏损失联合更新模型

### 关键实验
在医学、科学推理2个领域的4个基准（RaR-Medicine、HealthBench、RaR-Science、ResearchQA）上对比GRPO、Reweight、RuscaRL等基线：
- Qwen3-4B上RuACT在4个基准全部领先，平均得分从GRPO的56.52%提升到59.12%，其中ResearchQA从64.82%提升到69.44%
- 不可达rubric的无引导满足率从35.02%提升到42.86%
- 饱和rubric拆分后，奖励与独立质量评估的对齐度从57.74%提升到60.77%

### 核心结论
rubric无效不代表没有学习价值，针对不可达和饱和两种状态的不同监督缺口分配适配角色，是低成本恢复训练信号的有效方案。
