---
title: Rethinking LLM Pruning via Test-Time Scaling
title_zh: 基于测试时采样缩放的大语言模型剪枝效果重评估
authors:
- Mingyang Song
- Mao Zheng
affiliations:
- Tencent
arxiv_id: '2611.01133'
url: https://arxiv.org/abs/2611.01133
pdf_url: https://arxiv.org/pdf/2611.01133
published: '2026-10-31'
collected: '2026-11-03'
category: LLM
direction: 大语言模型 · 结构化剪枝效果评估
tags:
- LLM Pruning
- Structured Pruning
- MoE
- Test-Time Scaling
- Reasoning Coverage
- Sampling Efficiency
one_liner: 揭示LLM剪枝后低单样本准确率仍可保留高推理覆盖度，提出需同时评估覆盖度与采样成本
practical_value: '- 业务侧若要压缩用于生成式推荐、多候选文案生成的LLM，优先选择MoE expert剪枝而非FFN/层剪枝，相同总参数量下可保留2倍以上的推理覆盖度，适配多采样择优的业务流程

  - 剪枝后的LLM用于Agent决策、复杂query理解场景时，无需仅以pass@1为选型标准，可将采样次数提升至10~20次，即可恢复90%以上原模型的推理覆盖度，整体成本低于部署未剪枝的大模型

  - 重度剪枝（剪枝率>70%）的模型不要用于高实时性场景（如实时query改写、在线推理），达到相同覆盖度的总token消耗可达原模型的50倍以上，反而会提升推理延迟与成本

  - 评估业务用剪枝LLM时，需新增「指定覆盖度下的总token消耗」「响应长度分布」两个指标，避免仅用静态准确率低估实际推理开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
过往结构化剪枝的评估仅依赖单样本准确率pass@1，无法区分「模型永久失去特定问题的推理能力」和「正确答案采样概率降低但仍可通过多次采样获得」两类情况，导致剪枝方法的业务价值被误判，也无法适配多采样择优的推理流程。
### 方法关键点
- 以相同采样预算下的pass@k作为推理覆盖度衡量指标，定义准确率保留率Em、覆盖度保留率Rm,K，同时统计达到目标覆盖度所需的采样次数、总token消耗，完整刻画剪枝效果
- 对比三类无恢复训练的结构化剪枝：MoE expert剪枝（RAZOR选择）、FFN通道剪枝（Taylor显著性）、层剪枝（困惑度贪心选择），控制总参数量对齐对比
- 测试覆盖3款MoE模型、4款稠密模型，在AIME-2026、Minerva数学数据集，HumanEval+、LiveCodeBench-v6代码数据集上验证
### 关键结果
- 50% expert剪枝的Qwen3.6-35B pass@1仅保留原模型的92.8%，但k=2048时覆盖度保留率达100.6%，甚至能解决原模型未覆盖的问题；相同总参数量下expert剪枝的覆盖度保留率是FFN剪枝的2倍以上
- 80% expert剪枝的Qwen3.6-35B要达到原模型90%的覆盖度，需要1319次采样，总token消耗为原模型的59.63倍，远超过单响应长度缩短带来的成本节省
- 原模型准确率相同的问题，原始响应长度越长，剪枝后准确率损失越高，最长响应组剪枝后pass@1比最短组低35pct以上

剪枝后的模型效果不能仅用单样本准确率评估，「可解决的问题范围」和「获得正确答案的采样成本」是两个独立的核心选型指标
