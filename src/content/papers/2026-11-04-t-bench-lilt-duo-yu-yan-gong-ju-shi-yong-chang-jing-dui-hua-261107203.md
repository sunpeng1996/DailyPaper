---
title: 'τ-bench-LILT: Evaluating Conversational Agents on Realistic Multilingual Tool-Use
  Tasks'
title_zh: τ-bench-LILT：多语言工具使用场景对话Agent评测基准
authors:
- Kaden Uhlig
- Kiarash Mokhtari
- Anıl Arslan
- Yunsu Kim
- Joern Wuebker
affiliations:
- LILT
- Technische Universität Berlin
arxiv_id: '2611.07203'
url: https://arxiv.org/abs/2611.07203
pdf_url: https://arxiv.org/pdf/2611.07203
published: '2026-11-04'
collected: '2026-11-06'
category: Eval
direction: 对话Agent · 多语言工具使用评测
tags:
- Conversational Agent
- Multilingual Evaluation
- Tool Use
- Benchmark
- Customer Support
one_liner: 推出覆盖4种语言4个垂直领域的多语言对话Agent工具使用评测基准
practical_value: '- 做多语言客服Agent时，不要默认模型能自动适配不同语言的命名规则（如韩语姓在前、波斯语的后缀），需针对性增加字段映射规则，避免用户信息查询失败

  - 多语言Agent部署时不要直接全量翻译任务，仅本地化用户侧的数据库（姓名、地址、产品、币种等）和交互逻辑，保留内部政策、工具定义为英文，适配多数跨国企业的真实架构

  - 评测多语言Agent时，不能直接复用英语用户模拟器，要针对每个语言单独迭代用户模拟器prompt，避免出现提前终止、信息主动泄露等影响评测公平性的问题

  - 现有前沿LLM的多语言工具使用能力差异显著，韩语、波斯语零售场景的pass^4相比英语最多下降61点，出海业务需针对性做LoRA微调或prompt优化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有工具型对话Agent的评测几乎全部基于英语场景，跨国企业出海部署多语言客服（电商、航空、银行等垂直领域）时，缺少可真实反映本地化性能的评测基准；仅简单翻译的评测会生成不符合当地文化的场景，无法精准测出模型真实的多语言适配缺陷。
### 方法关键点
- 基于τ3-bench扩展德语、韩语、土耳其语、波斯语4种语言，覆盖航空、零售、电信、银行4个核心业务场景
- 仅本地化用户侧资产：数据库填充符合当地文化的姓名、地址、产品、航班等记录，用户模拟器prompt经母语专家多轮对比标注迭代优化，任务适配本地化真实需求
- 刻意保留Agent侧的政策文档、工具定义为英文，贴合跨国企业真实部署架构，避免理想化假设
- 修复原始τ3-bench的10个潜在bug，优化用户模拟器解决了提前终止、不符合文化交互等问题，最终采用Gemini 3.5 Flash作为全语言用户模拟器
### 关键结果
在8个前沿Agent模型上测试，德语表现与英语接近，韩语、波斯语零售场景的pass^4相比英语最多下降61点；Claude Opus 5在韩语零售场景中82.8%的姓名查询会错误转写为罗马字母，39.7%会颠倒姓名顺序，导致性能大幅下降；优化后的用户模拟器将非英语场景的提前终止率从7.62%降至0。
### 核心结论
前沿LLM无法直接从英语环境泛化到其他语言的工具使用场景，必须针对每个语言做单独的测试、prompt优化和工具适配。
