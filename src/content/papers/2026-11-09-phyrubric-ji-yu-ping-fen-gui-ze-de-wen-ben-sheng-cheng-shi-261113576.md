---
title: 'PhyRubric: Rubric-Grounded Diagnostic Evaluation of Physical Commonsense in
  Text-to-Video Generation'
title_zh: PhyRubric：基于评分规则的文本生成视频物理常识诊断评估框架
authors:
- Huiyi Chen
- Weitai Kang
- Shicheng Fan
- Xinshuo Wang
- Zhixiang Shen
- Yan Yan
- Philip S. Yu
- Baoxin Li
affiliations:
- University of Illinois Chicago
arxiv_id: '2611.13576'
url: https://arxiv.org/abs/2611.13576
pdf_url: https://arxiv.org/pdf/2611.13576
published: '2026-11-09'
collected: '2026-11-12'
category: Eval
direction: 多模态生成 · 物理常识评测
tags:
- Evaluation
- Text-to-Video
- Commonsense Reasoning
- LLM Judge
- Multimodal
one_liner: 提出基于预设评分规则的T2V物理常识评估框架、评测集与开源Judge，性能对齐Gemini 4 Argon
practical_value: '- 电商场景下商品短视频/3D展示内容生成的质检环节，可复用rubric前置构建、分维度细粒度判别的思路，替代主观人工质检，降低不合物理常识的错误内容流出率

  - 自研LLM Judge做内容合规/推荐效果评估时，可参考先针对query/prompt预构建专属评分项、再匹配对应证据给分的范式，提升判分和人类意愿的一致性

  - 构建垂直领域评测集时，可借鉴分维度拆解评估指标、配套对应训练数据微调开源Judge的方案，低成本得到对齐闭源SOTA的自研评测模型'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文本生成视频（T2V）的物理常识评估依赖人工单分值直觉打分，主观性强，无法定位具体违反的物理规则，难以有效支撑模型迭代优化。
### 方法关键点
1. 提出PhyRubric评估框架：在生成视频前先针对输入caption预构建专属评分规则，拆解为语义、物理两类评估项，基于带时间戳的视频证据给出项级判定后汇总得分
2. 构建跨5个物理域34个类别的PhyRubric-Bench评测集，配套3788条视频的PhyRubric-Train训练集，微调得到开源PhyRubric-Judge
### 关键结果
在10个主流T2V模型上验证，当前T2V物理常识能力仍存在明显短板；PhyRubric-Judge与人类判定的相关性优于现有开源评测模型，性能对齐闭源SOTA Gemini 4 Argon
