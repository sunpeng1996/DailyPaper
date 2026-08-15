---
title: 'NARU: A Benchmark for NARrative Evolution and Cultural Nuance Understanding
  in Japanese Extreme Long Video'
title_zh: NARU：面向日语超长视频叙事演化与文化细节理解的基准
authors:
- Yuheng Huang
- Jianlang Chen
- Jiayang Song
- Hua Qi
- Aza Kai
- Vincent Markert
- Edison Marrese-Taylor
- Jianjun Zhao
- Lei Ma
affiliations:
- The University of Tokyo
- Kyushu University
- Macau University of Science and Technology
arxiv_id: '2608.13210'
url: https://arxiv.org/abs/2608.13210
pdf_url: https://arxiv.org/pdf/2608.13210
published: '2026-08-13'
collected: '2026-08-15'
category: Eval
direction: 多模态长视频理解 · 基准评测
tags:
- Long-form Video Understanding
- MLLM
- Benchmark
- Cultural Reasoning
- Video QA
one_liner: 发布含146.8小时日语长视频的多维度评测基准NARU，配套分层标注流水线，暴露现有MLLM能力缺陷
practical_value: '- 做跨境日语内容/商品短视频/直播推荐的团队，可参考其文化维度标注框架，优化本地化内容理解模块的评测指标

  - 处理长视频（如直播回放、达人长视频）内容理解的场景，可复用其分层记忆式结构化标注流水线，降低大规模标注成本

  - 做多模态Agent长时序信息处理能力评测时，可参考其迭代去shortcut的问题生成方法，提升评测集区分度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有长视频理解基准多聚焦孤立事件检索，未同时覆盖叙事演化跟踪、隐性文化语义解读能力评测，且缺乏高语境非英语（如日语）语料的相关评测集。
### 方法关键点
1. 构建NARU基准，包含155条总时长146.8小时的日语长视频，配套1481道评测题，覆盖4类叙事维度、5类文化维度；
2. 提出分层记忆式标注流水线，先将原始视频转化为事件、叙事、文化结构化标注，再通过任务导向合成+迭代消除捷径生成评测题，全程包含2轮母语者验证，共68名标注者参与。
### 关键结果
对8种主流MLLM配置的评测显示，现有模型在长时序叙事整合、文化落地推理两个方向均存在显著能力缺陷。
