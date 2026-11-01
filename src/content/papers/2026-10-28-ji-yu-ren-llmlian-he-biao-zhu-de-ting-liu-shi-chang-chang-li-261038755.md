---
title: Leaving, Staying, or Living There? Duration Commonsense Reasoning with Human-LLM
  Co-annotations
title_zh: 基于人-LLM联合标注的停留时长常识推理研究
authors:
- Chenyang Yu
- Zhaomin Xiao
- Yan Huang
- Eduardo Blanco
affiliations:
- University of North Texas
- University of Arizona
arxiv_id: '2610.38755'
url: https://arxiv.org/abs/2610.38755
pdf_url: https://arxiv.org/pdf/2610.38755
published: '2026-10-28'
collected: '2026-11-01'
category: Reasoning
direction: 多模态常识推理 · 人-LLM联合标注
tags:
- Commonsense Reasoning
- Multimodal Understanding
- Human-LLM Co-annotation
- Vision-Language Model
- Social Media Mining
one_liner: 构建人-LLM联合标注的地理标记推文语料，验证现有多模态模型时长推理能力缺陷
practical_value: '- 人-LLM联合标注流程可复用：针对需常识推理的标注任务，先由LLM初标再人工校验，可大幅降低标注成本

  - 多模态理解场景可优化特征融合策略：避免过度依赖显性视觉特征，需叠加文本细粒度语义（如hashtag、上下文表述），提升用户停留时长、意图预测准确率

  - 社交平台用户停留时长推断方法可迁移到本地生活、旅游推荐场景，优化POI推荐、行程规划的个性化程度'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
社交平台用户行为很少明确标注停留时长，需从多模态、上下文线索推断，该能力对出行需求预测、个性化推荐等场景至关重要，但现有多模态模型的时长常识推理能力尚未得到系统验证
### 方法关键点
1. 构建人-LLM联合标注的带地理标记推文语料作为测试集，覆盖不同停留时长的行为场景
2. 测试SOTA视觉语言模型的时长推理表现，对比有无多轮Chain-of-Thought prompting的效果差异
3. 开展错误分析定位模型核心缺陷
### 关键结果
即使加入多轮Chain-of-Thought引导，SOTA多模态模型的时长推理表现仍较差；错误主要来自两类问题：一是无法整合关键上下文信息，二是过度依赖显性视觉特征，忽略文本侧的hashtag、细粒度语义差异
