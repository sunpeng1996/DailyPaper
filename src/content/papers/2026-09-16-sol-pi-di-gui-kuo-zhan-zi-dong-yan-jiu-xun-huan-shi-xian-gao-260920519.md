---
title: 'SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness'
title_zh: 《SoL-Pi：递归扩展自动研究循环实现高效Agent管控框架》
authors:
- Haozhe Liu
- Tian Ye
- Sensen Gao
- Qihang Cao
- Yitong Li
- Mingchen Zhuge
- Duomin Wang
- Ruihua Zhang
- Ping Luo
- Jiawang Bian
affiliations:
- NVIDIA
- NTU
- MIT
arxiv_id: '2609.20519'
url: https://arxiv.org/abs/2609.20519
pdf_url: https://arxiv.org/pdf/2609.20519
published: '2026-09-16'
collected: '2026-09-18'
category: Agent
direction: Agent效能优化 · Token成本降低
tags:
- Agent
- Token Efficiency
- Cost Optimization
- Auto Research
- Agent Harness
one_liner: 通过自动迭代筛选4项优化机制，性能持平下降49%token消耗与1/3API成本
practical_value: '- 可直接复用4项token优化机制到业务Agent链路（如电商智能客服、推荐内容生成Agent、广告素材生成Agent等），在不损失效果的前提下大幅降低token成本

  - 自动迭代优化Agent管控层的思路可复用：在业务真实环境跑闭环优化循环，仅保留同时满足提效降本的优化点，避免主观设计的无效优化

  - 针对长轨迹Agent场景，优先做输入输出侧的token压缩优化，相比模型侧微调、量化等方案投入产出比更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent已从单步任务演进到长轨迹无人值守探索，全链路token消耗随任务复杂度指数级上升，token效率成为Agent规模化落地的核心瓶颈，现有方案普遍存在性能与成本不可兼得的问题。

### 方法关键点
- 采用递归自动研究循环架构，在覆盖多编程语言、多业务场景的异构环境中自动探索Agent管控层优化方案，仅保留「性能不下降、成本降低」的优化点
- 最终筛选出4项可迁移的核心优化机制：Action Fusion（合并多步动作减少交互次数）、Online Context Compact（在线压缩冗余上下文）、ObservationPack（打包观测结果去重）、Evidence-Preserving Reducer（保留关键证据前提下规约长文本）

### 关键实验结果
基于51任务EdgeBench基准测试，对比Pi、原生Codex、Claude Code等baseline，在GPT-5.6 Sol、Opus 5两个大模型上验证：SoL-Pi性能与Pi持平，token流量降低44.7%-49.0%，API成本降低约1/3；对比原生Codex和Claude Code每小时节省8.75-13.5美元，对比Pi每小时节省4.36-5.71美元，最高降本54.3%。

### 核心结论
Agent规模化落地的核心瓶颈已从模型性能转向长轨迹运行的token成本，管控层的轻量化优化ROI远高于模型侧优化。
