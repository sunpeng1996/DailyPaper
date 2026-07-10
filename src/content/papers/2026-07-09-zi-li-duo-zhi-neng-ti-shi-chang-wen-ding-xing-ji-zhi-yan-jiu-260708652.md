---
title: 'Formal Mechanisms for Market Stability in Self-Interested Agent Societies:
  A Marketplace Simulation Study'
title_zh: 自利多智能体市场稳定性机制研究：基于LLM交易市场仿真
authors:
- Eugene Ng Yi Sheng
- Bingquan Shen
affiliations:
- DSO National Laboratories
- National University of Singapore
arxiv_id: '2607.08652'
url: https://arxiv.org/abs/2607.08652
pdf_url: https://arxiv.org/pdf/2607.08652
published: '2026-07-09'
collected: '2026-07-10'
category: MultiAgent
direction: 多智能体市场治理 · 对抗鲁棒性
tags:
- MultiAgent
- LLM Agent
- Mechanism Design
- Adversarial Robustness
- Market Simulation
one_liner: 通过两阶段多智能体交易仿真验证中介机制为对抗恶意攻击最稳定的市场治理方案
practical_value: '- 电商多Agent交易/撮合系统可直接复用Mediation机制：交易双方委托中立执行层完成交割，完全规避违约风险，比事后惩罚/合约机制摩擦更低、鲁棒性更高

  - 对抗恶意刷量/欺诈用户场景可借鉴v6攻击思路做红蓝对抗：锚定真实行为构造不可证伪的意图误导+高容量无效请求挤占资源，提前检验系统鲁棒性

  - 多Agent协作系统设计优先选择「事前预防」类机制而非「事后惩罚」类，低摩擦、无额外成本的机制 adoption 率远高于多步骤、有惩罚风险的机制

  - 做Agent治理仿真实验可复用文中渐进式恶意Agent注入框架，分阶段验证不同机制的抗攻击能力和恢复能力'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent越来越多应用在交易、资源分配等经济场景，自利Agent天然倾向于背叛合作，无约束下会导致交易收益崩塌，现有机制缺乏在复杂交易场景下的抗攻击能力验证，亟需明确哪种正式机制可维持市场稳定、对抗恶意攻击。

### 方法关键点
- 构造18个DeepSeek-V3驱动的自利Agent交易仿真环境：分3类专精不同商品的Agent，仅能和邻居交易，商品易腐必须高频交换，背叛可直接抢夺对方商品，仅靠通信无法约束行为
- 两阶段实验设计：第一阶段对比8类治理机制（通信基线、全局声誉、合约、中介、治理、网络重连、惩罚、司法），渐进注入硬编码恶意背叛Agent测试韧性；第二阶段对最优机制做迭代优化的LLM驱动红队攻击，测试对抗鲁棒性
- 核心指标为诚实Agent累计效用、基尼系数，定义对抗鲁棒性为最优攻击下仍能维持诚实Agent正效用

### 关键结果
- 第一阶段：中介机制累计效用1556，比通信基线高29%，比第二名网络重连高15%，是唯一随恶意Agent注入效用仍上升的机制
- 第二阶段：最优v6双向量攻击（不可证伪的离间消息+诱饵请求挤占资源）仅使诚实Agent效用下降13.3%，仍维持正效用，未发生市场崩塌

**最值得记住的一句话**：自利多智能体市场治理中，事前预防类的低摩擦机制（如托管中介）远优于事后惩罚类机制，可被击弯但绝不会被击穿。
