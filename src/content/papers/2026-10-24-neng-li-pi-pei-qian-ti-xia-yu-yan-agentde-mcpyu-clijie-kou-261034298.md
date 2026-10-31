---
title: 'Matched Capabilities, Different Behaviors: A Controlled Study of MCP and CLI
  Interfaces for Language Agents'
title_zh: 能力匹配前提下语言Agent的MCP与CLI接口行为差异对照研究
authors:
- Zhenning Shi
- Liang Pang
- Yongqi Li
affiliations:
- The Hong Kong Polytechnic University
- Institute of Computing Technology, Chinese Academy of Sciences
arxiv_id: '2610.34298'
url: https://arxiv.org/abs/2610.34298
pdf_url: https://arxiv.org/pdf/2610.34298
published: '2026-10-24'
collected: '2026-10-31'
category: Agent
direction: Agent 工具调用接口优化
tags:
- Language Agent
- MCP
- CLI
- Tool Calling
- Interface Optimization
one_liner: 可控对比验证能力匹配下接口表征显著改变Agent行为，提出MICA分析框架与DART修复机制
practical_value: '- 业务Agent工具选型时，不要仅验证功能匹配度，需优先测试MCP/CLI在对应场景下的性能、token成本差异，避免接口选择拖垮整体效果

  - 可直接复用DART核心思路：将语义决策与接口实现解耦，语义动作验证通过后仅修复格式错误，不重新生成决策，可显著提升修复成功率、降低token消耗

  - 做Agent行为归因时，可借鉴MICA的配对轨迹分析方法，快速定位决策差异源于语义选择还是接口实现问题，提升排障效率

  - 电商导购、售后工单处理等场景的Agent若使用MCP/CLI调用工具，可直接复用论文的对照实验设置，快速选定适配业务的最优接口'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前语言Agent广泛通过MCP、CLI两类接口调用外部能力，过往接口对比常混杂工具粒度、执行脚手架等干扰变量，无法确定接口表征本身对Agent行为的真实影响，而接口选择直接决定Agent的任务表现、token成本，亟需可控实验明确二者的实际效应边界。
### 方法关键点
- 提出MICA分析框架：从统一语义动作契约生成MCP、CLI两种接口，共享下游验证、编译、执行链路，确保可执行能力完全匹配，仅模型侧的接口表征存在差异
- 设计双维度分析逻辑：匹配状态探针固定决策上下文，拆解接口展示、实现、反馈三个模块的独立及交互影响；配对自然轨迹追踪首次决策差异的下游传播路径
- 提出DART修复机制：将语义决策与接口实现解耦，验证通过的语义动作固定不变，仅修复接口特定的格式错误，避免不必要的语义重选带来的成本浪费
### 关键实验
覆盖ALFWorld、WebShop、ScienceWorld三个交互环境，测试Qwen3全系列、DeepSeek-v4-Flash、Gemini-2.5-Flash共6个模型；94.3%的2004组配对轨迹出现显著行为差异；DART在6个基准-接口配置下全部提升性能，最高提分9.0，MCP场景下单任务最多减少27.1k token消耗。
### 核心结论
对于交互式语言Agent，能力的表征方式本身就是决策环境的核心组成部分，直接决定最终的策略实现效果
