---
title: 'VepAgent: Bridging Causal-Transition via Tool-Augmented Reinforcement Learning
  for Video Event Prediction'
title_zh: VepAgent：工具增强强化学习桥接因果过渡的视频事件预测框架
authors:
- Qiutong Chen
- Yuchan Guo
- Zhenlong Yuan
- Haobo Yang
- Fangfang Lin
- Xinyi Long
- Yin Wang
- Zijian Song
- Rui Lan
- Shi Qiu
affiliations:
- Nankai University
- Carnegie Mellon University
- Xiaohongshu Inc.
- Columbia University
- University of California, Santa Cruz
arxiv_id: '2610.06293'
url: https://arxiv.org/abs/2610.06293
pdf_url: https://arxiv.org/pdf/2610.06293
published: '2026-10-04'
collected: '2026-10-08'
category: Agent
direction: 多模态Agent · 视频事件因果预测
tags:
- Multimodal Agent
- Reinforcement Learning
- Video Event Prediction
- Tool Augmentation
- Causal Reasoning
- GRPO
one_liner: 提出融合因果过渡推理、工具增强RL与抗先验奖励的多模态Agent 实现视频事件预测SOTA
practical_value: '- 抗先验奖励设计可直接迁移到推荐/搜索场景：抑制模型依赖文本表面相似性的捷径行为，强制模型基于用户真实行为/内容语义生成结果，解决query和item语义匹配偏差问题

  - 先SFT冷启动再RL优化的两阶段训练策略，可用于低成本给小参数MLLM注入工具调用能力，避免直接RL训练时工具调用率退化的问题，适合业务侧小模型落地

  - 动态多工具调用框架可复用在电商短视频/直播理解场景：针对商品细节模糊、动作序列不连续的问题，按需调用帧检索、区域放大等工具补全信息，提升内容标签准确率、用户行为预测精度

  - 因果过渡推理的CoT数据集构造方法，可用于构造业务场景的推理链标注数据，比如用户后续下单行为预测、内容消费时长预测，大幅提升小模型推理性能'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态大模型（MLLM）在视频事件预测（VEP）任务中存在三个核心缺陷：一是仅能回溯历史事件，无法桥接观测终态到未来事件的因果逻辑gap；二是依赖语言先验走捷径，优先选择与查询文本相似度高的答案而非基于视觉证据推理；三是视频存在遮挡、运动模糊、采样不足等问题时，缺失关键视觉证据导致预测偏差。VEP是自动驾驶、智能监控、短视频内容理解等场景的核心基础能力，亟需更可靠的推理框架。
### 方法关键点
1. 构造FutureBench-4K因果推理Chain-of-Thought（CoT）数据集，用于Supervised Fine-Tuning（SFT），明确建模从观测终态、未完成动作到未来事件的推理链路，填补因果逻辑gap
2. 设计4种诊断工具库：状态跟踪器梳理动作序列与终态、帧检索器补全缺失关键时序证据、区域放大镜放大关键空间区域、视觉细节提取器将细粒度视觉特征转成文本锚定推理
3. 采用Group Relative Policy Optimization（GRPO）做Reinforcement Learning（RL）优化，复合奖励包含三部分：准确率奖励、因果过渡一致性奖励、抗先验惩罚（正确选项与查询文本相似度越低奖励越高，抑制语言捷径）
4. 采用两阶段训练策略：先SFT冷启动训练工具调用和因果推理能力，再RL优化，避免直接RL训练时工具调用率下降的问题
### 关键结果
在FutureBench数据集上，4B参数的VepAgent比之前最优的Qwen3-VL-30B-A3B准确率提升14.58个百分点，从66.86%到81.44%；在NEPBench数据集上，比之前最优的Qwen2.5-VL-72B准确率提升22.7个百分点，从47.5%到70.2%，大幅超越更大参数的通用MLLM基线。
最值得记住的结论：给小参数多模态模型加入主动工具调用能力+抗捷径的复合奖励设计，可在因果预测类任务上显著超越大参数量的通用MLLM。
