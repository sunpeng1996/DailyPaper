---
title: 'Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate
  consumer'
title_zh: 代理型AI作为替代消费者时的启发式决策机制研究
authors:
- Davood Wadi
- Yu Ma
affiliations:
- McGill University
arxiv_id: '2609.28372'
url: https://arxiv.org/abs/2609.28372
pdf_url: https://arxiv.org/pdf/2609.28372
published: '2026-09-23'
collected: '2026-09-24'
category: Agent
direction: AI购物Agent · 决策行为机制
tags:
- LLM Agent
- Shopping Agent
- Bounded Rationality
- Heuristic Decision
- Tool Calling
one_liner: 验证AI购物代理的启发式决策由信息架构与指令清晰度共同决定，而非固有缺陷
practical_value: '- 开发消费者端AI购物Agent时，必须内置目标澄清模块，用户给出模糊指令（如「找最划算的商品」）时，主动确认优化目标（如是否要求单位价格最低），避免信息截断导致选品错误

  - 电商平台面向AI购物Agent优化商品信息架构时，将决策必需的diagnostic属性（单位价格、重量、折扣后实付价）放在无需额外tool调用的默认返回字段，降低Agent获取成本，提升商品被选中概率

  - 设计AI Agent的工具调用策略时，可针对不同购物任务预设高优先级核心属性集，即便存在调用成本约束也优先拉取这类属性，避免启发式信息截断导致决策劣化

  - 电商定价策略层面，针对AI代理购物场景，传统尾数定价、折扣话术等针对人类的启发式套路效果有限，明确标注单位价格、实际结算价等核心属性更易获得AI代理偏好'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前消费者越来越多地将全链路购物决策委托给LLM驱动的AI代理，过往研究普遍认为LLM的类人启发式决策是训练数据带来的固有缺陷，但实际决策路径和影响因素未被明确，针对人类设计的零售定价策略（如尾数定价、折扣 framing）是否会误导AI代理，以及背后的驱动机制尚不清晰，直接影响AI购物代理的设计与电商平台的信息架构优化。
### 方法关键点
- 提出Tool-Lab实验范式，将商品属性隐藏在需要付费调用的tool接口后，可追踪AI代理决策前的信息获取全链路，区分「信息获取失败」和「信息利用失败」两类决策错误
- 核心变量采用2×2交叉设计：信息获取成本（零成本/高成本）、用户指令明确度（模糊指令：找最划算的/明确指令：找每盎司价格最低的）
- 实验覆盖3家主流厂商的8款商用LLM，总会话量16400次，包含全信息基线实验、Tool-Lab约束实验、多组鲁棒性验证实验
### 关键结果数字
- 全信息+明确指令场景下，AI代理决策最优率达94%，针对人类的定价线索几乎不会产生误导
- 高信息获取成本+模糊指令场景下，AI代理的诊断属性获取量下降35%-46%，最优决策率从89%骤降至29%（尾数定价场景）、48%（折扣 framing 场景），呈现与人类一致的启发式决策特征
- 验证显示99%以上的决策劣化来自诊断属性获取截断，而非LLM本身的算术或推理能力缺陷
### 核心结论
AI购物代理的启发式决策并非模型固有缺陷，而是由商家的信息架构设计和用户指令的明确度共同决定的
