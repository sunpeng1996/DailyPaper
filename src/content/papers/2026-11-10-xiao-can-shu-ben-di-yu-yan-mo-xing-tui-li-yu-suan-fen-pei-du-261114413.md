---
title: Bits or permutations? Spending a fixed inference budget on weight precision
  or on option-order averaging in small local language models
title_zh: 小参数本地语言模型推理预算分配：权重量化精度 vs 选项重排平均
authors:
- Mohammed Nayeem Khan
- Logesh L
- Aliyas Ahmad Misri
affiliations:
- Intel Corporation
arxiv_id: '2611.14413'
url: https://arxiv.org/abs/2611.14413
pdf_url: https://arxiv.org/pdf/2611.14413
published: '2026-11-10'
collected: '2026-11-11'
category: LLM
direction: 小参数LLM推理量化与成本优化
tags:
- weight_quantization
- permutation_averaging
- local_LLM
- inference_optimization
- cost_efficiency
one_liner: 给出小参数本地LLM固定推理预算下量化精度与选项重排平均的最优分配策略
practical_value: '- 小参数本地LLM部署优先选6-bit RTN量化：无精度损失，权重读取成本仅为fp16的39%，适合边缘端Agent、端侧推荐场景的轻量化部署

  - 固定推理预算下的资源分配规则：预算≥0.39倍fp16单轮推理成本时，优先用6-bit量化，剩余预算分配给最多4次选项重排平均，可额外提升2.4~4.7个点准确率

  - 低比特量化（≤4bit）导致的选项位置偏差问题，可通过4次循环重排平均大幅缓解，同时ECE可从0.33降至0.09，大幅提升模型输出校准度

  - 低比特场景下，模型单轮输出置信度可信度低，可通过多次重排的结果一致性作为无监督置信度指标，AUROC比单轮置信度高5~9个点'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
小参数本地LLM部署时，低比特量化可降低内存占用，选项重排平均可消除输出位置偏差，但二者的交互影响尚未被探明，固定推理预算下如何分配资源到量化精度还是重排次数没有明确指导。

### 方法关键点
- 测试对象为Qwen3-0.6B、Qwen3-1.7B两个小参数模型，采用每组64个权重的RTN量化，精度覆盖fp16、8bit、6bit、4bit、3bit
- 统一成本度量：以fp16单轮推理的权重读取字节数为单位，b-bit量化+K次重排的总成本为K*(b+0.25)/16
- 评估基准为ARC-Easy、ARC-Challenge、MMLU、HellaSwag四个多选任务，各取300样本，覆盖准确率、翻转率、位置偏差、校准度指标

### 关键结果
- 6-bit RTN量化无精度损失，较fp16准确率高0.9~1.8个点，权重读取成本仅为fp16的39%；8-bit量化精度损失<0.7个点
- 4-bit量化下0.6B模型位置偏差从0.15升至0.53，4次循环重排平均可提升准确率12.6个点，ECE从0.33降至0.09
- 成本匹配对比显示，仅当权重≥6bit时，增加重排次数优于提升量化精度；≤4bit时提升精度收益更高

小参数本地LLM最优部署策略为优先选择6-bit量化，剩余推理预算分配给最多4次选项重排平均，可实现成本与效果的最优平衡。
