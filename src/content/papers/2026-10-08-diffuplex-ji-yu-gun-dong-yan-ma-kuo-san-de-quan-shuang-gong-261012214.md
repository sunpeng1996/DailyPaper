---
title: 'DiffuPlex: Accelerating Full-Duplex Spoken Dialog Models via Rolling Masked
  Diffusion'
title_zh: DiffuPlex：基于滚动掩码扩散的全双工语音对话模型加速方法
authors:
- Heeseung Kim
affiliations:
- University of Seoul
arxiv_id: '2610.12214'
url: https://arxiv.org/abs/2610.12214
pdf_url: https://arxiv.org/pdf/2610.12214
published: '2026-10-08'
collected: '2026-10-10'
category: LLM
direction: 全双工语音对话 · LLM推理加速
tags:
- Diffusion Model
- LLM Inference
- Spoken Dialog
- Full-Duplex
- Speed Optimization
one_liner: 基于滚动掩码扩散一次预测多帧对话，实现全双工语音对话模型推理大幅加速
practical_value: '- 电商语音客服、语音导购类Agent可复用滚动预测+置信前缀截断策略，在不损失交互质量的前提下降低推理延迟

  - 实时交互场景可借鉴分场景推理调度逻辑，区分静默/发声场景匹配不同策略，平衡加速比与用户体验

  - 多帧预测+冲突时仅修正未输出内容的思路可迁移到实时直播口播文案生成、实时语音推荐等低延迟场景'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前全双工语音对话模型需逐帧自回归调用骨干模型，推理延迟高，无法满足实时交互的低耗时要求。
### 方法关键点
1. 提出滚动掩码扩散框架DiffuPlex，单次骨干模型唤醒即可预测多帧未来用户与助理对话帧，仅输出置信度达标的前缀部分，保持原帧率交互
2. 实时校验到达的用户语音与预测值的偏差，交互偏离时保留已播放的助理内容，仅修正未播放的未来帧
3. 配套两种推理策略：LISTEN仅在预测助理静默时批量消费多帧，SPEAK可同时消费预测的助理语音帧
### 关键结果
LISTEN、SPEAK分别实现1.46×、1.59×部署路径端到端提速，1.61×、1.80×核心LM提速，所有骨干调用耗时均低于80ms交互阈值；人工评估显示LISTEN完全保留语音自然度与对话质量，SPEAK仅轻微降低自然度，对话质量无损失。
