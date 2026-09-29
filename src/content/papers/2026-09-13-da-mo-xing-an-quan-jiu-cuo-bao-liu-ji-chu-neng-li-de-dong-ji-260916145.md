---
title: 'Safe Error Correction for Language Models: Frozen-Base Adjustment with Capability
  Preservation'
title_zh: 大模型安全纠错：保留基础能力的冻结基座调整方法
authors:
- Gautam Kishore
affiliations:
- Eulogik
arxiv_id: '2609.16145'
url: https://arxiv.org/abs/2609.16145
pdf_url: https://arxiv.org/pdf/2609.16145
published: '2026-09-13'
collected: '2026-09-29'
category: LLM
direction: 大模型纠错 · 参数高效能力保留微调
tags:
- Error Correction
- Parameter Efficient Fine-Tuning
- LoRA
- DPO
- Capability Preservation
one_liner: 提出34M参数轻量logit级纠错模块，无基座能力损失下修正53.3%的基座错误
practical_value: '- 电商客服/导购Agent场景可复用「冻结基座+logit层修正+KL锚定」架构，在不损失通用对话能力的前提下修复特定领域（商品参数、活动规则）的回答错误，避免LoRA微调带来的通用能力退化

  - 生成式推荐场景下，若用LLM生成推荐理由/文案，可叠加轻量logit修正模块，修正不符合平台规则、错误的商品属性表述，同时保留LLM原有的文案生成质量

  - 工程上该方法仅需训练<1%参数的小模块，训练成本极低（M4笔记本25分钟即可完成训练），适合中小业务快速迭代特定错误的修复规则'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型部署中常出现事实错误、推理错误，直接用LoRA等微调方案修正错误会导致基座原有通用能力大幅退化，存在显著的纠错-能力权衡问题，亟需能在不损失基座能力的前提下修复特定错误的生产可用方案。

### 方法关键点
- 架构：冻结全量Gemma 4 E2B 4.65B基座，仅在顶部加34M参数（占基座0.73%）的轻量CRN v2模块，读取基座最终隐状态输出加法性logit修正值，基座参数全程不更新
- 训练：分两阶段，第一阶段SFT用83400条纠错对，损失为任务交叉熵加λ=0.1的KL散度正则项，锚定修正后的分布与基座分布的差异；第二阶段用无参考DPO，偏好正确答案而非基座的错误输出
- 变体探索：测试了深层隐状态注入的纠错方案，仅需1.6M参数，但发现DPO阶段会破坏基座能力

### 关键结果
- 纠错效果：CEHRI领域考试（60题，覆盖事实、算术、隐式目标推理）上，CRN v2修正53.3%的基座错误，改写版考题修正率43.3%；同数据训练的LoRA基线修正率83.3%，但MMLU、BoolQ、car-wash基准测试上能力下降17~75个百分点
- 能力保留：CRN v2在MMLU、BoolQ、car-wash三个基准上的表现与冻结基座完全一致，无任何可测退化
- 消融：KL正则项λ从0.1降到0.01时，纠错率降至35%，锚定项对效果影响显著

最值得记住的话：牺牲部分纠错率换得全量基座能力的无损保留，比高纠错率但能力大幅退化的方案更适合生产部署。
