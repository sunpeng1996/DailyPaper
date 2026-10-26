---
title: Recommender regret for improving regularised RL estimation with bandits and
  MCTS
title_zh: 基于推荐器后悔度优化结合老虎机与MCTS的正则化RL估计
authors:
- Danilo Vucetic
- Alexandre Larouche
- Mohammad Pedramfar
- Audrey Durand
- Gauthier Gidel
affiliations:
- Université de Montréal
- Université Laval
- Mila - Québec AI Institute
- McGill University
- CIFAR AI Chair
arxiv_id: '2610.32910'
url: https://arxiv.org/abs/2610.32910
pdf_url: https://arxiv.org/pdf/2610.32910
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent决策优化 · MCTS与老虎机算法
tags:
- ReinforcementLearning
- MCTS
- MultiArmedBandit
- RegularizedRL
- RegretMinimization
one_liner: 提出正则化RL下的推荐器后悔度框架，证明均匀采样达最优下界并设计推荐器MCTS
practical_value: '- 业务中使用MCTS做决策（如电商广告动态出价、推荐冷启动探索）时，样本量充足场景优先选均匀采样作为探索策略，比E3W等贪心探索收敛更快、估计误差更低

  - 做正则化RL的目标估计时，可复用本文提出的正则器感知推荐器后悔度作为评估指标，避免仅评估采样效率带来的与下游效果脱节问题

  - 序列生成类业务（如电商营销文案生成、多步商品搭配推荐）可将推荐器MCTS作为base模型的后处理增强模块，提升生成结果的多样性和top-k质量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有正则化RL的估计框架（如MCTS、单步前瞻）仅评估采样效率，不衡量生成的policy、value、Q值估计的质量，缺乏最优采样预算分配的理论指导，导致估计结果与下游任务效果脱节，无法满足高可靠决策场景的需求。
### 方法关键点
- 定义正则器感知的推荐器后悔度（SRR），分别针对policy、value、Q值三类目标设计适配的散度度量，推导各类SRR的理论下界，证明均匀采样可达到最优上界，传统贪心采样（如E3W）的上界更松。
- 扩展推荐器后悔度到树搜索场景，提出推荐器MCTS，推导其在确定性转移下的后悔度集中性和期望上界，明确均匀采样在MCTS估计中的最优性。
### 关键实验
在三类任务上验证效果：
1. 合成树实验：均匀采样MCTS的Q值估计误差比E3W低20%~50%，随模拟次数增加收敛速度显著更快。
2. OCTAX 19款街机游戏实验：正则化MCTS比无搜索基线的 episodic return 提升30%~120%；高模拟量下均匀采样与E3W效果相当，低模拟量下E3W表现更优。
3. 生物序列设计实验：推荐器MCTS比基线TGM模型的top-100多样化奖励提升2%~15%，均匀采样几乎全面优于E3W。
### 核心结论
正则化RL的估计优化中，推荐任务需要纯探索而非最小化探索，均匀采样在多数场景下是性价比极高的采样策略
