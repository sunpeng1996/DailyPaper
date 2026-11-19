---
title: On Evaluating User Simulators for Interactive Agents
title_zh: 面向交互式Agent的用户模拟器元评估与评测套件
authors:
- Hengguang Zhou
- I-Hung Hsu
- Li Chen
- Priyanshi Shrivastava
- Anastasios Angelopoulos
- Wei-Lin Chiang
- Ion Stoica
- Cho-Jui Hsieh
affiliations:
- UCLA
- Arena
arxiv_id: '2611.24892'
url: https://arxiv.org/abs/2611.24892
pdf_url: https://arxiv.org/pdf/2611.24892
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent 仿真评估 · 用户模拟器评测
tags:
- User Simulator
- Agent Evaluation
- Meta-Evaluation
- Interactive Agent
- LLM Agent
one_liner: 设计扰动驱动的用户模拟器元评估框架与三层评测套件，覆盖全部10类常见仿真失效
practical_value: '- 做电商导购Agent、个性化推荐交互仿真时，可复用该研究的10类扰动构造方法，验证自有用户模拟器的可靠性，避免指标漏判模拟器偏差（如过度接受低质推荐、偏向特定策略）

  - 三层评估框架可直接落地到用户模拟器选型流程：先校验L1排序一致性（仿真测的Agent/策略排名是否与真实用户一致），再校验L2群体行为匹配度，最后校验L3单轨迹意图/persona保真，规避模拟器「太友好」导致的效果高估

  - 做仿真数据过滤时，优先选用L1排序一致性+L3 persona一致性组合，该组合在5%扰动漏过率下可保留98%的正常仿真数据，性能是现有最优方案的9.8倍'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
交互式LLM Agent（如导购Agent、编码Agent）的规模化评估高度依赖用户模拟器降低人力成本，但现有用户模拟器的评估指标存在大量盲区：仿真用户可能对话自然却接受不合格结果、偏向特定Agent，导致Agent评测结果失真，现有方案无法有效识别这类失效。

### 方法关键点
- 设计扰动驱动的元评估框架：人工构造10类真实存在的用户模拟器失效（包括目标篡改、移除约束、提前终止、偏向特定Agent、无条件接受低质输出等），测试评估指标是否能准确惩罚这些扰动
- 推出三层全覆盖评估套件：① L1下游排序一致性：验证用模拟器得到的Agent排序与真实用户参考排序的匹配度；② L2群体级保真度：对比仿真与真实用户的行为分布、交互动态、错误敏感度、信息贡献比例；③ L3轨迹级保真度：检查单条交互是否保留原始用户的目标、约束、persona

### 关键结果
- 对比3个主流现有评估套件（SimulatorArena、VISTA、SWE-Together），现有方案仅能检测5~6类扰动，甚至会给接受低质输出的扰动模拟器更高评分；这套评估套件可100%检测全部10类扰动
- 过滤实验中，这套方案在5%扰动样本漏过率下，可保留98%的正常仿真群体，是现有最优方案的9.8倍；轨迹级过滤下可保留68%的真实用户轨迹，是现有最优方案的2.4倍
- 评测6款主流用户模拟器，无一款在三个层面全部领先：SimulatorArena的L1排序一致性最高，配套的profile驱动模拟器在L2、L3保真度上最优

### 核心结论
用户模拟器评估不能仅看对话自然度，必须同时校验排序一致性、群体行为匹配度和单轨迹意图保真，否则会严重高估Agent的真实业务效果。
