---
title: 'Tree-Ising: Repairing Language Models with Bit-Level Ising Edits'
title_zh: Tree-Ising：基于比特级伊辛编辑的大语言模型修复方法
authors:
- Hadi Salloum
- Ammar Ali
affiliations:
- QDeep, Riyadh, Saudi Arabia
- LEAD Lab, ITMO University
arxiv_id: '2611.14210'
url: https://arxiv.org/abs/2611.14210
pdf_url: https://arxiv.org/pdf/2611.14210
published: '2026-11-09'
collected: '2026-11-11'
category: LLM
direction: 大模型权重编辑 · 无梯度稀疏修复
tags:
- Model Editing
- Ising Model
- Sparse Optimization
- Weight Programming
- BF16
one_liner: 用离散伊辛优化替代LLM Agent做模型权重修复，成本降350倍精度更高
practical_value: '- 推荐/Agent场景的小模型推理异常（循环、重复输出等）可复用该无梯度修复思路，无需重新SFT，单修复成本不到1美元

  - BF16权重的稀疏比特编辑技巧可直接用于部署后模型hotfix，仅修改少量比特位，无需全量更新权重，大幅降低分发成本

  - 基于前向统计的异常层定位方法，可快速定位大模型推荐/Agent行为异常对应的层，无需反向梯度，计算效率极高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
此前MIT提出的用前沿LLM Agent做权重空间编程修复模型推理循环的方案成本极高（单次修复312美元，耗时15.6小时），依赖Agent的自然语言决策，无法保证编辑最优性，且修改权重大、对存储格式不友好，亟需低成本、高稀疏性的无梯度模型修复方案。
### 方法关键点
- 将模型修复转化为BF16权重上的稀疏离散优化问题，仅允许符号翻转、指数偏移两类操作，不修改共享指数和尾数，天生适配BF16存储格式
- 通过前向统计计算循环方向、推理结束方向，自动定位需编辑的层，无需Agent介入或反向梯度计算
- 优化目标可精确拆解为每个输出行独立的QUBO（Ising）问题，用GPU模拟退火或量子启发的模拟分岔法求解，也可直接映射到量子硬件执行
### 关键结果
在Qwen3.5-0.8B推理循环修复任务上，对比MIT GPT-6 Agent方案，MATH-500精度从51.7%提升至54.6%，修改权重减少13%，BF16比特翻转降低2.2倍，仅需4次前向请求，成本从312美元降至0.9美元，耗时从15.6小时压缩到31分钟；迁移到Qwen3.5-2B无需参考编辑，GSM8K贪心精度从21.6%提升至69.4%。
最值得记住的结论：针对特定故障的小模型无梯度离散修复，成本和效果远优于用大模型Agent做权重编程
