---
title: Long-Horizon Textual World Modeling through Structured Reasoning
title_zh: 基于结构化推理的长时序文本世界建模
authors:
- Fangxin Wang
- Xiang Gao
- Yuguang Yao
- Kaiwen Dong
- Nikash Walia
- Kamalika Das
affiliations:
- University of Illinois Chicago
- Intuit AI Research
arxiv_id: '2610.06637'
url: https://arxiv.org/abs/2610.06637
pdf_url: https://arxiv.org/pdf/2610.06637
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: Agent 长时序文本世界建模优化
tags:
- World_Model
- Long_Horizon_Prediction
- Structured_Reasoning
- Text_Environment
- Agent
one_liner: 提出非递归结构化推理框架，缓解长时序文本世界模型的误差累积问题
practical_value: '- 电商/广告Agent长时序决策建模可复用非递归稀疏状态更新替代递归rollout，减少中间误差累积，适配用户生命周期价值预测、多步营销转化效果建模等长周期场景

  - 训练长时序预测模型时，可复用「终点质量+预测增益+中间状态监督」的混合奖励设计，解决长序列信用分配弱的问题，无需仅依赖终点监督

  - 需可解释性的Agent场景（如电商智能客服、商家运营Agent）可采用显式结构化文本状态（JSON键值对）替代隐式embedding，方便人工校验、规则干预'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长时序文本世界模型的两类主流范式均有缺陷：递归单步rollout会随预测时长放大中间误差，性能衰减严重；直接多步预测仅监督终点结果，信用分配弱，中间状态无显式约束，长时序下易丢失关键信息，无法支撑Agent可靠的长期规划与反事实推理。
### 方法关键点
- 非递归结构化推理框架latent-SR：单轮自回归生成所有动作对应的稀疏状态增量Δ，通过确定性算子合并到初始状态得到各步中间状态，无需递归调用模型，避免误差反馈
- 两阶段训练：先用大模型教师生成符合格式、预测达标的状态与编辑轨迹做蒸馏初始化，再用GRPO做轨迹级强化学习优化
- 混合奖励设计：融合终点预测质量、相对原始历史预测的增益、中间状态预测质量三类信号，解决长序列监督稀疏问题
### 关键结果
在SCIENCEWORLD、JERICHO、CEO-BENCH三个文本交互环境测试，对比递归、直接预测等5类基线：horizon=10时，SCIENCEWORLD上Fact-F1相对提升12.3%，CEO-BENCH上SE-score相对提升9.3%，JERICHO上预测误差下降近30%；是唯一在反事实测试中对未来动作有统计显著敏感性的模型（p<0.001），基线无相关敏感性甚至呈负相关。

**核心结论**：长时序文本世界建模中，显式结构化中间轨迹+非递归更新的范式，比递归拼接单步预测更能抵御误差累积，支撑更可靠的长期推理。
