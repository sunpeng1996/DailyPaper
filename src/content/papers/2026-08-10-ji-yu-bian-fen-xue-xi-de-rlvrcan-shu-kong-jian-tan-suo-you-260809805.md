---
title: Parameter Exploration for RLVR via Variational Learning
title_zh: 基于变分学习的RLVR参数空间探索优化方法3PO
authors:
- Vatsal Venkatkrishna
- Nico Daheim
- Iryna Gurevych
affiliations:
- INSAIT, Sofia University
- Technical University of Darmstadt
- National Research Center for Applied Cybersecurity ATHENE
arxiv_id: '2608.09805'
url: https://arxiv.org/abs/2608.09805
pdf_url: https://arxiv.org/pdf/2608.09805
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: LLM RLVR训练优化 · 参数空间探索
tags:
- RLVR
- Parameter Exploration
- Variational Learning
- GRPO
- LLM Training
one_liner: 提出参数空间扰动的3PO系列方法，同等FLOPs下提升RLVR训练性能与探索效率
practical_value: '- 面向导购Agent、文案生成等需要RL微调的业务场景，可替换原有AdamW+温度缩放的探索方案，用IVON加参数扰动实现探索，减少高温度带来的无效生成，降低调参成本

  - GRPO训练遇到零advantage组停滞问题（如RL优化排序策略时同组样本reward一致无梯度），可复用C3PO分块扰动思路，拆分rollout给多组扰动参数生成，提升组内多样性，持续获取学习信号

  - 落地超参参考：参数扰动的ESS λ默认选1e9，训练崩溃则升到1e10，训练停滞则降到1e8，无需额外预训练噪声先验，直接初始化常数Hessian即可生效'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有RLVR的探索方案均在动作空间实现（如温度缩放），仅能调整token分布方差无法改变相对排序，易生成无效内容；且GRPO训练经常出现同组所有rollout reward一致的零advantage组，导致训练停滞、算力浪费，亟需更高效的探索范式。

### 方法关键点
- 基于变分学习的IVON优化器，训练时给模型参数加可学习高斯噪声，从参数posterior采样不同策略生成rollout，实现参数空间探索，和现有动作空间探索方法正交兼容
- 推出3种扰动策略：B3PO每步采1组扰动参数生成所有rollout；M3PO采M组参数分别计算GRPO损失后平均梯度更新；C3PO将每组GRPO的G个rollout拆分给N组扰动参数生成，再合并计算advantage，最大化组内多样性
- 所有方法无需预训练噪声先验，直接初始化常数Hessian即可落地，算力成本和标准GRPO接近

### 关键结果
基于OLMo-3-7B、Qwen2.5-Math-7B在数学推理、代码生成任务测试，对比GRPO、熵正则、Polaris等动作空间探索基线：
- C3PO在数学推理任务平均Pass@1比GRPO高1.05~1.52pct，难度更高的AIME数据集最高提升5.83pct；代码生成任务LiveCodeBench得分比GRPO高2.17
- 3PO系列方法比基线多拯救30%+的零advantage组，生成的无效/错误rollout比GRPO少20%以上

### 核心结论
参数空间探索是比动作空间探索更高效的LLM RL训练优化方向，仅需少量工程修改即可获得显著收益。
