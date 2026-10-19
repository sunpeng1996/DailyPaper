---
title: 'Dream2Discern: Learning from Hard Latent Variants for Runtime Failure Prediction
  in Multi-Agent Systems'
title_zh: Dream2Discern：基于难例隐式变体的多Agent运行时故障预测
authors:
- Boxuan Zhang
- jianing Zhu
- Xiaotian Han
- Ruixiang Tang
affiliations:
- Rutgers University
- The University of Texas at Austin
arxiv_id: '2610.16071'
url: https://arxiv.org/abs/2610.16071
pdf_url: https://arxiv.org/pdf/2610.16071
published: '2026-10-11'
collected: '2026-10-19'
category: Agent
direction: 多Agent系统 · 运行时故障预测
tags:
- MultiAgent
- Runtime Auditing
- Failure Prediction
- Hard Example Mining
- LoRA
one_liner: 提出交替Dream-Discern训练的运行时审计器，无需额外标注轨迹提升多Agent故障预测精度
practical_value: '- 难例生成trick可直接复用：无需额外采集标注数据，通过对模型Q/V投影层加低秩扰动生成当前模型专属难例，适合电商推荐/Agent场景下标注成本高的分类任务（如异常流量识别、Agent客服故障预判）

  - Dream-Discern训练范式可迁移：先最大化当前模型损失定位能力短板生成难例，再用难例迭代训练模型，比固定难例池训练的泛化性提升更明显，可用于排序模型、异常检测模型的小样本调优

  - 运行时校准方案可落地：按交互步拟合分位数阈值的方法，能平衡预测准确率和干预及时性，可直接用于推荐链路异常提前拦截、多Agent执行故障提前告警等需要低延迟干预的场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM驱动的多Agent系统落地时，运行时故障预测审计器依赖有限的标注轨迹语料，新增轨迹需付出高昂的执行+校验成本；传统轨迹编辑方法会改变执行走向导致原有标签失效，且泛化的故障覆盖无法针对性识别当前审计器难以分类的前缀，小样本下性能提升瓶颈明显。

### 方法关键点
- 双阶段交替训练：Dream阶段对审计器Transformer的Q/V投影层施加有界低秩扰动，最大化当前批次预测损失，生成专属难例隐式变体，无需修改原始输入和标签；Discern阶段固定扰动，训练审计器从变体中识别执行结果，扰动随模型训练动态更新，适配不同阶段的能力短板。
- 低参数开销：主干采用冻住的预训练LLM，仅微调Q/V层LoRA参数和分类头，推理时移除扰动，推理开销和普通分类器完全一致。
- 运行时校准：按交互步拟合分位数阈值，平衡预测准确率和告警及时性，支持提前干预。

### 关键实验
在AFTraj-2K（覆盖多Agent数学推理、编码、工具使用场景）和StepShield（Agent安全监控场景）两个基准上测试，对比SAFE、TRACES等SOTA审计器：轨迹级加权准确率（wACC）超过90%，比最强基线最高提升11.11%；在Qwen、Llama全系列backbone上均稳定超过基线，跨模型族泛化性好；不同告警优先级下均兼顾准确性和及时性，性能优于所有基线。

### 核心结论
无需额外采集标注数据，通过针对性扰动模型表征层生成动态难例的范式，能大幅提升小样本下分类任务的性能和泛化性。
