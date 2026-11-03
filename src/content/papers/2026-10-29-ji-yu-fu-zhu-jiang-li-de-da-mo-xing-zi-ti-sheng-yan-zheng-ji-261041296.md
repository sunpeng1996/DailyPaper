---
title: 'Self-Improvement with Auxiliary Rewards: Learning from Verified Traces and
  Evaluating Transfer'
title_zh: 基于辅助奖励的大模型自提升：验证轨迹学习与迁移效果评估
authors:
- Minju Gwak
- Alan Ritter
affiliations:
- Georgia Institute of Technology
arxiv_id: '2610.41296'
url: https://arxiv.org/abs/2610.41296
pdf_url: https://arxiv.org/pdf/2610.41296
published: '2026-10-29'
collected: '2026-11-03'
category: Training
direction: 小模型自提升 · 辅助奖励设计
tags:
- Auxiliary Reward
- Self-Improvement
- LLM Reasoning
- DPO
- SFT
- Test-Time Adaptation
one_liner: 提出两类辅助轨迹奖励，在仅答案级监督下提升小模型自提升效果与跨任务迁移能力
practical_value: '- 业务场景仅有最终结果对错标注时，可直接复用SC/UID-Conj两个无标注成本的辅助信号，区分相同结果的轨迹质量，挖掘现有训练样本的额外价值

  - 优化垂类小模型（如电商客服、推荐理由生成、导购Agent）时，用辅助分数加权SFT/构造DPO偏好对，无需额外标注即可提升模型推理质量与跨场景迁移性

  - 做测试时领域适配（如大促场景临时适配新的推荐话术规范）时，用辅助奖励增强TTRL，可缓解原生TTRL容易过拟合适配集的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有仅基于最终答案正确性的奖励信号，无法区分结果正确但推理逻辑、冗余度差异显著的轨迹，在标注资源有限的场景下浪费了大量已生成正确响应的训练价值，导致小模型自提升效果差、跨任务迁移能力弱。
### 方法关键点
- 设计两类完全无额外标注成本的辅助轨迹奖励：Self-Certainty（SC，基于模型预测置信度，偏好推理确定性高的轨迹）、UID-Conj（结合全局熵波动与局部平滑性，偏好信息密度合理、无冗余的轨迹）
- 适配三类主流训练范式：在线TTRL中给多数一致的正确轨迹叠加辅助奖励调整、离线DPO中用辅助分数构造正确轨迹的偏好对、离线SFT中用辅助分数给正确样本动态加权
- 所有辅助分数仅从模型自身预测的token分布计算，无需额外标注或训练独立Reward Model
### 关键结果
以Qwen3-1.7B为基线，仅用30条无参考答案的AIME数学题做在线适配：UID-Conj增强的TTRL相比原生TTRL，跨4个推理基准的macro准确率提升2.08pp；离线训练中，UID-Conj加权SFT相比均匀加权SFT，macro准确率提升1.93pp，95%置信区间为[0.44, 3.44]；无需任务特定训练即可迁移到CriticBench错误检测任务，准确率提升1.24pp、错误类F1提升1.58pp。

相同正确结果的轨迹训练价值存在显著差异，无需额外标注的模型内部预测统计信号即可挖掘这部分价值，且训练收益与人工判定的轨迹质量不一定完全一致，应以最终下游任务收益为评估标准。
