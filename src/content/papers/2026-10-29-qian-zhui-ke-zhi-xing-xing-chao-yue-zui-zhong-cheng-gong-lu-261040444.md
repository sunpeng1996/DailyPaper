---
title: 'Prefix Executability: Evaluating Tool-Using Agents Beyond Final Success'
title_zh: 前缀可执行性：超越最终成功率的工具调用Agent评估方案
authors:
- Amir H. Rezaeian
- Weiyi Sun
- Yassine Benajiba
- Dan Roth
affiliations:
- Oracle AI
arxiv_id: '2610.40444'
url: https://arxiv.org/abs/2610.40444
pdf_url: https://arxiv.org/pdf/2610.40444
published: '2026-10-29'
collected: '2026-10-30'
category: Eval
direction: 工具调用Agent可靠性评估
tags:
- Agent Evaluation
- Tool Calling
- Trajectory Metric
- Reliability
- LLM Agent
one_liner: 提出前缀可执行性评估体系，弥补仅靠最终成功率评估工具调用Agent的可靠性盲区
practical_value: '- 电商客服/订单处理Agent可直接复用前缀可执行性校验逻辑，每步工具调用前校验schema、依赖、前置条件，避免无效API调用（如提前扣库存、重复发短信等不可逆操作），降低资损

  - 评估现有工具调用Agent时，除最终任务成功率外，补充TER、AUC-PEC两个指标，可更精准识别Agent的中间路径可靠性，尤其是涉及外部交易、资源消耗的场景

  - 可复用Dual-Loop的规划-校验架构，在工具调用执行前增加轻量校验环节，实验显示该架构可在维持最终成功率基本不变的前提下，将TER提升0.6~0.8

  - 前缀可执行性的FED首错定位能力，可直接用于Agent badcase根因分析，快速定位工具调用失败的首因是参数错、依赖缺还是前置条件不满足，降低迭代成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有工具调用Agent的评估仅以最终任务成功率为核心指标，无法感知中间工具调用序列的可执行性：早期无效调用可能导致状态污染、额外资源消耗，甚至大量最终成功的路径也隐藏着中间无效操作，在电商交易、订单处理、客服干预等对中间操作可靠性要求高的场景存在严重评估盲区，缺乏系统性度量中间路径可靠性的标准化体系。
### 方法关键点
- 定义前缀可执行性规则：工具调用序列的每一个前缀都必须同时满足工具schema约束、状态前置条件、跨步骤数据依赖三大要求
- 提出5个互补的评估指标：用生存曲线形式的PEC度量各调用深度的可执行率，FED定位首个无效调用的步数，TER统计全路径完全可执行的占比，归一化AUC-PEC综合度量路径可靠性，RR量化出现无效调用后最终仍成功的恢复能力
- 配套Dual-Loop验证架构：规划器生成执行计划后先由校验器做前置可执行性检查，通过后再交给ReAct执行器调用工具，用于验证评估体系的有效性
### 关键实验结果
在BFCL-v3多轮工具调用、ToolSandbox、τ3-bench航空/零售三个数据集上测试，覆盖4类Agent架构、3个主流LLM基座：
1. 未做前置校验的计划条件ReAct最终成功率最高可达0.94，但TER仅为0.47，超90%的成功路径存在中间无效调用
2. Dual-Loop架构在维持最终成功率与前者基本持平的前提下，TER提升至0.94，AUC-PEC提升至0.96，第一错误深度平均延后2步以上

**最值得记住的结论**：工具调用Agent的可靠性不能仅看最终是否成功，还要看中间每一步是否合法可执行，避免「表面成功但中间埋坑」的伪可靠路径。
