---
title: 'CertiSum: Bitwise-Identical MXFP4 Training Across Platforms and Parallelism
  Layouts'
title_zh: CertiSum：实现跨平台与并行布局的逐位一致MXFP4训练
authors:
- Steve Rhyner
- Yubo Gao
- Stefan de Lasa
- Sankeerth Durvasula
- Nandita Vijaykumar
affiliations:
- University of Toronto
- Vector Institute
- NVIDIA
arxiv_id: '2611.21584'
url: https://arxiv.org/abs/2611.21584
pdf_url: https://arxiv.org/pdf/2611.21584
published: '2026-11-16'
collected: '2026-11-17'
category: Training
direction: 低精度LLM训练·确定性优化
tags:
- MXFP4
- Low-Precision Training
- LLM Training
- Reproducibility
- Deterministic Training
one_liner: 通过运行时验证原生MXFP4 GEMM精确性+按需精确计算，实现跨平台/并行布局的逐位一致MXFP4训练
practical_value: '- 若业务采用低精度（FP4/FP8）训练LLM做推荐/Agent推理，可借鉴CertiSum的验证+精确回退框架，避免训练推理不一致、多卡训练结果漂移问题，尤其在RLHF类对齐任务中保证训练和采样引擎输出对齐

  - 跨云/跨GPU厂商训练LLM时，可复用其全局MX块分配+无舍入合并逻辑，保证不同硬件环境下训练结果完全一致，降低跨环境调试、审计成本

  - 大尺寸输入的MXFP4训练场景优先采用该方案，对比确定性BF16有最高1.7×加速，latency开销仅11.8~60.5%，适合生产级大模型预训练/微调降本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前MXFP4是LLM训练降本的核心低精度格式，但浮点加法非结合性、不同硬件/并行布局的求和顺序差异，会导致MXFP4训练非确定性，同输入在不同GPU厂商、不同并行度下输出差异是BF16的18倍，严重影响调试、训练审计、训练推理一致性，现有方案要么仅支持部分不变性，要么开销极高难以落地。

### 方法关键点
- 核心洞察：99.2%的MXFP4 GEMM输出在任意求和顺序下都可通过原生FP32累加得到精确结果，仅需对剩余0.8%的场景做精确计算
- 三层精确性校验：量化时同步收集行统计量、块统计量、绝对值乘积矩阵，逐层验证累加精确性，校验成本从低到高，校验通过直接复用原生GEMM结果
- 未通过校验的输出采用分块精确累加+无舍入合并，MX块按全局张量位置分配而非分卡分片位置，保证不同并行布局的求和项完全一致
- Attention、权重梯度GEMM这类校验通过率低的算子直接走精确核，避免不必要的校验开销

### 关键结果
在FineWeb-Edu、The Stack v3数据集上测试Qwen3-8B/14B、Llama3.1-8B模型，对比非确定性MXFP4、BF16、确定性BF16基线：
- 实现AMD MI350X和NVIDIA GB200跨厂商、DP/TP/CP多并行布局下200步训练状态完全逐位一致，推理时不同batch大小、并行度下生成token100%匹配
- 大输入尺寸下，比非确定性MXFP4仅增加11.8~60.5% latency，比BF16最高加速1.24×，比确定性BF16最高加速1.70×

### 最值得记住的结论
MXFP4训练的确定性不需要对所有算子做高成本精确计算，仅需对不到1%的异常场景做回退即可实现全链路逐位一致，兼顾性能和可复现性。
