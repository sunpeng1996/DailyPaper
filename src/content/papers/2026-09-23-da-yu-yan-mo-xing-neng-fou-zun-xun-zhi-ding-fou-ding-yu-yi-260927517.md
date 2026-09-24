---
title: 'Not What You Meant: Can LLMs Follow a Specified Negation Semantics?'
title_zh: 大语言模型能否遵循指定否定语义？基准测试与能力边界分析
authors:
- Qiming Bao
- Agnieszka Mensfelt
- Michael J. Witbrock
- Kostas Stathis
affiliations:
- University of Auckland
- Royal Holloway, University of London
arxiv_id: '2609.27517'
url: https://arxiv.org/abs/2609.27517
pdf_url: https://arxiv.org/pdf/2609.27517
published: '2026-09-23'
collected: '2026-09-24'
category: Reasoning
direction: LLM逻辑推理 · 否定语义评测
tags:
- Negation Semantics
- Logical Reasoning
- LLM Benchmark
- NAF-Bench
- Prompt Engineering
- LoRA
one_liner: 提出NAF-Bench基准，测评LLM遵循指定否定语义的能力并给出三类优化方案
practical_value: '- 做合规类Agent（电商规则审核、售后纠纷判定）时，可采用「LLM翻译规则+符号求解器执行」的架构，避免LLM默认语义和业务要求的否定语义冲突，大幅提升规则执行准确率

  - 涉及三值逻辑（是/否/无法判定）的推荐/审核场景，可在prompt中加入「先枚举所有原子值再下结论」的验证脚手架，减少LLM强制输出二元答案的错误

  - 业务有自定义语义要求时，可收集符号求解器生成的标注轨迹做LoRA微调，注意覆盖多场景话术避免过拟合到特定表述'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
不同高风险场景（法律、医疗、电商合规）对「否定」的语义定义差异极大（闭世界假设/三值逻辑/轻信推理/怀疑推理），现有LLM推理基准默认固定单一否定语义，无法测评LLM是否能遵循指定语义执行规则，导致高可靠需求场景下LLM推理结果不可控。

### 方法关键点
- 推出NAF-Bench自动生成带求解器认证真值的逻辑程序样本，覆盖SLDNF、良基语义(WFS)、稳定模型下的轻信/怀疑推理4种常见否定语义，每个样本在4种语义下可生成最多4种不同标签
- 样本生成时控制否定深度、规则宽度、循环结构等复杂度参数，同时支持逻辑等价的多话术、多规则顺序渲染，可分离语义理解能力和对表面表述的敏感性
- 设计三类实验范式：无指定语义（测默认语义偏好）、控制样本（所有语义结果一致，测基础指令遵循）、差异样本（不同语义结果不同，测指定语义遵循能力）

### 关键结果
- 顶尖闭源模型Claude Sonnet 5、GPT-5.6 Sol在固定复杂度测试集上4种语义准确率均达100%，o4-mini整体准确率94.8%，仅在WFS的undefined场景跌到81%
- 开源模型表现差距显著：最强的Qwen2.5-coder-32B准确率仅59~74%，Llama3-8B最低仅31~67%，且超过50%的逻辑等价规则重排会导致输出结果变化
- 三类优化方案均有效：翻译后求解架构将开源模型WFS准确率提升25~36个百分点，验证脚手架提升7~23个百分点，LoRA微调可使小模型WFS准确率达91%+

### 关键结论
LLM的默认否定语义无法匹配所有业务场景，在规则明确的高可靠需求场景下，「符号求解器兜底」比纯靠LLM端到端推理的成本更低、可靠性更高
