---
title: 'Recognition-Conditioned Reasoning: A Training-Free Multimodal-LLM Pipeline
  for Fine-Grained Micro-Action Understanding'
title_zh: 基于识别条件推理的免训练多模态大模型细粒度微动作理解流程
authors:
- Fengshun Wang
- Jin'ang Han
- Zhigang Tu
affiliations:
- Wuhan University
arxiv_id: '2608.21022'
url: https://arxiv.org/abs/2608.21022
pdf_url: https://arxiv.org/pdf/2608.21022
published: '2026-08-21'
collected: '2026-08-24'
category: Multimodal
direction: 多模态大模型 · 免训练任务路由
tags:
- Multimodal-LLM
- Training-Free
- Task Routing
- Reasoning
- Evaluation
one_liner: 提出免训练识别条件推理范式，按任务路由MLLM，获MAC2026微动作挑战赛赛道第一
practical_value: '- 免训练落地场景可按任务属性路由不同能力模型：闭域判别类任务用判别型大模型，开域生成/推理类任务用生成型大模型，大幅降低微调成本

  - 做复杂多模态业务（如直播观众微动作情绪识别、商品展示细节合规校验、生成式推荐归因解释）时，可将识别与推理解耦，用判别模型的输出作为生成推理的前置条件，提升输出可信度

  - 评估开域生成推理结果（如推荐理由、营销文案生成）时，可采用无LLM评委的金标准锚定评估方式，规避LLM打分偏见，更准确衡量推理保真度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
细粒度微动作理解需同时完成分类识别、动作部位描述、归因推理三类子任务，原有单MLLM方案能力适配性差；且MAC2026挑战赛限制微调与真值监督，亟需免训练的高性能落地方案。
### 方法关键点
1. 提出识别条件推理范式，将视觉识别与解释推理完全解耦；
2. 采用免训练动态路由机制：8项子任务分别分配给最优适配的冻结MLLM，闭域识别任务用判别型MLLM，开域描述、推理任务用生成型MLLM，且将判别模型输出的粗细粒度预测显式作为生成模型推理的前置条件；
3. 提出无LLM评委的金标准锚定评估指标，隔离推理保真度与表面语言流畅度的干扰。
### 关键结果
获得MAC2026微动作挑战赛细粒度理解赛道冠军，开域任务平均得分2.68/5，较第二名的1.44提升86%，性能优势统计显著。
