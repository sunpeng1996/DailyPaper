---
title: 'I Seek You in Videos: Identity-Conditioned Queries for Person-Centric Video
  Reasoning'
title_zh: 在视频中检索特定人物：面向以人为中心视频推理的身份条件查询
authors:
- Shibo Gao
- Chongxiao Wang
- Chenglong Huang
- Jie Ma
- Haolin Shi
- Fei Ding
- Jing Li
- Qiang Lyu
- Yangyang Liu
- Yang Liu
affiliations:
- Beijing Jiaotong University
- HUJING Digital Media & Entertainment Group
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Tongji University
arxiv_id: '2608.07417'
url: https://arxiv.org/abs/2608.07417
pdf_url: https://arxiv.org/pdf/2608.07417
published: '2026-08-07'
collected: '2026-08-10'
category: Multimodal
direction: 多模态推理 · 以人为中心视频理解
tags:
- Multimodal Reasoning
- Video Understanding
- Person Retrieval
- Benchmark
- MLLM
one_liner: 提出身份条件查询ICQ任务及配套数据集、基准、模型，提升以人为中心的视频推理能力
practical_value: '- 电商直播特定人物行为分析、达人内容检索场景，可复用「参考图像+视频联合关联推理」范式，优化身份匹配与行为理解精度

  - 构建多模态训练数据集时，可参考「自动标注+多轮校验+人工复核」流水线，低成本生成高质量大规模训练样本

  - 长视频内容理解场景，可借鉴无需额外镜头级标注的信息挖掘训练策略，降低标注成本同时提升关键帧利用效率'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有视频推理任务多采用简化的视频-文本双模态设置，难以支撑真实场景下的身份匹配、以人为中心的复杂推理需求。
### 方法关键点
1. 定义身份条件查询（ICQ）任务，要求模型联合关联输入视频与人物参考图像，完成身份定位、行为理解、时序推理等多类任务；
2. 推出ISYV体系：包含覆盖6级难度、从身份识别到因果推理全能力的1377条真实视频+问答对的ISYV-Bench评估基准，75K经多环节校验的高质量ISYV-75K训练集，以及无需额外镜头级标注即可挖掘有效视频镜头的ICQ专属模型与训练策略。
### 关键结果
主流闭源/开源MLLM在ISYV-Bench上表现较差，跨域身份匹配、长序列追踪能力短板明显；ISYV模型显著优于所有基线，部分能力接近闭源MLLM水平。
