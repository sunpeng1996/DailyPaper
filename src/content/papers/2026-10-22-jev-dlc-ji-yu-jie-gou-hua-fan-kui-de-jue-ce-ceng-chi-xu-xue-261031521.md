---
title: 'Jev-DLC: Decision-Level Continual Learning from Typed Feedback'
title_zh: Jev-DLC：基于结构化反馈的决策层持续学习框架
authors:
- Yangyang Feng
- Jianle Gan
- Zhuoyan Feng
- Chengwei Qin
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Sun Yat-sen University
arxiv_id: '2610.31521'
url: https://arxiv.org/abs/2610.31521
pdf_url: https://arxiv.org/pdf/2610.31521
published: '2026-10-22'
collected: '2026-10-24'
category: RecSys
direction: 推荐系统 · 结构化反馈驱动持续个性化
tags:
- Continual Learning
- Personalization
- Typed Feedback
- User Modeling
- Online Learning
- RecSys
one_liner: 在冻结基础评分器之上通过双路紧凑状态实现决策层持续个性化，无需重放历史或运行时训练模型
practical_value: '- 可复用双路紧凑状态设计：保守通道存储用户高频偏好计数、响应通道存储偏好修正方向，无需保存原始交互历史，单用户状态仅数百字节，适配大流量推荐/Agent场景的端侧或近线个性化需求

  - 对于支持显式结构化反馈的场景（如电商推荐的「不喜欢并换同类」、Agent工具调用的用户纠错），可直接复用PA-I最小更新规则，每次反馈仅做向量运算，无额外模型前/后向调用，耗时可忽略

  - 可直接借鉴TCPA-BENCH的predict-then-update评估协议，评估持续学习方法的真实在线效果，避免离线评估常见的未来信息泄露问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有个性化方法要么需重放历史交互增大推理开销，要么微调模型引入稳定性-可塑性权衡；而Jev风格结构化接口可直接输出用户「接受/拒绝并指定替代项」的显式反馈，无需从自由文本或隐式行为反推偏好，因此可设计轻量的决策层持续学习方案，完全冻结基础模型，仅用紧凑状态承载用户偏好。
### 方法关键点
- 基础层：冻结预训练JEV-SFT评分器，输出候选的基础logit和语义表征，通过固定线性投影降维到32维空间
- 双路状态通道：保守通道融合用户偏好动作的频次先验+偏好修正向量，适配高频重复决策场景；响应通道仅存修正向量，适配新场景偏好迁移
- 更新规则：采用PA-I被动-aggressive算法做最小变化更新，仅当当前决策不符合反馈时调整状态，且单次更新步长设上限避免状态漂移
- 通道融合：根据两个通道的历史预测准确率自适应加权输出，权重用指数更新保证稳定性
### 关键实验
在TCPA-Repeat（基于LaMP-2构建的重复决策数据集）上，Jev-DLC整体用户宏准确率达44.83%，较冻结基线高5.39个点，较Recent-4历史重放方法高2.43个点；收到至少2次反馈后准确率达56.07%，较最优基线高7.54个点；单用户状态仅324字节，单次状态更新耗时<0.1ms，无额外模型调用。
### 核心结论
结构化显式反馈可直接转化为紧凑决策状态，无需重放历史或运行时训练模型即可实现高效持续个性化
