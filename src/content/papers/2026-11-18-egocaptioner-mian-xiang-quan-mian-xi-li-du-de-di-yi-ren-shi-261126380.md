---
title: 'EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning'
title_zh: EgoCaptioner：面向全面细粒度的第一人称视频字幕生成
authors:
- Yuqi Tang
- Yang Shi
- Yuran Wang
- Tengfei Liu
- Rundong Wang
- Zongyang Qiu
- Qixun Wang
- Zhuoran Zhang
- Xuanyu Zhu
- Yifan Xu
affiliations:
- HKUST(GZ)
- KlingAI Research
- PKU
- USTC
- NJU
arxiv_id: '2611.26380'
url: https://arxiv.org/abs/2611.26380
pdf_url: https://arxiv.org/pdf/2611.26380
published: '2026-11-18'
collected: '2026-11-20'
category: Multimodal
direction: 多模态大模型 · 第一人称视频字幕生成
tags:
- Multimodal LLM
- Video Captioning
- Egocentric Video
- GRPO
- Fine-grained Annotation
one_liner: 提出粗到细标注+多奖励优化的带时间戳第一人称视频字幕框架，性能领先主流开源/闭源基线
practical_value: '- 粗到细的标注流程可复用在短视频/直播内容打标场景，先定事件结构再补细节，大幅提升标注效率与数据质量

  - 多维度互补奖励（事实准确性、时序对齐、冗余惩罚）+GRPO的优化范式，可迁移到生成式商品文案、短视频种草文案的LLM微调场景，解决生成内容时序混乱、冗余问题

  - 引入传感器/姿态等多源数据补充事实监督的思路，可用于电商直播场景中主播动作、商品互动的自动识别打标，提升内容标签准确率'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前MLLM生成第一人称视频字幕时易遗漏短时动作、混淆时序、误判佩戴者动作，现有字幕格式无法同时兼顾细节描述与精准时序匹配。
### 方法关键点
1. 输出结构包含视频级全局概述（场景、参与者、整体活动）+带时间戳的分步骤细粒度描述，适配不同场景感知需求；
2. 搭建粗到细标注pipeline，先确定事件结构再扩展步骤描述，从8个第一人称视频源生成5万训练样本；
3. 设计覆盖事实准确性、时序对齐度、冗余惩罚的互补奖励机制，结合GRPO引导字幕优化，有姿态传感器数据时补充动作事实监督提升可靠性。
### 关键结果
在5个第一人称视频基准上，字幕质量、字幕条件问答、时序对齐效果均为参评开源模型最优；PhysCapBench上超越Gemini 3.1 Pro，Minerva-Ego基准字幕转QA指标超过所有参评闭源基线；ablation验证多奖励互补性，粗到细标注比单轮标注监督效果更优。
