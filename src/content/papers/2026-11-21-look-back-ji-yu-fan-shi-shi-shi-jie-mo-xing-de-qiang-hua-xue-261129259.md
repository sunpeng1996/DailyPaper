---
title: 'Look Back: Reinforcement Learning with Counterfactual World Models'
title_zh: Look Back：基于反事实世界模型的强化学习方法RLB
authors:
- Jinwoo Kim
- Toghrul Abbasov
- Lucius E. J. Bynum
- Aahlad Puli
- Stephanie Milani
- Hyunwoo Ryu
- Seunghoon Hong
- Kyunghyun Cho
- Rajesh Ranganath
affiliations:
- KAIST
- NYU
- MIT
arxiv_id: '2611.29259'
url: https://arxiv.org/abs/2611.29259
pdf_url: https://arxiv.org/pdf/2611.29259
published: '2026-11-21'
collected: '2026-11-27'
category: Agent
direction: Agent 强化学习 · 反事实世界模型优化
tags:
- ReinforcementLearning
- CounterfactualReasoning
- WorldModel
- PolicyGradient
- VarianceReduction
one_liner: 提出基于反事实世界模型的RLB策略梯度算法，降低复杂随机环境下梯度估计方差
practical_value: '- 电商/广告动态策略优化（如流量分配、补贴、出价）场景，可复用反事实基线思路：基于历史观测日志固定环境随机因子（如大促流量波动、用户自发行为），仅替换待评估动作生成反事实收益，无需全量建模复杂环境就能降低策略梯度估计方差，提升收敛稳定性

  - 多智能体博弈场景（如广告竞价、多商家推荐流量分配），每个Agent无需建模其他所有参与者的策略，仅基于已观测的其他方行为构造反事实，大幅降低建模复杂度，提升数据效率

  - 生成式推荐的素材/文案迭代场景，可复用扩散世界模型的反事实推理方法：基于已验证效果的素材，固定其他生成噪声仅替换待优化元素（如价格、权益话术），快速生成高置信度候选，避免全量重新生成的随机波动'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
复杂随机环境下的强化学习存在两大痛点：一是普通世界模型需要完整建模环境动态，当环境复杂度超过模型容量时预测误差会快速累积；二是环境随机噪声会掩盖动作的真实效果，导致策略梯度估计方差过高，算法收敛慢甚至无法学习到有效策略。
### 方法关键点
- 定义反事实世界模型（CWM）：基于已观测的真实轨迹作为基准，固定环境潜在随机噪声，仅替换动作预测对应反事实轨迹，相比普通世界模型只需建模动作带来的变化，学习难度显著降低
- 两种CWM构造方案：有配对轨迹（同环境噪声下不同动作的结果）时直接用最大似然训练；无配对数据时基于扩散世界模型做噪声反转，反推观测轨迹对应的潜在噪声后替换动作生成反事实
- 提出REINFORCE Look Back（RLB）策略梯度算法：用CWM生成的多条反事实轨迹的平均收益作为基线，分离动作的真实效果与环境随机噪声带来的收益波动，理论证明满足无偏性，且在环境噪声主导时可降低梯度估计方差
### 关键实验
1. 上下文老虎机任务：环境噪声σ=60时，RLB+CWM的平均reward比RLOO+WM高32，CWM的预测RMSE比普通WM低83%
2. 多智能体老虎机任务：智能体数量K=60时，RLB+CWM的单智能体平均reward比RLOO+WM高27
3. Chrome Dino游戏任务：RLB+CWM的碰撞率为3.77%，比RLOO+WM的7.89%低52%，平均生存时长提升11.8%
### 核心结论
当环境动态复杂度远高于动作带来的变化时，无需完整建模整个环境，基于已观测轨迹做反事实推理即可实现更高效的策略学习
