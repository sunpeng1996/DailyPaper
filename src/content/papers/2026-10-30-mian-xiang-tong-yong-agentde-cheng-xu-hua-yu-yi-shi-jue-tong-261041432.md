---
title: 'Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface
  for General Agents'
title_zh: 面向通用Agent的程序化-语义-视觉统一混合计算机交互接口
authors:
- Haoqing Wang
- Xiaoyi Zhang
- Sicheng Fan
- Zhexin Zhang
- Xinjie Zhang
- Jiahao Li
- Bin Li
- Yan Lu
affiliations:
- Microsoft Research
- Fudan University
- Tsinghua University
arxiv_id: '2610.41432'
url: https://arxiv.org/abs/2610.41432
pdf_url: https://arxiv.org/pdf/2610.41432
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: 通用Agent · 计算机交互接口优化
tags:
- Computer Use Agent
- Accessibility API
- Unified Interface
- OSWorld
- HCI
one_liner: 融合三类人机交互通道，为通用Agent提供兼具高性能与高交互效率的统一计算机操作接口
practical_value: '- 搭建电商运营自动化Agent/商家后台操作Agent时，可复用AX+GUI+代码的混合交互架构，相比纯GUI模拟点击能降低30%以上操作步数与调用成本

  - 跨工具/跨通道交互场景可引入文中的状态校验Guard机制，执行前校验目标元素/页面布局有效性，避免状态过期导致的误操作

  - 给工具调用型Agent加专用交互技能说明文档，可大幅降低调用错误率，文中从17.37%降至1.36%，该prompt工程技巧可直接复用

  - 多步交互任务可采用批处理操作+内置等待校验逻辑，将多轮工具调用合并为单轮，显著降低LLM调用次数与链路延迟'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有计算机操作Agent大多采用模拟人类的截图识别+键鼠操作范式，引入了强人类交互先验，不仅需要反复解析屏幕信息，还浪费了系统原生暴露的语义、程序化交互能力，导致操作效率低、任务成功率上限不足。

### 方法关键点
- 统一三类交互通道：程序化通道（代码/命令行工具）、语义通道（无障碍AX API读取控件树、执行引用寻址操作）、视觉通道（GUI截图+键鼠输入），通过Model Context Protocol暴露给Agent
- 设计跨通道动作Guard：执行AX操作前校验目标元素有效性，执行GUI操作前校验页面布局与上次截图一致性，避免状态过期导致的误操作
- 优化AX通道效率：输出压缩AX视图降低token消耗，支持单调用内批量操作+等待步骤，执行后返回AX差异作为反馈，减少交互轮次
- 附加交互技能说明：指导模型选择合适通道、组合操作，降低工具调用错误

### 关键实验
在OSWorld 2.0基准测试，对比CUA Driver等基线：用GPT-6 Astra时Partial得分达72.37%，超基线3.55个百分点；用Claude Opus 5时Binary得分达35.19%，超官方基线3.76个百分点，同时成本降低20%；在OSWorld 1.0上相比CUA Driver平均得分高6.48个百分点，步数减少17%，成本降低30%，跨WeaveBench、MacAgentBench、Windows Agent Arena多平台均实现性能效率双提升。

过度模仿人类交互范式的接口会限制大模型能力释放，基于系统原生能力设计的混合交互接口能同时提升Agent的任务表现与执行效率。
