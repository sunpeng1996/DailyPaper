---
title: 'First Things First: Teaching LLM-Based Agents to Prioritize Must-Haves before
  Nice-to-Haves'
title_zh: 让LLM Agent优先满足必选需求：需求感知推理优化框架
authors:
- Tianjie Ju
- Xinyue Xu
- Wanxuan Sun
- Lingxiao Diao
- Gongshen Liu
- Zhuosheng Zhang
- Cheng Yang
affiliations:
- Shanghai Jiao Tong University
- ByteDance
arxiv_id: '2609.05224'
url: https://arxiv.org/abs/2609.05224
pdf_url: https://arxiv.org/pdf/2609.05224
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: Agent 需求感知推理能力优化
tags:
- MLLM
- Agent
- Reinforcement Learning
- Requirement Understanding
- Benchmark
one_liner: 提出需求优先级推理基准FTF-BENCH与多目标RL框架FTF-RL，提升MLLM Agent服务场景任务准确率
practical_value: '- 电商导购/客服Agent可直接复用需求分层逻辑：先识别用户请求中的必选需求（如预算、尺码）做初筛，再用可选需求（如颜色、赠品）做排序，降低无效推荐率

  - 可复用FTF-RL的多目标奖励设计：在SFT基础上叠加「需求分类准确率、格式合规、结果正确性」三类可验证奖励，不用复杂RLHF就能快速提升Agent任务完成率

  - 电商个性化推荐场景可借鉴需求优先级建模思路：将用户硬约束（如不买特定品牌、价格区间）和软偏好（如倾向新品）解耦，避免因过度拟合软偏好违反硬约束导致用户流失'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
当前MLLM Agent在电商导购、酒店预订、打车等真实服务场景处理用户多维度需求时，普遍存在必选/可选需求混淆问题：要么违反硬约束（如用户要非吸烟房，返回带早餐的吸烟房），要么把可选需求升级为必选导致无结果返回，现有基准未覆盖这类需求优先级推理场景，亟需针对性评估和优化方案。

### 方法关键点
- 构建FTF-BENCH基准：覆盖电商、预订、地图/打车3类场景共3649个样本，分为三类任务：单答案（必选需求唯一命中）、多答案（必选命中后用可选排序）、无答案（无符合必选需求需拒答）
- 提出FTF-RL多目标强化学习框架：设置三类可验证奖励：格式奖励（输出符合<requirements>/<think>/<answer>结构化格式）、答案准确率奖励（与ground truth语义一致）、需求分类奖励（必选/可选分类的Macro-F1），采用GRPO算法优化
- 基准采用LLM生成+人工校验的构建流程，将结构化需求转成口语化用户请求，真实还原用户表达习惯

### 关键实验结果
- 对比Gemini 2.5 Pro、GPT-5、Qwen2.5-VL等主流MLLM，闭源模型直接处理口语化请求时平均准确率最高仅81.75%（Gemini 2.5 Pro），开源模型平均准确率普遍低于60%
- FTF-RL训练后，Qwen2.5-VL 7B在FTF-BENCH上平均准确率提升16.02%，多答案场景提升达26.38%，同时在LogicVista、MathVision等通用推理基准上也有1~7%的稳定提升
- 给模型输入gold需求标签作为上限时，准确率平均提升3~20%，证明需求识别错误是主要性能瓶颈

### 最值得记住的一句话
MLLM Agent在服务场景的核心瓶颈不是感知或推理能力不足，而是无法正确区分用户需求的优先级，仅优化需求分类就能带来大幅性能提升
