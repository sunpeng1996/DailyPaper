---
title: 'Judging the Justification: Decision Certificate Supervision for Generative
  Reward Models'
title_zh: 生成式奖励模型的无参考决策证书监督框架DECERT
authors:
- Guiquan Sun
- Bing Bai
- Martin Renqiang Min
- Dongjin Song
affiliations:
- University of Connecticut
- NEC Labs America
arxiv_id: '2610.27528'
url: https://arxiv.org/abs/2610.27528
pdf_url: https://arxiv.org/pdf/2610.27528
published: '2026-10-19'
collected: '2026-10-27'
category: Training
direction: 生成式奖励模型 · 无参考推理监督
tags:
- Generative Reward Model
- Rationale Supervision
- DPO
- LLM Alignment
- Positional Robustness
one_liner: 提出无参考解释的DECERT框架，从三维度监督生成式奖励模型推理，同时提升判断准确率和位置鲁棒性
practical_value: '- 电商场景LLM-as-a-Judge任务（如生成文案质量判分、商品问答合理性校验）可复用DECERT三维评分逻辑：从证据真实性、核心维度覆盖度、理由-结论一致性三个维度评估生成推理质量，无需人工标注参考解释即可优化判分模型。

  - 优化推荐Agent/生成式推荐模型的RLHF流程时，可复用同判决结果下的推理偏好对构造方法：对多个输出结果相同的生成样本，按推理质量排序构造DPO训练对，无需额外标注即可提升模型推理一致性，减少幻觉。

  - 解决排序类任务位置偏差（如商品曝光顺序偏置、候选Item顺序偏置）可借鉴该思路：通过监督推理过程而非仅最终判决结果，无需swap数据增强即可提升位置鲁棒性，论文实测最高提升14.8个百分点的位置一致准确率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
生成式奖励模型（GenRM）输出自然语言推理理由后再给出偏好判断，但仅靠判决结果监督无法区分「结果正确但推理错误」的样本；现有推理监督方法依赖参考解释，标注成本高，且无法验证生成理由是否真的支撑判决结果，还会否定和参考表述不同但逻辑有效的正确推理。

### 方法关键点
- 定义决策证书三维无参考评估维度：Soundness（理由引用的证据和局部推理逻辑是否有效）、Coverage（理由是否覆盖所有核心决策问题）、Decision Support（推理得出的结论是否和最终判决一致），无需参考解释即可完成自动化评分。
- 偏好对构造策略：判决正确性优先级高于推理质量，对所有采样样本先按「判决正确得分+λ*推理质量得分」的总分排序构造通用偏好对；如果所有采样样本判决都正确，则直接按推理质量分差构造纯推理偏好对。
- 训练流程：先用高分样本做SFT热身，再用两类偏好对做DPO训练，全程用LoRA降低训练成本。

### 关键实验
基于HelpSteer3数据集构造10k SFT样本、8k DPO对，基于Llama3.1-8B、Qwen3-8B训练，对比Outcome-only基线、R-Align等SOTA GenRM：对比Outcome-only基线，Llama3.1-8B的位置一致准确率（PCA）提升14.8个百分点，Qwen3-8B的RM-Bench准确率提升2.7个百分点；无swap增强的前提下，证据适配率（EAR）从64.5%提升到88.9%，过期理由率下降22.9个百分点。

**最值得记住的一句话**：监督判决的推理过程比仅监督判决结果更能提升模型的鲁棒性和泛化性，无需参考解释的推理质量评估可以大幅降低监督成本。
