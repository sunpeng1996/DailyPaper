---
title: 'When Quantization Preserves Accuracy but Not Evidence: Explanation-Aware Post-Training
  Quantization for Medical LLMs'
title_zh: 解释感知医疗大模型训练后量化：兼顾答案精度与推理证据保留
authors:
- Yeji Kim
- Mi-Young Kim
- Randy Goebel
affiliations:
- University of Alberta
arxiv_id: '2609.24799'
url: https://arxiv.org/abs/2609.24799
pdf_url: https://arxiv.org/pdf/2609.24799
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: LLM训练后量化 · 解释一致性保留
tags:
- PTQ
- Quantization
- Medical-LLM
- Explanation-Faithfulness
- LLM-Compression
one_liner: 提出双损失解释感知PTQ框架，低比特量化下保留医疗LLM答案准确性与支撑证据一致性
practical_value: '- 低比特LLM部署评估不能仅用准确率，需新增业务核心信息保留率指标（比如电商推荐理由的核心卖点保留、客服回答的依据一致性），避免量化后输出看似正确实则核心信息丢失的隐蔽故障

  - 可复用双阶段PTQ优化思路：先用基准PTQ得到探针模型，定位易受量化损失的关键token/片段，再针对性加损失做细粒度保留，完全不增加推理成本

  - 对于需要输出可解释内容的业务场景（可解释推荐、智能客服应答），可复用证据缓存+加权损失的思路，在量化/蒸馏等模型压缩阶段保留核心支撑信息，提升用户对输出的信任度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有PTQ方法仅以重建误差、困惑度、答案准确率为优化目标，在医疗等高解释敏感场景下，会出现量化后答案正确但支撑推理的核心证据被篡改、遗漏甚至编造的问题。诊断发现标准量化损失的优化信号83%被通用话语token占据，真正关键的领域证据token得不到足够保护，导致量化模型的输出可信度大幅下降，无法满足监管与用户信任要求。

### 方法关键点
- 双阶段PTQ流程：第一阶段用标准OSTQuant得到量化探针模型，第二阶段结合离线faithfulness cache做解释感知优化，最终部署的W4A4KV4量化模型与基线推理成本完全一致
- 离线证据缓存构建：仅保留全精度模型答对的校准样本，用大模型提取全精度输出中支撑答案的核心证据片段，筛选出量化后支撑效果下降的片段，生成token级权重
- 双辅助损失设计：① 推理token损失：加权优化量化前后核心证据token的分布一致性，优先保护易受损证据；② 推理条件恢复损失：优化证据对应的答案偏好分布一致性，确保证据对答案的支撑逻辑不变

### 关键实验
在MedExQA、MedExpQA、ChallengeClinicalQA三个医疗QA数据集上，对4款7B-8B量级医疗/指令微调LLM做W4A4KV4量化，对比同校准集的OSTQuant基线：整体全精度答案一致性从68.44%提升至79.86%，答案自支撑率（PredRec）从75.96%提升至87.68%，答案准确率无明显下降；MedExpQA场景下，全精度证据保留率（FER）平均提升5.34个百分点，无依据错误claim率（UCR）平均下降4.65个百分点。

### 核心结论
低比特模型压缩的评估不能仅看最终答案准确率，必须针对业务核心需求新增关键信息保留指标，避免出现「答案对但逻辑错」的隐蔽故障。
