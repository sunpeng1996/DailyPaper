---
title: 'A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference
  Resets'
title_zh: 大模型后训练策略优化理论：覆盖崩溃问题与参考重置解法
authors:
- Audrey Huang
- Nan Jiang
- Sham M. Kakade
- Sadhika Malladi
- Akshay Krishnamurthy
- Dylan J. Foster
affiliations:
- Harvard University
- UIUC
- University of California San Diego
- Microsoft Research NYC
arxiv_id: '2611.14467'
url: https://arxiv.org/abs/2611.14467
pdf_url: https://arxiv.org/pdf/2611.14467
published: '2026-11-10'
collected: '2026-11-11'
category: Training
direction: 大模型后训练 · 策略优化理论
tags:
- Policy Optimization
- Post-Training
- RLHF
- Coverage Collapse
- Reference Reset
- PPO
one_liner: 揭示REINFORCE类算法的覆盖崩溃问题，提出带参考重置的APMD框架保证后训练高效收敛
practical_value: '- 做LLM驱动的推荐/Agent RLHF调优时，放弃固定基模型为KL参考的做法，定期将KL参考重置为当前最新策略，可避免优质候选（推荐文案、商品、Agent回复）的生成概率被压低，大幅缩短训练收敛周期，消除训练
  plateau

  - 调优PPO/GRPO时，裁剪阈值要与KL正则强度联动：正则越强，裁剪区间越窄，既能控制重要性权重的统计噪声，又不会破坏最优解的学习，适合电商场景冷启动后训练的快速调参

  - 采用平方损失类后训练算法（如KimiPO）时可按需选择基线：算力有限选均值基线配强正则，采样资源充足选归一化基线配更多样本，适配电商个性化文案生成、推荐prompt调优等不同场景的后训练需求

  - 生成式推荐/Agent训练过程中可新增「优质候选覆盖度」监控指标，一旦覆盖度低于基模型的1/2立刻触发参考重置，避免无效训练开销'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM后训练的策略优化算法（如PPO、GRPO）缺乏理论指导，调参高度依赖试错，且基于REINFORCE的算法哪怕增加固定基模型的KL正则，仍会出现**覆盖崩溃**：基模型原本能生成的最优响应/候选的概率在训练中被压低到指数级水平，导致梯度信号消失，收敛需要指数级步数，现有理论未解决该后训练特有的问题。
### 方法关键点
1. 定义「覆盖保留」算法标准：收敛所需样本量与梯度步数仅由基模型的最优响应覆盖度决定，不受训练过程中覆盖度下降的影响
2. 提出APMD（近似策略镜像下降）元算法框架：核心是周期性将KL正则的参考策略重置为当前最新策略，每次迭代仅在当前参考的KL邻域内做局部优化，既避免覆盖崩溃，又能逐步收敛到全局最优
3. 证明带参考重置的PPO/GRPO变体、KimiPO、Rebel-OnPolicy等主流后训练算法均为APMD实例，均满足覆盖保留的收敛保证
4. 明确PPO裁剪的核心作用是控制重要性权重的统计成本，而非直接优化，需与正则强度联动设置
### 关键结果
固定参考的REINFORCE类算法收敛步数为$exp(\Omega(1/\sqrt{\varepsilon}))$，APMD类算法收敛步数降至$poly(1/\varepsilon)$，避免指数级开销；基模型覆盖度$C_{base} \leq 6$的场景下，REINFORCE会出现覆盖崩溃，最优响应概率降至指数级低，而APMD能始终保持最优响应覆盖度不低于基模型的1/2。
### 核心结论
LLM后训练策略优化要避免覆盖崩溃，核心是不要固定KL参考为初始基模型，而是定期重置为当前最新策略，用多次局部优化换取全局高效收敛。
