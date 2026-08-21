---
title: 'Pandora''s AI Model Routing Box: Efficient Allocation with Costly Value Estimation'
title_zh: 潘多拉AI模型路由框架：带价值估计成本的高效分配方案
authors:
- Adam Fisch
- Shubhendu Trivedi
- Fantine Huot
- William W. Cohen
- Michael Kaisers
- Mirella Lapata
- Kate Larson
- Jacob Eisenstein
affiliations:
- Google DeepMind
arxiv_id: '2608.20316'
url: https://arxiv.org/abs/2608.20316
pdf_url: https://arxiv.org/pdf/2608.20316
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: Agent路由 · 成本-精度权衡
tags:
- Model Routing
- Value of Information
- Multi-LLM
- Decentralized Agent
- Pandora's Box
one_liner: 将经典潘多拉盒问题引入多模型路由，实现带价值估计成本权衡的集中式与分布式路由策略
practical_value: '- 多召回源/多模型排序场景可直接复用框架：先用embedding KNN做廉价预打分，通过预留价格阈值判断是否调用昂贵的精排模型，在精度损失可忽略的前提下最大幅降低推理成本

  - Agent工具调用决策可套用闭形式信息价值计算：判断是否需要调用RAG、计算器等工具时，基于高斯信号模型计算阈值，比人工规则更能自适应成本波动

  - 跨团队分布式能力调度场景可借鉴Pandora''s Bidder逻辑：每个服务/Agent自主决定是否投入成本做自我能力评估，无需中央路由全量采集信息，降低系统耦合'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多模型/多专家路由方案默认价值估计无成本，忽略了廉价估计（如embedding KNN）噪声大、精准估计（如微调打分模型、预跑推理片段）成本高的矛盾，无法动态权衡估计成本与路由收益，导致要么精度不足要么推理成本过高。
### 方法关键点
- 将带成本的价值估计路由问题抽象为非强制开箱的经典潘多拉盒问题，每个专家对应一个盒子，开箱成本对应精准价值估计的开销
- 基于高斯信号模型推导闭形式的信息价值表达式，计算每个专家的预留价格（开箱收益与成本平衡的阈值），按预留价格降序决定是否调用精准估计，提前终止无收益的估计流程
- 扩展到分布式场景的Pandora's Bidder：专家基于当前竞价阈值自主判断是否投入成本做自我评估，适配无中央路由的多Agent竞价场景
### 关键结果
在Math（1.6万道数学推理题）、RAG（混合通用+生物医疗QA）、EmbedLLM（多LLM路由基准）三个数据集测试，对比f-only、g-always、Top-2等基线：
- Pandora's Router在三个数据集上的总损失（路由遗憾+估计成本）分别为0.105、0.118、0.386，比全量调用精准估计的g-always分别降本18%、16%、83.6%，同时精度几乎持平
- 分布式场景下Pandora's Bidder在全成本区间内始终跟踪最优基线下限，比静态策略平均提升12%的代理收益

最值得记住的一句话：任何带成本的决策前都要先计算信息价值，不要为了提升一点点精度付出远超收益的估计成本。
