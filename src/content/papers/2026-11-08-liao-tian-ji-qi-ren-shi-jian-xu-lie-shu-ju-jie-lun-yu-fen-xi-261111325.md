---
title: 'Linking Event-sequence Data Claims to Analytic Provenance in Chatbots: Technique
  and Evaluation'
title_zh: 聊天机器人事件序列数据结论与分析溯源的关联技术及评估
authors:
- Po-Ming Law
- Jianheng Ouyang
- Nguyen-Truong Thinh
- Weizhi Li
- Arpit Narechania
affiliations:
- Adaptive Machines, Inc
- The Hong Kong University of Science and Technology
arxiv_id: '2611.11325'
url: https://arxiv.org/abs/2611.11325
pdf_url: https://arxiv.org/pdf/2611.11325
published: '2026-11-08'
collected: '2026-11-10'
category: Agent
direction: Agent 事件序列数据分析溯源增强
tags:
- Chatbot
- Analytic Provenance
- Clickstream Analysis
- Event Sequence
- Agent Tool Calling
one_liner: 提出聊天机器人事件序列分析结论与溯源绑定的技术并验证用户感知效果
practical_value: '- 电商用户行为（点击流）分析Agent可直接复用「可寻址引用表+结论绑定」机制，降低用户对分析结论的信任成本

  - 大模型生成数据分析结论时增加溯源引用标注，可同时提升正确结论的感知准确度、降低错误结论的误导性

  - 点击流分析标准化操作集+透视表抽象思路，可直接复用到用户行为自动化分析工具的开发中'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前点击流等事件序列分析类聊天机器人无法解释结论背后的分析流程，解读结论往往需要专业编程能力，用户对结论的信任度缺乏支撑。
### 方法关键点
1. 核心技术包含两个组件：可寻址单元格构成的参考表（记录全量分析步骤与结果）、将结论绑定到对应单元格的引用格式；
2. 针对点击流场景梳理标准化分析操作集，通过透视表抽象组织，开发AI Agent可调用工具，自动生成参考表并组装带引用标注的自然语言回答。
### 关键结果
两次各90人众包实验显示：带引用的正确结论较无解释场景感知准确度更高；带引用的错误结论较代码/无解释场景感知准确度更低，误导性明显下降。
