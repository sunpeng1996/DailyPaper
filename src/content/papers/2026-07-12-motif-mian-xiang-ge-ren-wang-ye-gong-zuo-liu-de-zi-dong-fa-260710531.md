---
title: 'Motif: Discovering and Automating Personal Web Workflows'
title_zh: Motif：面向个人网页工作流的自动发现与自动化系统
authors:
- Shaokang Jiang
- Daye Nam
affiliations:
- University of California, Irvine
arxiv_id: '2607.10531'
url: https://arxiv.org/abs/2607.10531
pdf_url: https://arxiv.org/pdf/2607.10531
published: '2026-07-12'
collected: '2026-07-14'
category: Agent
direction: Agent 个人工作流自动化发现与生成
tags:
- Web Automation
- Workflow Mining
- LLM Agent
- End-User Programming
- Ambient Intelligence
one_liner: 被动采集用户浏览器行为挖掘可自动化重复模式，生成可部署本地化脚本，解决用户不知道什么值得自动化的痛点
practical_value: '- 电商运营端自动化工具可复用「被动行为采集+语义模式挖掘」的思路，无需运营主动提需求，自动识别批量改价、客户固定回复等重复操作生成自动化脚本，降低工具使用门槛

  - 模式挖掘阶段放弃传统纯频率序列挖掘，改用LLM做语义匹配过滤噪声、识别有业务价值的可自动化模式，可迁移到用户行为路径分析、高频重复任务挖掘场景

  - 自动化输出优先选择可本地运行的确定性程序而非每次调用LLM Agent，能大幅降低推理成本、提升执行速度、减少隐私风险，适合C端用户侧自动化产品设计

  - 推荐系统的用户意图挖掘可参考「行为+语义结合」的思路，被动识别重复行为背后的稳定需求，提前做服务/内容推荐，覆盖用户自身未意识到的需求缺口'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前基于LLM的vibe coding、示教编程等低代码自动化工具，默认用户知道什么任务值得自动化，但实际上用户会对高频重复任务产生习惯化认知，也缺乏编程能力判断哪些任务可自动化，存在「启动缺口」不知道该自动化什么；同时LLM Agent每次执行的推理成本高、隐私风险大，需要更轻量化的自动化方案。

### 方法关键点
- 数据层：Chrome插件被动采集浏览器UI交互、页面URL、截图、轻量网络请求四类行为数据，本地存储，支持暂停采集和URL黑名单保障隐私
- 处理pipeline：将60s内连续低层级交互用多模态LLM抽象为带元数据的高层级自然语言动作；用LLM做模式挖掘，合并相似的可自动化重复序列，比传统纯频率序列挖掘噪声过滤效果更好；LLM生成包含触发条件、功能描述、通知逻辑的非技术化程序设计方案，按出现频率+未来使用概率排序后推给用户
- 工程层：用户确认/修改设计后，LLM生成可直接运行的Tampermonkey脚本，全程用户可控，脚本权限最小化，所有数据本地留存

### 关键实验
8名用户连续使用平均5.5天，对比vibe coding基线：Motif平均每人发现22个可自动化模式，用户自主仅能识别1.3个；40个被用户审核的模式中85%符合用户日常流程，60%成功生成可运行脚本；用户满意度在易用性、准确性、可理解性等所有维度都显著高于vibe coding，75%用户愿意持续使用。

### 核心洞见
自动化的最大瓶颈不是怎么实现自动化，而是先发现什么值得自动化。
