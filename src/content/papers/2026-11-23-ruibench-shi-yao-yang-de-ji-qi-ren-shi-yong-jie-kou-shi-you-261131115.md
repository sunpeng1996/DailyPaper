---
title: 'RUIBench: What Makes a Good Robot-Use Interface?'
title_zh: RUIBench：什么样的机器人使用接口是优秀的？
authors:
- Yanzhe Chen
- Zhijun Cao
- Zechen Bai
- Wenzheng Zeng
- Kevin Yuchen Ma
- Yiqi Lin
- Guoqiang Liang
- Xiaokang Liu
- Ke Sun
- Kevin Qinghong Lin
affiliations:
- Show Lab, National University of Singapore
arxiv_id: '2611.31115'
url: https://arxiv.org/abs/2611.31115
pdf_url: https://arxiv.org/pdf/2611.31115
published: '2026-11-23'
collected: '2026-11-27'
category: Agent
direction: 具身Agent · 接口设计与评测
tags:
- EmbodiedAgent
- Benchmark
- InterfaceDesign
- ActionAbstraction
- LLM
one_liner: 构建RUIBench评测基准与RUIKit框架，验证RUI设计对具身Agent性能的关键影响
practical_value: '- 电商仓储/物流具身Agent落地可参考RUI设计原则：减少不必要决策分支、保留核心反馈链路，能大幅提升执行成功率

  - Agent调用外部工具/执行器的接口设计可复用RUIKit的分层抽象思路，对齐Agent决策粒度与执行器能力边界，降低执行误差

  - 多模态Agent系统上线前可借鉴RUIBench的任务分层评测逻辑，补充任务级验证模块，解决Agent虚报成功的验证gap问题'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
大模型具备复杂物理任务推理能力，但转化为可靠机器人执行的效果较差，核心被忽视的影响因素是连接Agent决策与机器人执行的机器人使用接口（RUI）。

### 方法关键点
1. 构建RUIBench评测基准，覆盖世界知识、上下文学习、动态交互、高接触操作等5大类共30项典型操作任务；
2. 推出RUIKit统一框架，交叉6种动作抽象与2种交互形式，在统一感知、控制底座下支持13种不同RUI的对比评测。

### 关键结果
仅更换RUI即可让前沿Agent的任务成功率从45%提升至81%，微调4B模型的成功率从13%提升至47%；同时发现存在验证gap：Agent经常在可观测失败的情况下宣告成功，需补充独立于单步动作的任务级校验能力。
