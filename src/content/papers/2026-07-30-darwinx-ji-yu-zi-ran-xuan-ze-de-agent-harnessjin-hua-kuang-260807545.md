---
title: 'DarwinX: Evolving Agent Harnesses Through Natural Selection'
title_zh: DarwinX：基于自然选择的Agent Harness进化框架
authors:
- Yifan Zhang
- Yutong Dai
- Juntao Tan
- Luyu Yang
- Rishi Mullur
- Thai Hoang
- Zhiyuan Hu
- James Zhu
- Phil Mui
- Silvio Savarese
affiliations:
- Salesforce AI Research
- Salesforce Agentforce
arxiv_id: '2608.07545'
url: https://arxiv.org/abs/2608.07545
pdf_url: https://arxiv.org/pdf/2608.07545
published: '2026-07-30'
collected: '2026-08-14'
category: Agent
direction: Agent自我进化 · Harness种群优化
tags:
- Agent
- Self-Evolution
- Harness Optimization
- Natural Selection
- Frozen LLM
one_liner: 冻结LLM底座，通过种群自然选择优化Agent Harness组件，实现跨任务泛化提升
practical_value: '- 优化业务Agent时可优先固定LLM底座，通过迭代Harness（prompt、工具链、控制流）降本提效，无需微调大模型即可快速落地

  - 可复用「保留-扩展」准入规则：Harness迭代仅接受在至少1个任务上提升、且原有已解决任务退化不超过阈值的变更，避免越改越差

  - 多场景Agent迭代可保留多分支Harness存档，跨分支合并互补能力，比单路线迭代泛化性更好，适合电商搜索/推荐/客服多场景复用

  - 无需标注数据即可驱动迭代：可复用失败轨迹归因、专家示范蒸馏、自身成败对比三类信号，统一转化为Harness编辑'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有单谱系Agent自进化方案存在路径依赖、跨任务干扰问题，优化时经常出现解决了新任务但原有任务性能退化的情况，且迭代收益多适配特定benchmark难以泛化，同时微调大模型成本极高，亟需低成本、高泛化的Agent能力升级方案。

### 方法关键点
- 底座完全冻结，仅优化Harness层（prompt、工具、技能、控制流），迭代收益完全来自Harness优化
- 采用「保留-扩展」准入契约：子变体只有在至少1个任务上性能提升、且原有任务退化不超过预设阈值才可进入种群存档
- 保留多分支Harness存档，支持跨分支互补能力合并，避免单谱系路径依赖
- 统一三类进化信号接口：失败轨迹诊断、专家示范蒸馏、自身成败对比，所有信号都转化为Harness编辑，不碰模型权重

### 关键结果
4类benchmark平均提升约17个点：Terminal-Bench 2.1从75.5%提升到83.2%（GPT-5.5底座），最高达84.7%登顶公开榜单；WebArena-Infinity真实任务pass@1从43.5%提升到93.0%，非法轨迹从293条降至17条，能力与合规性同步提升；TerminalWorld持外任务pass@1达68.3%，超过所有现成Agent；Terminal-Bench 2.1训练的Harness零样本迁移到SWE-bench Verified达84.2%，超过基准3.4个点。

> 最值得记住的结论：冻结的LLM底座不等同于固定能力的Agent，通过Harness的种群选择可将评估算力转化为可迁移的持久能力
