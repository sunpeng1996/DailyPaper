---
title: 'Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable
  Artifacts?'
title_zh: 瓶装Agent：LLM Agent能否将能力转化为低成本可扩展任务工件
authors:
- Ankit Sonthalia
- Haritz Puerto
- Alexander Rubinstein
- Martin Gubri
- Seong Joon Oh
affiliations:
- University of Tübingen
- Max Planck Institute for Intelligent Systems
- École Polytechnique
- KAIST AI
arxiv_id: '2610.08775'
url: https://arxiv.org/abs/2610.08775
pdf_url: https://arxiv.org/pdf/2610.08775
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: Agent 能力评测 · 低成本任务工件生成
tags:
- LLM Agent
- Benchmark
- Cost Optimization
- Distillation
- Task Artifact
one_liner: 提出BOTTLED基准评测LLM Agent将通用能力封装为低成本任务工件的能力
practical_value: '- 电商大规模重复任务（如query-商品相关性标注、商品属性抽取）可参考bottling思路，用Agent自主生成低成本工件（小模型、规则程序）替代反复调用大模型，实测Opus
  5在ESCI任务上保留82%零-shot性能的同时成本降低657倍

  - 选择Agent基座时不要仅看零-shot任务效果，相同零-shot性能的模型bottling能力差异可达3倍以上，需额外评测其资源分配、工具调用、工程决策能力

  - 研发资源有限时优先验证相同token预算的朴素蒸馏小模型 baseline，论文显示31/60的Agent bottling效果不如该基线，避免过度追求Agent方案反而带来效果下降

  - 业务Agent可接入BOTTLED的预算跟踪机制，增加token、时间配额的实时检测与回调能力，避免Agent耗尽资源却无有效产出（论文中8/60的运行无输出）'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent处理百万级规模重复任务（如电商商品属性抽取、query相关性判断）时逐实例调用大模型成本线性增长，现有蒸馏、规则生成等降本方案需要大量人工介入，亟需验证Agent能否自主将通用能力封装为低成本可复用的任务工件，平衡效果与摊薄成本。

### 方法关键点
- 提出BOTTLED基准，设置固定预算（5M token、10小时、单A100 40G），Agent拿到全量无标注任务数据后自主选择方案（训练小模型、写程序、混合方案等），最终输出全量任务预测结果
- 测试10款主流LLM基座，覆盖3类真实场景任务：MAVE商品属性抽取（4.77M样本）、ESCI query-商品相关性分类（2.62M样本）、RAID AI生成文本检测（5.62M样本）
- 设计两类基线：零-shot大模型基线、相同token预算的朴素蒸馏小模型基线（GLM 5.3 Flash打标+Qwen3-0.6B/SmolLM2-360M微调）

### 关键结果
- 零-shot性能与bottling能力无强相关性：相同零-shot F1的模型bottling效果差异可达3倍以上，48/60的bottling运行效果低于对应模型零-shot 95%置信区间下限
- 最优效果的Opus 5在ESCI任务上保留82%零-shot macro-F1，成本仅为零-shot方案的1/657；同时保留94%的专用低成本模型Jev的效果，成本仅为Jev的1/4

**最值得记住的一句话**：对于大规模重复任务，优秀的零-shot能力不代表优秀的低成本规模化落地能力，当前多数Agent的bottling效果不如相同预算的朴素蒸馏方案
