---
title: 'TLRS-DPO: Token-Level Risk Scoring for Better Direct Preference Optimization'
title_zh: TLRS-DPO：基于Token级风险打分的增强型直接偏好优化
authors:
- Suxin Ji
- Hungtao Wan
affiliations:
- University of Pennsylvania
- Independent Researcher
arxiv_id: '2611.11232'
url: https://arxiv.org/abs/2611.11232
pdf_url: https://arxiv.org/pdf/2611.11232
published: '2026-11-08'
collected: '2026-11-10'
category: Training
direction: LLM对齐 · DPO训练优化
tags:
- DPO
- LLM Alignment
- Token-Level Optimization
- Preference Tuning
- RLHF
one_liner: 为标准DPO引入轻量化Token级风险打分与课程式惩罚，无需额外数据即可提升对齐效果与训练稳定性
practical_value: '- 做LLM驱动的Agent、生成式推荐文案对齐时，可直接将TLRS-DPO作为DPO的drop-in替换，仅增加5%以内GPU开销即可获得10%+的对齐效果提升，尤其适合商品文案合规性管控、推理类导购回答的错误抑制场景

  - Token级风险打分机制可直接复用在生成式推荐的不良内容识别上，无需额外训练安全模型，通过policy与reference模型的token概率差即可快速定位高风险生成片段（如虚假宣传、违规词）

  - 课程式惩罚策略可迁移到所有对比偏好训练任务中，训练初期降低细粒度惩罚权重避免训练震荡，后期逐步提升权重优化细节，能适配标注噪声较高的业务偏好数据（比如用户点击/负反馈的噪声数据）'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
标准DPO作为RLHF的轻量化替代方案被广泛用于LLM对齐，但序列级损失设计将整段响应作为单一比较单元，无法精准定位并抑制响应中局部的错误、有害token，会导致训练梯度方差大、收敛慢，对标注噪声鲁棒性差，在数学推理、安全对齐、结构化内容生成场景下效果受限。

## 方法关键点
- 拆解DPO隐式奖励为token级贡献，计算当前policy与reference模型在拒绝响应上每个token的对数概率差作为基础风险分
- 采用中位数绝对偏差（MAD）自适应筛选高风险token集合，仅对高风险token增加惩罚项，避免影响正常token的学习
- 引入课程式权重调度，训练过程中逐步提升token级惩罚的强度，前期保证序列级对齐的稳定性，后期优化细节
- 整体损失为原DPO损失加token级补偿项，可直接嵌入现有DPO训练框架，无额外数据依赖

## 关键结果
在LLaMA-3-Instruct-8B、Mistral-7B-Instruct等模型上验证，对比标准DPO、SimPO、TIS-DPO等SOTA基线：AlpacaEval 2.0、Arena-Hard win rate分别达73.4%、64.1%，较标准DPO提升超10%；Llama-Guard安全率达86.8%，GSM8K-Pref推理准确率达67.5%；20%标注噪声下性能仅下降2.9%，收敛速度为DPO的1.18倍，GPU开销仅增加5%。

最值得记住的一句话：细粒度的token级风险管控相比粗粒度的序列级对齐，能以极低的额外成本同时提升偏好优化的效果、稳定性与噪声鲁棒性。
