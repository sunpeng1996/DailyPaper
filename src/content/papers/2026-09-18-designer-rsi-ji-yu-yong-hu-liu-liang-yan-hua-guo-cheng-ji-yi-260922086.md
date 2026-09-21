---
title: 'Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic
  Design'
title_zh: Designer-RSI：基于用户流量演化过程记忆的智能体平面设计框架
authors:
- Hongyang Du
- Lan Yan
- Christian Flores
- Asim Kadav
affiliations:
- Adobe
- Brown University
arxiv_id: '2609.22086'
url: https://arxiv.org/abs/2609.22086
pdf_url: https://arxiv.org/pdf/2609.22086
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: Agent 过程记忆演化与无监督迭代优化
tags:
- Procedural Memory
- Skill Evolution
- No Fine-tuning
- Tool Calling
- Replay Gate
one_liner: 冻结大模型权重，通过演化自然语言技能库无监督提升多步设计Agent执行成功率与生成质量
practical_value: '- 可复用「技能库拓展+迭代+保守准入」的无权重更新Agent迭代框架，避免LLM微调成本与合规风险，尤其适合电商广告素材生成、运营Agent等高频交互场景

  - 可直接照搬matched replay gate设计：固定上游上下文做成对对比，避免评估器漂移与上下文扰动导致的错误技能上线，大幅降低线上迭代的regression风险

  - 针对长序列多步工具调用任务，可参考「高频未覆盖子任务聚类出新技能、失败技能用成功/失败样例对比迭代」的双轴优化逻辑，快速提升工具调用成功率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
专业平面设计是长周期多步智能体任务，依赖超230种工具的组合调用，既无明确的成功判定oracle，长序列信用分配难度极高，且商用大模型往往因权限、成本问题无法微调，需要在模型权重冻结的前提下，从真实用户流量中积累可复用经验持续提升性能。

### 方法关键点
- 双轴演化技能库：① 拓宽：聚类用户流量中高频未覆盖子任务，蒸馏生成新的自然语言技能；② 加深：对比同一技能的成功/失败执行轨迹，迭代优化已有技能描述
- 保守准入replay gate：所有候选技能变更（新增/修改）都在固定上游上下文的前提下与基线成对对比，只有无性能回退且至少在1个场景下有提升才允许上线，避免噪声反馈导致的效果下降
- 全程无模型权重更新、无人工标注，仅修改外部可插拔的技能库

### 关键结果
基于1406份真实用户设计brief、1869条自动评分轨迹迭代5轮，技能库从76个冷启动文档技能扩充到139个。对比无技能基线，Claude-Sonnet-4的GenEval2执行成功率从72.7%提升到99.3%，生成质量提升11.99分；在4个专业设计基准上对Claude-Sonnet-4、Claude-Opus-4.6的胜率分别达61.8%、67.6%；单独拓宽/加深的胜率仅49.4%/48.6%，结合后达58.5%，端到端latency仅增加3.4%~6.2%。

**最值得记住的一句话**：针对无明确成功oracle、无法微调大模型的商用Agent场景，基于用户流量演化外部过程记忆是性价比极高的迭代路径
