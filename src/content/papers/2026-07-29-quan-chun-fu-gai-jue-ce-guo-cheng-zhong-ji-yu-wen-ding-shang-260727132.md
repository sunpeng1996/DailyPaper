---
title: Minimal Markovization via Stable Quotients in Holonomy-Cover Decision Processes
title_zh: 全纯覆盖决策过程中基于稳定商的最小马尔可夫化方法
authors:
- Zuyuan Zhang
- Yongshan Chen
- Mahdi Imani
- Tian Lan
affiliations:
- The George Washington University
- Northeastern University
arxiv_id: '2607.27132'
url: https://arxiv.org/abs/2607.27132
pdf_url: https://arxiv.org/pdf/2607.27132
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: Agent 部分可观测环境状态压缩
tags:
- POMDP
- Reinforcement Learning
- State Abstraction
- Memory Efficiency
- Markov Representation
one_liner: 为结构化部分可观测决策过程提出最小马尔可夫统计量及高效强化学习框架
practical_value: '- 电商推荐/广告的用户隐意图建模可借鉴稳定商粗化思路，对同当前观测下的隐状态做最小聚合，大幅降低历史记忆存储开销，同时不损失决策最优性

  - 若业务支持小流量校准探测试验，可复用文中最近原型类推断方法，隐状态识别误差随探针次数指数级下降，快速实现状态跟踪同步

  - 处理用户行为序列依赖时需避免滥用计数类特征，非交换序列（如先加购后浏览vs先浏览后加购）需采用有序传输跟踪方法更新状态，避免信息损失'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
部分可观测环境下，现有RL方案存在明显落地缺陷：信念状态是连续分布维度极高，RNN/Transformer等历史编码方案无法严格保证输出的马尔可夫性，也无法实现记忆量的最小化。而大量真实业务决策场景（如电商用户行为建模、广告投放决策）都符合一类结构化POMDP特性：可见状态转移满足马尔可夫性，隐模式仅随观测转移做固定置换，针对这类场景找到最小马尔可夫充分统计量，可在保证决策效果的前提下大幅降低工程开销。
### 方法关键点
- 定义稳定商迭代算子：从按奖励划分的初始隐状态分区开始迭代细化，仅保留对后续单步奖励和转移有影响的隐状态差异，得到最粗的观测级抽象，和当前观测组成精确有限马尔可夫状态
- 提出全纯记忆强化学习（HMRL）框架：用稳定类表示记忆，通过有序边传输规则更新状态；支持可重置校准探针场景下的最近原型类推断，状态同步后直接对接标准有限MDP的RL主干
- 证明非交换隐转移场景下，计数类记忆（如操作次数统计）存在固有信息损失，必须采用有序状态跟踪才能保证决策最优
### 关键实验结果
- ChainCover环境：216个原始状态被压缩到25个商状态，无奖励、转移、最优值误差
- LoopGuess环境：HMRL最终成功率1.000，配对顺序准确率1.000，仅用3个决策时记忆状态，性能与商神谕完全持平；计数类记忆基线配对顺序准确率仅0.342，接近随机水平，全量历史编码基线需占用超1000个记忆状态
### 核心结论
部分可观测场景下的最小记忆状态不需要存储全量历史，仅需保留对未来决策有影响的隐状态等价类，有序转移跟踪的信息效率远高于计数类特征
