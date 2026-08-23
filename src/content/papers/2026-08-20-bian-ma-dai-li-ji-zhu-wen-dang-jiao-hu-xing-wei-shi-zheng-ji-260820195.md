---
title: 'From Agent Behaviour to Agent-Friendly Documentation: An Empirical Study of
  How Coding Agents Discover, Read, and Write Technical Documentation'
title_zh: 编码代理技术文档交互行为实证研究及代理友好文档优化方向
authors:
- Zhijun Gao
- Jing Chen
affiliations:
- Peking University
arxiv_id: '2608.20195'
url: https://arxiv.org/abs/2608.20195
pdf_url: https://arxiv.org/pdf/2608.20195
published: '2026-08-20'
collected: '2026-08-23'
category: Agent
direction: Agent 编码代理行为实证研究
tags:
- Agent
- Coding Agent
- Empirical Study
- Documentation
- Behaviour Analysis
one_liner: 基于两组大规模编码代理行为数据集，揭示文档交互规律，推翻代理友好文档的主流假设
practical_value: '- 搭建业务编码Agent时，优先配置Agent专属指令文件、工作笔记类物料，比传统技术文档、API参考的调用率高5倍以上

  - 设计Agent工作流无需强制「先查文档再编码」的线性流程，数据显示70%+文档查询为主动触发，且代码修改先于文档更新的概率高4.7倍

  - 无需盲目对齐行业流传的「可行动、可验证」代理友好文档标准，该类假设无实际行为数据支撑

  - 做Agent行为分析时可复用本文的事件分类、交互建模pipeline，提升埋点与分析效率'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有技术文档均面向人类开发者设计，编码Agent的文档交互行为规律尚不明确，行业普遍认可的「代理友好文档」核心属性缺乏实证支撑。
### 方法
基于两组公开数据集开展行为分析：SWE-chat的557次编码会话，包含94813个开发事件、3033次文档交互；AIDev的33097个Agent提交的PR，包含690260条分类文件变更记录。
### 关键结果
1. Agent文档交互中60.5%为代理专属指令、工作笔记，传统技术文档仅占10.6%，API参考仅占1.3%；
2. 文档查询后紧接代码编辑的概率仅0.002，阶段调整后OR值为1.33；
3. 未观测到基于文档的显式验证序列，文档查询后即时测试的lift为0.23；
4. 70.2%的文档查询为主动触发，仅7.5%为失败驱动，多commit PR中代码先于文档修改的概率高4.7倍。
研究推翻了「代理友好文档需具备可行动性、可验证性」的主流假设，提出双叶循环的Agent-文档交互模型。
