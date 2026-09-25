---
title: 'Omni Demand Understanding: A Benchmark for Contextual User-Intent Inference
  in Multimodal Interaction'
title_zh: 全需求理解：多模态交互中上下文用户意图推断基准
authors:
- Qi Chen
- Yunfei Chu
- Haolin He
- Yifan Yang
- Zihan Liu
- Yuxuan Wang
- Ziyang Ma
- Ruiyang Xu
- Meng Gao
- Yinsong Yan
affiliations:
- Shanghai Jiao Tong University
- Alibaba Group
- The Chinese University of Hong Kong
- Tsinghua University
- Johns Hopkins University
arxiv_id: '2609.21392'
url: https://arxiv.org/abs/2609.21392
pdf_url: https://arxiv.org/pdf/2609.21392
published: '2026-09-18'
collected: '2026-09-25'
category: Eval
direction: 多模态交互 · 用户意图推断评测
tags:
- Multimodal
- Intent Recognition
- Benchmark
- MLLM
- Contextual Reasoning
one_liner: 构建聚焦多模态上下文用户需求理解的基准ODU-Bench，揭示现有MLLM的意图推理能力缺口
practical_value: '- 开发电商多模态对话助手/语音购物入口时，可复用ODU的5维度需求评估框架（存在性/意图/时间/转录/用户画像）降低误触发率，尤其可针对性优化旁人间对话、朗读内容等无需求场景的识别能力

  - 构造多模态交互训练数据时，可参考ODU的Agent脚本生成+真人录制的混合pipeline，低成本覆盖指代消解、上下文依赖、环境噪声等难例场景

  - 优化多模态意图识别模块时，可重点补充视觉/对话历史维度的特征对齐，现有模型仅靠ASR转录对上下文依赖的意图恢复率不足50%'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有多模态交互基准多聚焦回复质量，默认用户需求已被正确识别，但真实场景下用户表达常遵循最小努力原则，大量指代、省略表述依赖视觉/对话/声学上下文才能理解，同时旁人间对话、朗读文本等类需求表述易引发助手误触发，缺乏专门针对多模态上下文需求理解能力的标准化评测方案。
### 方法关键点
- 定义ODU任务为5维度评测：需求存在性检测、结构化意图+所需上下文推断、需求时间定位、语音转录、用户画像预测，核心权重（60%）放在意图语义恢复
- ODU-Bench共含2078个样本，覆盖购物、家居、办公等14类场景，构造采用挑战驱动分类法引导的Agent脚本生成+真人录制混合方案，所有标注经过多轮人工校验
- 评测采用LLM Judge基于原子关键点校验意图恢复准确率，同时统计无需求场景的误触发率FTR
### 关键结果
- 评测14款主流MLLM，最强的Gemini 3.1 Pro在音视频场景整体得分仅72.6%，需结合多模态/对话上下文的关键点恢复率仅44.7%
- 11款模型的无需求场景误触发率超过50%，即使最优的Gemini 3.7 Flash也有16%误触发，Seed 2.0 Lite意图恢复率达78%但误触发率高达80.7%
- 盲测显示给模型输入正确的需求标注后，85.8%的有效判断中用户更偏好生成的回复

👉 最值得记住：多模态交互中，准确的语音转录≠正确的需求理解，强感知能力不代表上下文推理能力达标
