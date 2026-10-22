---
title: 'Beyond 4 bits: Data-Centric Post-training Quantization and Recovery'
title_zh: 低于4比特场景下以数据为中心的训练后量化与恢复方案
authors:
- Rhea Sanjay Sukthanker
- Riccardo Grazzi
- James Hensman
- Pashmina Cameron
affiliations:
- Microsoft
- Microsoft Research
arxiv_id: '2610.28537'
url: https://arxiv.org/abs/2610.28537
pdf_url: https://arxiv.org/pdf/2610.28537
published: '2026-10-20'
collected: '2026-10-22'
category: LLM
direction: 大语言模型低比特量化部署优化
tags:
- PTQ
- quantization
- LLM
- MoE
- model_compression
one_liner: 提出2比特LLM量化实操配方，保留89%-97%全精度性能，比QAT少1.4-30倍计算
practical_value: '- 端侧/低吞吐场景部署LLM4Rec、Agent时，2比特量化优先选择vector codebook方案，不要用标量PTQ，可避免精度掉落到随机水平

  - 量化的校准、恢复数据要联合选择：用通用web数据校准就选电商/广告垂直领域数据做恢复，用垂直数据校准就选通用web数据恢复，最大化生成任务精度

  - 量化后的LLM/Agent推理时可适当调高重复惩罚系数，缓解低比特量化导致的思维循环、重复输出问题

  - 轻量恢复阶段仅训练codebook即可，3200条样本就能饱和收益，成本远低于全量QAT，适合业务快速迭代'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
4比特Post-training quantization (PTQ)精度损失可忽略，是当前LLM部署的主流方案，但降至2比特时标量PTQ精度直接掉落到随机水平，无法落地低资源端侧、高吞吐推理场景。现有低比特量化方案要么依赖计算成本极高的Quantization-Aware Training (QAT)，要么忽略校准与恢复数据的耦合关系，对电商/推荐场景常用的MoE模型也缺乏适配优化。
### 方法关键点
- 量化表示优先选择vector codebook（如YAQA），替代传统标量量化，利用权重维度相关性降低压缩损失
- 校准数据采用任务对齐的混合语料：侧重生成类任务优先用垂直领域数据，侧重通用问答能力混合70%以上web通用数据
- 校准与恢复数据联合选择，仅做codebook维度的轻量恢复，冻结模型主干权重，大幅降低调优开销
### 关键结果
实验覆盖3.8B-32B共6个稠密/MoE模型，对比标量PTQ（SpinQuant、QuaRot）、QAT基线（BitDistiller、GSQ）：
1. 2比特vector PTQ仅用2.3有效比特/权重，即可保留89%~97%的全精度QA精度，而标量PTQ完全失效
2. 仅需3200条样本的codebook恢复即可饱和生成任务收益，整体计算量比最强QAT基线低1.4~30倍
3. 2比特量化模型推理时调高重复惩罚系数，可缓解低比特导致的思维循环、重复输出问题，推理精度恢复到全精度的80%以上
> 最值得记住的一句话：低于4比特的LLM量化，数据选择的影响远大于量化算法细节，校准和恢复数据必须联合调优，不要分开优化
