---
title: 'From Counterfactual Edits to Human Narratives: LLM-Driven Interpretations
  for Recommender System Explanations'
title_zh: LLM驱动的推荐系统反事实编辑到人类可读叙事转化方法
authors:
- Vojtech Cahlik
- Amir Reza Mohammadi
- Rodrigo Alves
- Pavel Kordik
- Eva Zangerle
affiliations:
- Czech Technical University in Prague
- University of Innsbruck
arxiv_id: '2611.13914'
url: https://arxiv.org/abs/2611.13914
pdf_url: https://arxiv.org/pdf/2611.13914
published: '2026-11-10'
collected: '2026-11-11'
category: RecSys
direction: 推荐系统可解释性 · 反事实解释
tags:
- Recommender Systems
- Counterfactual Explanation
- Natural Language Explanation
- LLM
- Direct Preference Optimization
one_liner: 利用LLM将推荐系统冗长反事实编辑列表转为高保真可读自然语言解释，通过DPO优化生成质量
practical_value: '- 电商/内容推荐场景可直接复用该框架，将SHAP、LIME等生成的长序列特征重要性列表/交互编辑列表，输入小参数LLM生成用户易懂的推荐理由，降低用户困惑、提升平台信任度

  - 生成解释的prompt设计可复用「同时输入反事实编辑样本+剩余用户历史样本」的逻辑，避免生成的解释过于泛化，有效提升解释与用户真实偏好的匹配度

  - 解释质量优化可复用DPO偏好优化流程，先用LLM judge打分构建配对训练数据，对小参数LLM做DPO微调，平衡生成质量与推理成本，实测可提升10%左右的解释正确性

  - 解释效果评估可参考「正确性+信息度+语言质量」三维指标，用少量人工标注训练小分类器做自动评估，替代纯人工评估降低评测成本，评估准确率可达90%以上'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐系统的反事实解释（CFX）可明确指出修改哪些用户历史交互会改变推荐结果，是提升推荐透明度、用户信任的核心手段，但现有CFX方法输出的往往是数十条交互组成的长列表，普通用户难以理解；同时现有评估仅关注编辑数量、成功率，完全忽略解释的可读性和用户可理解性，导致反事实解释无法落地到ToC场景。
### 方法关键点
- 构建4阶段Pipeline：先调用现有CFX方法生成用户历史交互编辑列表，再分别采样反事实交互、剩余用户历史交互的元数据（如商品类目、发布时间等），将两类数据输入LLM生成自然语言解释，最后通过DPO优化解释质量
- 设计三维评估指标：正确性（解释和反事实交互的匹配度）、信息度（解释对反事实交互和剩余历史的区分度，避免泛化）、语言质量（流畅度、简洁度等），先通过LLM judge生成优化信号，最终用人工校准的分类器做落地评估
- 用DPO微调生成LLM：基于三维指标构建配对偏好数据，微调小参数LLM，在不损失语言质量的前提下提升解释的保真度
### 关键实验
在MovieLens-1M数据集上测试，对比Jaccard、Cosine、LIME-RS、SHAP、ACCENT、SPINRec共6种CFX生成器，以及Ministral 8B、Gemma3 12B、Qwen3 8B三款LLM；其中ACCENT、SPINRec的CFX成功率最高（0.99、1.00），生成的解释正确性最高可达0.51；DPO微调几乎在所有场景下都能提升正确性和信息度，语言质量整体保持在0.8以上（人工校准评分）。
### 核心结论
将反事实解释落地到用户端的核心不是最小化编辑数量，而是把低阶的交互编辑转化为符合人类认知的高阶偏好模式，LLM是实现这一转化的低成本高效方案。
