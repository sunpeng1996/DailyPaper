---
title: 'Potential emergence in LLM agents: a statistical physics perspective'
title_zh: 统计物理视角下LLM Agent的势函数涌现现象研究
authors:
- Zhuo-Yang Song
- Hua Xing Zhu
affiliations:
- Peking University
arxiv_id: '2611.27618'
url: https://arxiv.org/abs/2611.27618
pdf_url: https://arxiv.org/pdf/2611.27618
published: '2026-11-20'
collected: '2026-11-23'
category: Agent
direction: LLM Agent可解释性 · 统计物理建模
tags:
- LLM Agent
- Emergence
- Statistical Physics
- Post-Training
- Potential Landscape
- RLHF
one_liner: 提出统计物理配分函数框架量化LLM Agent训练中状态空间的势结构涌现规律
practical_value: '- 做电商客服Agent、推荐话术生成Agent的RLHF/PPO训练时，可将语义等价的输出聚类为有限状态，通过势函数秩序参数r量化策略收敛性，替代部分人工评估成本

  - 微调LLM时可参考论文的校准因子c量化实际训练与理想最优的差距，动态调整每轮KL系数、迭代步数，提升训练效率，减少不必要的算力消耗

  - 若Agent任务奖励与目标状态强相关（如推荐item是否命中用户偏好、检索结果是否满足query需求），可复用奖励-熵联合变化规律监控训练过程，避免熵塌陷同时保证奖励提升'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent的多步推理、决策行为难以通过人类直觉解释，训练后的策略波动、性能变化缺乏可量化的底层理论支撑，已有研究仅停留在语义状态的统计描述，未建立训练目标与状态级行为的量化关联，无法解释RLHF等后训练过程如何重塑Agent的决策逻辑。

### 方法关键点
- 引入统计物理配分函数建模KL正则化RL的状态转移分布，将奖励分解为源状态偏移、目标状态共享奖励、残差三部分，提出秩序参数r量化状态转移对数比与全局势差的匹配度
- 设计两个控制任务：8状态安全测试选择（任意状态可互转）、12状态物理推理步骤选择（仅相邻状态可互转），基于Qwen3.5-9B用LoRA+PPO训练8轮，全程监控势结构、平均奖励、状态熵三个指标
- 通过调整KL系数、模型尺寸、推理温度、prompt变体、奖励结构等变量，验证框架的普适性和边界条件

### 关键结果
- 配分函数预测的转移概率变化与实测值的皮尔逊相关系数，安全测试任务达0.76，物理推理任务达0.89
- 训练后期实测势函数与理论极限的皮尔逊相关系数分别为0.86（安全测试）、0.61（物理推理），秩序参数r从初始的~0.4提升至~0.8
- 仅当奖励包含跨源共享的目标状态项时，训练才会同时出现奖励上升、状态熵下降、势结构增强的一致性变化，单纯奖励提升不足以诱导稳定的势结构

### 核心结论
LLM Agent经过KL正则化的后训练后，状态空间会自发涌现出全局势函数主导决策转移方向，可用于量化评估训练效果和策略稳定性
