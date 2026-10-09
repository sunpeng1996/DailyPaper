---
title: 'LadderEdit: Edit-Level Residual Compression for Memory-Efficient Lifelong
  Editing of LLMs'
title_zh: LadderEdit：面向LLM终身编辑的编辑级残差压缩方法
authors:
- Xiaobing Yu
- Peijie Qiu
- Jin Yang
- Xuanzhao Dong
- Weiwei Ma
- Zhaoqi An
- Xiaoqi Zhao
- Xiaofeng Liu
affiliations:
- Yale University
- Washington University in St. Louis
- Icahn School of Medicine at Mount Sinai
- Arizona State University
arxiv_id: '2610.11160'
url: https://arxiv.org/abs/2610.11160
pdf_url: https://arxiv.org/pdf/2610.11160
published: '2026-10-08'
collected: '2026-10-09'
category: LLM
direction: LLM终身编辑 · LoRA存储优化
tags:
- LoRA
- Model Editing
- Lifelong Learning
- Low Rank Compression
- LLM
one_liner: 通过阶梯式低秩分配+行为审计，将LLM终身编辑的LoRA存储降5.2倍且性能追平全量LoRA
practical_value: '- 电商/推荐场景多LoRA适配（分品类/人群/场景）可直接复用该压缩逻辑：80%的适配任务用rank1 LoRA即可满足要求，仅给少数复杂场景分配更高秩，可降低80%以上的LoRA存储开销，不影响业务效果

  - Agent技能/知识库迭代场景，可借鉴「光谱预估+业务指标审计」的秩分配流程：新技能先用低秩LoRA落地，校验不通过再升秩，平衡存储成本和迭代效率，支持上万次技能更新

  - 实时推荐策略迭代场景，可参考该覆盖优先的设计思路：避免直接丢弃旧策略的LoRA，改为压缩到最低可行秩存储，既保留历史迭代的可回溯性，又控制存储线性增长的压力'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有LLM终身编辑方案大多为每个知识更新存储一个全量LoRA适配器，存储随编辑次数线性增长，无法支撑上万次的长期知识迭代；而固定内存的编辑方案会出现新旧编辑的参数冲突，导致编辑失效、无关知识被篡改等问题，无法同时满足可更新、不遗忘、低存储三个核心要求。
### 方法关键点
1. 精确优先：每个新编辑先训练全量LoRA更新，对其做SVD分解得到不同秩的低秩草图，保证基础编辑效果的上限
2. 光谱预估：基于LoRA的奇异值尾分布和全量LoRA的行为余量（改写、泛化、locality三个指标的阈值余量），预估满足要求的最低秩，仅做一次SVD无额外推理开销
3. 行为审计：对预估的低秩草图做三类约束校验（改写准确、泛化到相关prompt、不影响无关知识），校验不通过则按阶梯升秩直到满足要求，给locality指标最高权重避免不可逆的知识污染
4. 预算控制：内存不足时按每单位参数的效果收益密度，降级低优先级编辑的秩，保障核心编辑的效果
### 关键结果
在ZsRE、CounterFact、WikiBigEdit三个标准编辑基准上测试LLaMA-3-8B、Mistral-7B、Qwen2.5-7B三类模型，对比全量LoRA存储降低5.2倍，5万次连续编辑下仍保持0.86的平均得分，效果基本追平全量LoRA，远优于MEMIT、GRACE等基线方案；约80%的编辑用rank1 LoRA即可满足所有约束，仅不到5%的编辑需要全量秩。
### 核心结论
终身编辑存储的核心问题不是选择保留哪些编辑，而是为每个编辑分配刚好满足效果要求的最小表示分辨率
