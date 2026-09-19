---
title: 'Sample Count Is Not Enough: Candidate-Generation Strategy Shapes the Energy
  and Performance of LLM Test-Time Scaling'
title_zh: 候选生成策略而非样本数决定LLM测试时缩放的能耗与性能
authors:
- Mobina Kashaniyan
- Ali Jannesari
affiliations:
- Iowa State University
arxiv_id: '2609.19499'
url: https://arxiv.org/abs/2609.19499
pdf_url: https://arxiv.org/pdf/2609.19499
published: '2026-09-15'
collected: '2026-09-19'
category: LLM
direction: LLM推理调度 · 测试时缩放优化
tags:
- LLM-inference
- test-time-scaling
- batch-scheduling
- energy-efficiency
- latency-optimization
one_liner: 固定候选生成数量下，验证更大批量更少调用的调度可大幅降低LLM推理能耗与延迟
practical_value: '- 涉及多候选生成的业务场景（如Best-of-N选品文案生成、Agent多路径推理、生成式推荐多候选打分），若候选独立且显存够用，直接合并为最大批量单次调用，可降低4倍以上能耗、5倍以上P95延迟

  - 做LLM服务成本核算时，不能仅用候选数量预估成本，需将生成调度的批大小、调用次数纳入计算模型，避免成本预估出现数倍偏差

  - 显存不足无法全量批量时，优先选择最大可行批大小、最小化调用次数，例如8个候选分2次4个批调度，能效是8次单候选调度的2倍以上

  - 短输出场景（如搜索Query改写、推荐标签生成）同样适用该规则，批量生成比串行能效高2.5~3.3倍，无特殊需求不要拆分调用'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM测试时缩放（如Self-Consistency、Best-of-N）普遍仅用候选数量N描述推理预算，但相同N下不同生成调度的系统成本差异极大，相关研究很少披露调度细节，导致结果不可复现、成本预估失真，亟需量化调度策略对性能、能耗的实际影响。

### 方法关键点
- 定义生成调度为`a×b`：a次串行调用，每次生成b个候选，总候选数N=a×b固定为8，对比1×8、2×4、4×2、8×1四种调度策略
- 测试模型为Phi-3-mini、Qwen2.5-1.5B，硬件覆盖A100 80G、V100 32G，测量指标包含P95延迟、GPU能耗、吞吐量、GPU小时
- 严格控制变量：相同prompt、解码参数、答案提取与投票规则，确保不同调度的逻辑生成token量差异小于1%

### 关键实验
- 数据集采用GSM8K（长输出推理）、SciQ（短输出选择），基准为1×8全批量调度
- A100上8×1串行调度相比1×8，能耗高4.64~4.86倍，P95延迟高5.77~6.12倍，吞吐量降至17%左右，该结果在3个独立A100节点稳定复现
- V100上短输出SciQ任务中，8×1相比1×8能耗高2.57~3.34倍，延迟高2.88~4.42倍，吞吐量降至23%~36%
- N从1升至8时，GSM8K精度提升8.4（Phi-3）~18.4（Qwen）个百分点，单token能耗随批量增大降低60%以上

### 核心结论
当候选独立且显存允许时，优先用最少调用次数、最大批大小的生成调度，可在不损失精度的前提下大幅降低推理成本。
