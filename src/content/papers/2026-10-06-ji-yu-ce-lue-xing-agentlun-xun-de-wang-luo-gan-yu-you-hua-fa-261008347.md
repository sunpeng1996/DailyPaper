---
title: Network Intervention by Polling Strategic Agents
title_zh: 基于策略性Agent轮询的网络干预优化方法
authors:
- Chenyu Zhang
- Rohit Parasnis
- Saurabh Amin
affiliations:
- MIT
- IIT Bombay
arxiv_id: '2610.08347'
url: https://arxiv.org/abs/2610.08347
pdf_url: https://arxiv.org/pdf/2610.08347
published: '2026-10-06'
collected: '2026-10-07'
category: MultiAgent
direction: 多智体网络 · 干预策略优化
tags:
- MultiAgent
- NetworkGame
- MechanismDesign
- DistributedOptimization
- IncentiveCompatibility
one_liner: 给出兼顾计算/学习/经济效率的Poll轮询算法，实现大规模网络策略Agent的最优干预定价
practical_value: '- 电商平台做品类补贴、创作者流量激励等全局策略设计时，可复用Poll的随机游走局部采样架构，无需全量采集商家/创作者的私有成本数据，大幅降低通信和存储开销，性能接近最优解

  - 应对策略性用户/商家的谎报薅羊毛问题，可借鉴「混合真假信号+利用网络结构信息模糊性」的思路，无需额外支付激励成本即可诱导真实上报，适合大促补贴、流量激励等高频场景

  - 分布式多Agent系统全局优化时，可复用其异质性感知的查询逻辑，根据用户/Agent的偏好异质性、网络异质性动态调整采样量，平衡优化效果和计算资源开销'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
大规模网络下的策略Agent干预（如政府研发补贴、平台用户激励政策制定）存在三大核心痛点：最优策略依赖Agent私有信息无法直接获取、被查询Agent可能谎报引导结果偏向自身利益、全量计算复杂度随Agent规模激增无法落地。现有方法要么假设已知网络结构或Agent私有信息，要么未考虑策略性谎报问题，无法适配真实大规模场景。
### 方法关键点
- 将最优价格问题转化为Katz-Bonacich中心性分解形式，每个Agent的贡献与其在偏好加权网络中的中心性平方成正比，无需全局网络信息即可建模
- Poll轮询算法流程：每轮随机采样1个Agent，从该节点发起两条独立随机游走，仅聚合游走路径及端点的局部报告更新价格，Agent无需存储全局状态，也无需上报原始私有数据
- 三类效率保障：计算上仅需O(tm²)操作，与Agent规模无关；学习上查询复杂度仅依赖网络和偏好异质性，不随Agent数量线性增长；经济上通过发送混合真假信号，利用网络结构带来的信息模糊性诱导Agent真实上报，无需额外激励成本
### 关键实验
在包含31.7万节点的DBLP合著网络上测试，对比Gossip、Federated、Consensus等分布式基线，达到1e-5福利缺口时，Poll的通信量比基线低316~1572倍；面对策略性Agent时，设计合理的诱饵信号即可将上报偏差控制在不影响收敛效率的范围内。
### 核心结论
大规模多Agent系统的全局优化不需要全量采集信息，结合网络结构的局部采样+激励兼容设计，可在极低开销下接近最优效果
