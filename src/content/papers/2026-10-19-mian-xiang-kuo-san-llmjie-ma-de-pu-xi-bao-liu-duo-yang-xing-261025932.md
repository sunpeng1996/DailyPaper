---
title: 'Keep the Lineages Alive: Diversity-Preserving SMC for Diffusion LLM Decoding'
title_zh: 面向扩散LLM解码的谱系保留多样性SMC推理方法
authors:
- Minoo Ahmadi
- Seyedarmin Azizi
- Mehdi Kamal
- Massoud Pedram
affiliations:
- University of Southern California
arxiv_id: '2610.25932'
url: https://arxiv.org/abs/2610.25932
pdf_url: https://arxiv.org/pdf/2610.25932
published: '2026-10-19'
collected: '2026-10-21'
category: LLM
direction: 扩散LLM · SMC解码多样性优化
tags:
- Diffusion LLM
- Sequential Monte Carlo
- Resampling
- Diversity
- Reasoning
one_liner: 提出无需额外训练的LP-SMC重采样策略，提升扩散LLM解码多样性与推理表现
practical_value: '- 生成式推荐（如商品文案、营销素材生成）场景下，可直接替换现有扩散LLM解码的多项式重采样逻辑为LP-SMC，无需微调模型即可提升候选集多样性，降低输出同质化问题，权重下限可直接复用κ=lnN的无调优配置

  - Agent多路径推理探索场景中，可借鉴权重下限trick，在重采样前将路径权重抬升为不低于最大权重的1/N，避免过早淘汰中间表现一般但最终有效的推理路径，无需增加额外的模型调用开销

  - 多候选召回/多样性排序场景下，除ESS外可新增「存活谱系数量」作为多样性监控指标，解决ESS无法识别候选集看似权重均衡、实则来源单一的问题，优化多样性评估体系'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
扩散LLM的推理侧Sequential Monte Carlo（SMC）解码可在无额外训练的前提下提升推理性能，但传统多项式重采样会淘汰中间权重低、但最终结果正确的推理谱系，且常用的有效样本量（ESS）指标仅衡量权重均衡度，无法感知谱系丢失，导致推理路径多样性不足，限制了最终准确率的上限。

### 方法关键点
- 提出谱系保留SMC（LP-SMC），仅修改重采样逻辑无需额外训练或模型调用：一是用Chopthin重采样替代多项式重采样，约束重采样后最大/最小权重比不超过η，保留不等权重不做强制均一化，减少谱系随机丢失；二是新增输入权重下限，重采样前将低于最大权重e^-κ倍的权重抬升到底线，避免低权重谱系被直接过滤
- 兼容内部自奖励、外部过程奖励模型两种权重生成方式，原有重采样触发规则（ESS<N/2）保持不变

### 关键实验
在LLaDA-1.5、Dream-7B两个扩散LLM上测试，覆盖MATH-500、GSM8K、HumanEval、MBPP四个推理/代码基准，对比基线SR-SMC：12种模型+奖励+基准组合下，oracle覆盖率（至少有一个正确候选的样本占比）全部提升，幅度1.8~25.6个百分点；11种组合的端到端准确率提升，LLaDA-1.5最高提7.9个点，Dream-7B最高提18.3个点；GSM8K任务16个初始谱系的存活数从5.2提升至10.0，候选多样性显著提升。

> 最值得记住的一句话：高ESS不代表谱系多样性，仅优化重采样策略无需修改模型就能显著提升扩散LLM的推理性能
