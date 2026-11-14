---
title: 'SPADE: Soft Prompts for Ai-text DEtection'
title_zh: SPADE：基于软提示的AI生成文本检测方法
authors:
- Alex Jiang
- Didier Schwab
- Chuyuan Li
affiliations:
- ChapsVision, France
- Univ. Grenoble Alpes, France
arxiv_id: '2611.16929'
url: https://arxiv.org/abs/2611.16929
pdf_url: https://arxiv.org/pdf/2611.16929
published: '2026-11-12'
collected: '2026-11-14'
category: LLM
direction: LLM内容安全 · AI生成文本检测
tags:
- AI Text Detection
- Soft Prompt
- PMI
- OOD Generalization
- LLM Security
one_liner: 提出利用PMI量化提示影响、按类别训练软提示的AI文本检测框架，OOD场景性能达SOTA
practical_value: '- 电商UGC/AI生成商品文案/评论的真实性校验场景，可复用PMI量化提示对生成文本的影响特征，替代单纯的NLL特征，提升跨场景检测准确率

  - Agent生成内容风控模块可借鉴按类别训练专属软prompt的思路，低成本适配客服话术、营销文案等不同生成场景的检测需求

  - 各类OOD分类任务均可参考「捕捉生成过程隐信号+训练类别专属软prompt放大差异」的范式，提升跨域泛化性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有AI文本检测器仅关注生成文本本身，忽略底层生成过程中prompt的影响，监督方法依赖标注数据、零样本方法仅依赖文本概率分布，开放OOD场景下鲁棒性差，跨数据集迁移效果差。

### 方法关键点
1. 引入Pointwise Mutual Information (PMI) 指标量化prompt对生成文本的解释度，作为区分AI/人类文本的判别信号
2. 为AI、人类两个类别各训练1个专属软prompt，放大两类样本的特征差异
3. 推理时判断候选文本与哪个类别的软prompt匹配度更高，输出分类结果

### 关键结果
在多个基准数据集的OOD测试集上性能达SOTA，相比基于NLL的基线检测方法，在Qwen/LLaMA/Falcon等不同基座下AUC最高提升0.39
