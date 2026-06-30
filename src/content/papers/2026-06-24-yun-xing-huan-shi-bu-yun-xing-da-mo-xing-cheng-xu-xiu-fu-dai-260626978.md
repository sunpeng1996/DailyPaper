---
title: 'To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in
  LLM-Based Program Repair'
title_zh: 《运行还是不运行：大模型程序修复中代码执行的成本效益分析》
authors:
- Zhihao Lin
- Junhua Zhu
- Mingyi Zhou
- Xin Wang
- Zhensu Sun
- Renyu Yang
- David Lo
- Li Li
affiliations:
- Beihang University
- Wuhan University
- Singapore Management University
arxiv_id: '2606.26978'
url: https://arxiv.org/abs/2606.26978
pdf_url: https://arxiv.org/pdf/2606.26978
published: '2026-06-24'
collected: '2026-06-30'
category: Agent
direction: Agent 工具调用成本收益优化
tags:
- LLM Agent
- Tool Calling
- Cost Effectiveness
- Program Repair
- Empirical Study
one_liner: 通过两阶段大规模实证分析揭示大模型程序修复中无差别代码执行性价比极低，需做显式成本收益权衡
practical_value: '- Agent 工具调用不要默认开启，所有高成本工具调用（如API调用、复杂检索计算）都应先做成本收益预判，避免无意义开销

  - 工具调用收益集中在任务后期，前期可优先依赖大模型原生能力输出，比如电商客服Agent前期直接生成回复，卡壳时再调用订单/商品查询工具

  - 商用SOTA大模型的工具调用增益极低，优先用强模型原生能力降本，比如用Claude/GPT-4做电商文案生成时，无需每次都调用合规校验工具，可省50%+的token和耗时'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM程序修复Agent普遍默认采用generate-run-revise范式，无差别调用代码执行工具校验补丁，但执行耗时高、成本高，其实际收益此前缺乏系统性量化分析。
### 方法关键点
开展两阶段实证研究：第一阶段分析SWE-bench排行榜提交的7745条Agent执行轨迹，规模化刻画执行行为特征；第二阶段基于200个SWE-bench实例、3类Agent（Claude Code、Codex、OpenCode）开展3000次端到端修复实验，对比4种执行范式下的性能与成本差异。
### 关键结果数字
1. 各Agent平均每个任务执行8.8次测试，执行频率2~19次不等，后期执行成功率比早期高8.1pct；
2. 禁用执行对商用SOTA模型修复成功率的影响仅1.25pct（无统计显著性），同时可节省56~62%token、48~54%耗时，开源模型Qwen2.5-Coder-32B上禁用执行的成功率差距几乎为0；
3. 执行收益高度集中，大部分场景下执行无增益，当前无差别调用的成本浪费严重。
