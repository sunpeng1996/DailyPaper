---
title: Learning to Refer from Estimated Listener Gaze
title_zh: 基于预估听众注视行为的指代表达生成学习
authors:
- Téa Wright
- Alane Suhr
affiliations:
- University of California, Berkeley
arxiv_id: '2609.14207'
url: https://arxiv.org/abs/2609.14207
pdf_url: https://arxiv.org/pdf/2609.14207
published: '2026-09-13'
collected: '2026-09-15'
category: Multimodal
direction: 多模态指代生成 · 隐式交互信号训练
tags:
- Vision-Language Model
- Referring Expression Generation
- Reinforcement Learning
- Implicit Feedback
- Gaze Signal
one_liner: 利用预估的听众注视路径作为奖励信号微调视觉语言模型，生成更简洁高效的最优指代表达
practical_value: '- 电商搜索/导购Agent生成商品指代文案时，可复用「将用户隐式行为（如眼球注视、点击停留序列）转化为token/序列级奖励」的思路，优化文案的简洁性与准确率

  - 生成式推荐的item文案生成场景，可借鉴将用户实时交互过程信号作为RLHF的补充奖励，不用仅依赖最终点击/转化显式反馈，降低训练数据门槛

  - 多模态对话Agent的指代任务，可直接复用「先训练预估用户行为的listener模型，再用其输出奖励优化speaker生成策略」的两阶段训练架构'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有指代表达生成（REG）仅依赖最终通信成功的显式信号优化，未利用听众理解过程的隐式交互信号，生成的表达冗余度高、指代准确率不足，难以满足实用场景的效率要求。

### 方法关键点
1. 微调视觉语言模型作为speaker生成策略，输入图像+目标指代对象，采样生成候选指代表达；
2. 预训练神经listener模型模拟人类注视行为，输入图像+候选指代表达输出对应注视扫描路径，每个注视点映射到表达中的一个token；
3. 基于注视序列与目标指代的匹配度，构造token级、序列级奖励，用强化学习迭代优化speaker的策略参数。

### 关键结果
人类听众测评显示，优化后模型相比基线：指代表达平均长度从15.4词降至4.0词，指代成功率从75.2%提升至80.0%，实用最优性显著提升。
