---
title: 'The Illusion of Visual Tool-Use: A Causal Audit of Thinking with Images'
title_zh: 视觉工具使用的假象：多模态大模型图像推理的因果审计
authors:
- Zhiheng Wang
- Bo Peng
- Lai Wei
- Chaochao Lu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
arxiv_id: '2608.06270'
url: https://arxiv.org/abs/2608.06270
pdf_url: https://arxiv.org/pdf/2608.06270
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 多模态Agent · 视觉工具调用校准
tags:
- Multimodal LLM
- Tool Use
- Causal Inference
- Agent Calibration
- Visual Reasoning
one_liner: 通过三级因果干预拆解多模态模型视觉工具调用的真实增益，揭露两种校准失效模式
practical_value: '- 搭建商品/广告多模态理解Agent时，不要盲目叠加裁剪放大类视觉工具，可先通过轨迹级干预（替换返回的裁剪图为随机同尺寸图）测试工具是否真的带来有效增益，避免浪费token成本

  - 工具调用策略优化可借鉴Visual Evidence Gain（VEG）指标做细粒度监督，给真正带来信息增益的工具调用正反馈，惩罚“为了调用而调用”的冗余操作，比仅看最终结果的RL效果更优

  - 多模态Agent推理可增加预调用置信度判断，当模型对答案的置信度超过0.95阈值时直接返回结果，停止后续工具调用，减少无用开销，避免越调用越错的问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前多模态大模型“边思考边调用图像工具（如裁剪放大）”的范式普遍存在增益边际甚至为负、token成本极高的问题，且经常出现直接推理能答对、调用工具后反而答错的情况，现有研究无法明确工具返回的视觉证据是否真的对答案产生因果影响，亟需定量拆解工具调用的真实价值。

### 方法关键点
- 构建视觉工具调用的因果图，区分三类路径：不调用工具的直接路径、视觉证据介导的有效路径、仅工具调用动作本身影响答案的捷径路径
- 设计三级因果干预方案：①策略级：对比直接推理和工具调用的准确率差异；②轨迹级：运行时替换所有工具返回的观测为随机裁剪图，测试总增益；③步骤级：用反事实替换单步观测，提出Visual Evidence Gain（VEG）指标，量化单步工具返回视觉信息的真实贡献
- 提出轨迹级诊断方法，将工具调用轨迹分为四类：无调用、调用却不看（CWL，观测无因果贡献）、看了却无规划（LWP，观测有效但调用时序混乱）、校准有效

### 关键实验
在6个主流视觉工具调用模型、5个细粒度感知基准上测试，发现：①仅10%-45%的工具调用轨迹属于校准有效组，贡献了全部的策略级准确率增益；②高达34%-73%的调用属于“调用却不看”，工具返回的信息完全不影响最终答案；③最优模型的冗余调用率可达17.8%，大量调用发生在模型置信度已经足够的阶段。

### 核心结论
拥有工具不代表会正确使用工具，评价视觉工具调用能力的核心不是“是否调用工具”，而是“工具返回的证据是否真的因果性影响了最终答案”。
