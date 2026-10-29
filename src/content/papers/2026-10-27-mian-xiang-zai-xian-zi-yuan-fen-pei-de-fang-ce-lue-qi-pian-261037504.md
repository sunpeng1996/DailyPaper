---
title: Strategyproof Deep Reinforcement Learning for Online Resource Allocation
title_zh: 面向在线资源分配的防策略欺骗深度强化学习机制
authors:
- Fariba Dehghan
- Sebastian Stein
- Vahid Yazdanpanah
- Stephanie Gauthier
affiliations:
- University of Southampton
arxiv_id: '2610.37504'
url: https://arxiv.org/abs/2610.37504
pdf_url: https://arxiv.org/pdf/2610.37504
published: '2026-10-27'
collected: '2026-10-29'
category: MultiAgent
direction: 多智能体资源分配 · 防策略机制设计
tags:
- Strategyproofness
- Reinforcement Learning
- Online Resource Allocation
- Imitation Learning
- Neural Mechanism Design
one_liner: 提出首个防策略欺骗的深度RL在线资源分配机制，性能显著优于现有线性与启发式方案
practical_value: '- 电商广告流量坑位、直播资源位等稀缺资源分配场景可复用构造性单调网络设计，在保障商家报价真实的前提下提升资源利用率

  - 冷启动阶段可借鉴「模仿现有规则预训练 + RL 微调」范式，比纯 RL 训练提速近90倍，大幅降低落地成本

  - 广义临界支付规则可直接迁移到竞价类广告系统，消除参与者虚报估值/需求的动机，同时保证分配效率最优'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
在线稀缺资源分配面临两大耦合挑战：不确定未来需求下的高效分配难，无法保证参与Agent上报估值、需求的真实性（防策略性）；现有策略鲁棒RL仅支持线性分配规则表达能力有限，神经机制设计仅能提供近似激励保证。
### 方法关键点
集成三类创新组件：① 构造性单调神经网络，天然满足「报价越高接受概率越高、需求/时长越高接受概率越低」的单调性约束；② 广义临界支付规则，固定其他输入时取最低可接受报价作为支付额；③ 支持纯RL或模仿现有规则两种训练模式。单调性+临界支付天然保障防策略性与个体理性。
### 关键结果
在4类资源、2组伙伴配对的非线性场景下，方案达到离线最优福利上界的97.8%，较线性RL（93.8%）、先到先得（89.0%）分别缩小65%、80%的最优性差距；模仿学习训练仅需261秒即可达到97.5%性能，速度是纯RL的89倍。
