---
title: Measuring the collaboration, not the agent
title_zh: 人机高维可视化分析评估框架：评估协作效果而非单一Agent能力
authors:
- Xinxiao Li
- Eisei Nakahara
affiliations:
- Shonan Institute of Technology
- Nihon University
arxiv_id: '2611.06487'
url: https://arxiv.org/abs/2611.06487
pdf_url: https://arxiv.org/pdf/2611.06487
published: '2026-11-04'
collected: '2026-11-07'
category: Eval
direction: 人机协作Agent评估框架
tags:
- Human-AI Collaboration
- Evaluation Metric
- Visualization Agent
- Interaction Log
- Testbed
one_liner: 提出5项人机协作可视化Agent评估指标，4项可仅通过交互日志计算并配套开源测试床
practical_value: '- 电商智能运营/可视化分析Agent评估可复用「仅从交互日志计算指标」的思路，无需额外标注即可量化人机协作效率

  - 可复用互补性、干预效率、合理依赖度、知识留存4项指标，评估推荐系统/Agent与人工运营的协作效果，适配人工干预推荐策略的业务场景

  - 做Agent上线前验证时，可引入模拟用户/模拟运营的测试床方法，先在可控环境下验证策略有效性，降低线上实跑风险'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有可视化Agent Benchmark仅单独评估Agent能力，高维数据分析场景下核心领域知识由一线专家掌握，单独评测Agent无法反映人机协作的实际业务价值。
### 方法关键点
聚焦「Agent输出可视化方案→分析师接受/拒绝/修改→反馈留存复用」的协作范式，提出5项量化评估指标：互补性、干预效率、合理依赖度、知识留存、自主权，其中前4项可完全基于交互日志计算，无需额外标注成本。
### 关键结果
在UCI SECOM公开制造数据集的平行坐标设计测试床中，采用行为可控的模拟分析师验证，4项日志类指标全部可计算，且能敏感响应协作模式的受控差异，目前已开源对应测试床供后续真人验证使用。
