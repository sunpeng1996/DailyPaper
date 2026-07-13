---
title: Evolution of Accuracy and Visual-Cognitive Errors in a Decade of Vision-Language
  AI Models
title_zh: 十年间视觉语言AI模型的准确率与视觉认知误差演进
authors:
- Shravan Murlidaran
- Miguel P. Eckstein
affiliations:
- University of California, Santa Barbara
arxiv_id: '2607.09654'
url: https://arxiv.org/abs/2607.09654
pdf_url: https://arxiv.org/pdf/2607.09654
published: '2026-07-10'
collected: '2026-07-13'
category: Eval
direction: 多模态大模型 · 性能与误差评估
tags:
- VLM
- MLLM
- Multimodal Evaluation
- Hallucination
- Visual Cognition
one_liner: 提出复杂社交行为数据集CSB，量化2017-2025年VLM的准确率演进与五类视觉认知误差特征
practical_value: '- 电商多模态内容理解（如商品图识别、直播场景理解）场景下，可参考本文划分的5类视觉认知误差做bad case归因，优先优化检测、识别、幻觉三类高影响误差

  - 针对复杂交互场景的多模态任务，可参考CSB数据集的构建思路补充场景测试集，避免仅用MS-COCO类简单场景高估模型的实际业务表现

  - 业务选型MLLM做图文理解任务时，可优先验证空间依赖类误差是否符合业务要求，该类误差是当前MLLM残留的核心问题'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有VLM评估多采用MS-COCO等简单场景数据集，缺乏对复杂社交交互场景的覆盖，也未系统拆解模型误差类型，无法真实反映模型在复杂场景下的落地性能。

### 方法关键点
构建包含100张复杂社会交互场景的CSB数据集，选取2017-2025年共9款VLM（4款预MLLM、5款MLLM），以20份人类标注的描述为金标准，分析五类视觉认知误差：目标检测、识别、幻觉、场景理解、空间依赖。

### 关键结果
1. CSB数据集上MLLM描述准确率已达人类top水平，预MLLM准确率低于人类最低水平；
2. MLLM已完全消除MS-COCO简单场景与CSB复杂场景的描述准确率差距；
3. 除空间依赖误差外，MLLM几乎消除其余四类误差，其中检测、识别、幻觉三类误差对准确率影响最大。
