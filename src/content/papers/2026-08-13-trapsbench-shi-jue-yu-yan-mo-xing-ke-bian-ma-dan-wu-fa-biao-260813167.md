---
title: 'TRAPSBench: Vision-Language Models Encode but Fail to Express Epistemic Restraint'
title_zh: TRAPSBench：视觉语言模型可编码但无法表达认知克制
authors:
- Fnu Pramono
- John Cai
- Sourabh Kulkarni
affiliations:
- Meta Superintelligence Labs
arxiv_id: '2608.13167'
url: https://arxiv.org/abs/2608.13167
pdf_url: https://arxiv.org/pdf/2608.13167
published: '2026-08-13'
collected: '2026-08-14'
category: Eval
direction: 多模态模型认知能力评测
tags:
- VLM
- Benchmark
- Epistemic Restraint
- Evaluation Metric
- Multimodal Reasoning
one_liner: 推出TRAPSBench评测基准与PECS指标，证实VLM认知克制瓶颈在输出而非感知阶段
practical_value: '- 多模态商品理解/直播内容理解的可靠性评估可复用PECS指标，同时考核可回答场景准确率、不可回答场景拒答率，降低幻觉风险

  - 多模态导购Agent/智能审图系统遇到视觉信息缺失（商品遮挡、画面模糊）时，可先通过隐层探针判断可回答性，再在输出层加干预强制拒答

  - 多模态模型校准优化可优先针对输出层做干预，无需重新训练视觉编码器，大幅降低优化成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
VLM落地时认知克制能力（证据不足时主动拒答）对可靠性至关重要，但现有物理推理基准未覆盖证据不足场景的拒答评测，无法衡量模型真实可用水平。

### 方法关键点
1. 构建TRAPSBench基准，含1404组配对物理视频样本，单变量修改后视觉证据无法确定结果，专门用于评测拒答能力；2. 提出PECS指标，同时衡量可回答场景准确率、不可回答场景拒答率，鲁棒性更强；3. 测试16款跨5个系列的VLM，结合线性探针、隐层方向steering定位性能瓶颈。

### 关键结果数字
16款VLM自发拒答能力极差，最高PECS仅0.292；瓶颈在输出层而非感知层：隐层线性探针解码可回答性AUROC最高达0.91，单隐层方向引导可直接控制拒答行为；VLM检测文本不确定性的能力是视觉缺失场景的4倍，优化需优先针对输出层干预。
