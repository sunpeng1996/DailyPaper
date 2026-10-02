---
title: 'Rethinking Latent Visual Reasoning: Grounding Latent Reasoning in Visual Evidence'
title_zh: 重新思考隐式视觉推理：将隐式推理过程与视觉证据对齐
authors:
- Xi Xiao
- Tianchen Zhao
- Youngeun Kim
- Zhuowei Li
- Linghan Xu
- Jiaye Wu
- Zheng Zhang
- Xiang Xu
- Xuanbai Chen
- Farhan Tejani
affiliations:
- University of Alabama at Birmingham
- Amazon AGI
arxiv_id: '2609.34563'
url: https://arxiv.org/abs/2609.34563
pdf_url: https://arxiv.org/pdf/2609.34563
published: '2026-09-27'
collected: '2026-10-02'
category: Reasoning
direction: 多模态大模型 · 隐式视觉推理优化
tags:
- Latent Visual Reasoning
- MLLM
- GRPO
- Contrastive Learning
- Visual Grounding
one_liner: 提出ReaLVR训练框架，通过双对比信号优化隐式视觉推理，无需改架构推理逻辑，可扩展至235B多模态大模型
practical_value: '- 电商多模态商品理解/搜索场景可直接复用训练思路：无需修改现有MLLM推理架构，仅在训练阶段新增双对比损失即可提升细粒度属性识别、场景推理准确率，完全不增加推理耗时

  - 推荐/Agent隐式过程的监督可借鉴信用分配trick：对于仅能获得最终结果reward的场景，通过「正确/错误输出对中间隐层的注意力差异」定位需优化的隐层位置，解决隐式建模无标注监督的痛点

  - 多模态匹配场景可复用对比损失设计：商品图文匹配、直播内容理解等场景，可通过「相关/不匹配视觉特征对比」损失强化模型对关键区域的注意力，降低幻觉输出率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Latent Visual Reasoning（LVR）通过连续隐式token完成中间推理，无需输出文本CoT，特别适合空间关系、细粒度视觉等难以用文字逐步骤描述的场景。但传统LVR的隐token仅受最终答案reward监督，存在「隐式证据-信用缺口」：隐token对会改变正确答案的图像扰动响应极弱，推理过程未和有效视觉证据绑定，极易产生幻觉。

### 方法关键点
- 提出ReaLVR训练框架，仅在训练阶段新增双对比监督信号，完全不改变原有模型架构与推理流程：
  1. **What监督**：对比相关视觉证据与不匹配证据的特征，让隐token学习区分有效视觉信息；
  2. **Where监督**：对比正确答案和模型生成的错误答案对各隐token的注意力差异，给贡献更高的隐token分配更强的监督权重；
  3. 将视觉对比损失按注意力权重加权后加入GRPO训练目标，梯度回传至隐token生成过程，强化隐层和视觉证据的绑定。

### 关键结果
在MMVP、BLINK、HRBench-4K/8K、MME-RealWorld五个视觉推理基准测试，覆盖4个模型系列7B到235B全规模均稳定提升：Qwen2.5-VL-7B上五任务平均准确率达63.7%，比最优LVR基线高0.8pp；235B规模下MMVP准确率达81.9%，比基线高1pp，是首个验证235B级隐式视觉推理可有效训练的工作。

### 核心结论
对于无显式中间监督的隐式推理场景，无需修改推理架构，仅通过「结果对比定位监督位置+证据对比定义监督内容」的训练策略，就能有效提升推理准确性与鲁棒性，同时可平滑扩展到超大规模模型。
