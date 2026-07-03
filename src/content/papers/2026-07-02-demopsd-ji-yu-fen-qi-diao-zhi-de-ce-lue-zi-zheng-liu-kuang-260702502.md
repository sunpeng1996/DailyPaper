---
title: 'DemoPSD: Disagreement-Modulated Policy Self-Distillation'
title_zh: DemoPSD：基于分歧调制的策略自蒸馏框架
authors:
- Yunhe Li
- Hao Shi
- Wenhao Liu
- Mengzhe Ruan
- Hanxu Hou
- Zhongxiang Dai
- Shuang Qiu
- Linqi Song
affiliations:
- City University of Hong Kong
- Tsinghua University
- Shenzhen University of Advanced Technology
- Chinese University of Hong Kong, Shenzhen
arxiv_id: '2607.02502'
url: https://arxiv.org/abs/2607.02502
pdf_url: https://arxiv.org/pdf/2607.02502
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: LLM训练 · 策略自蒸馏优化
tags:
- Self-Distillation
- Policy Optimization
- Privileged Information Leakage
- LLM Reasoning
- On-Policy Training
one_liner: 基于师生分布分歧自适应调制自蒸馏目标，缓解特权信息泄露并保留模型探索能力
practical_value: '- 业务LLM自蒸馏场景（如Agent推理、生成式推荐prompt蒸馏）可复用分歧调制思路：用师生输出分布JSD计算衰减系数，高分歧位置降低蒸馏权重，避免过拟合仅训练时可用的特权信息

  - 蒸馏目标优先选reverse-KL barycenter几何混合而非算术混合，既能保留双方共识的高置信信号，又避免模间平均导致的目标模糊，适合文案生成、Query推荐等对输出一致性要求高的场景

  - 自蒸馏训练时可复用稳定trick：仅处理含至少1个正确rollout的prompt组，用EMA版本学生模型作为参考计算分歧与目标，避免训练振荡，可直接迁移到业务LLM的RLHF后精调阶段'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有On-policy自蒸馏（OPSD）用带特权信息的同一模型做教师，可将稀疏奖励转化为稠密token级监督，大幅提升训练效率，但存在两大痛点：一是特权信息泄露，学生学到测试时不可用的答案依赖捷径；二是强制拟合教师分布会压制探索，导致熵塌陷、跨域泛化能力下降。现有方法多依赖教师熵、样本正确率等间接代理控制蒸馏，无法直接衡量特权信息对教师输出的影响。
### 方法关键点
- 逐token计算师生分布的JSD分歧，分歧越大说明教师输出受特权信息影响越强，对应生成单调递增的泄漏衰减系数αt，控制蒸馏目标向学生分布偏移的程度
- 蒸馏目标采用reverse-KL barycenter几何混合形式：$π_{target} \propto (π_{teacher})^{1-α_t} \cdot (π_{student})^{α_t}$，避免算术混合的模平均问题，仅保留师生共识的高置信信号
- 训练时仅保留至少含1个正确rollout的prompt组，用正确rollout作为特权信息注入教师上下文，采用EMA版本学生模型作为参考计算分歧与目标，避免梯度振荡
### 关键结果
在SciKnowEval四个科学领域数据集上，相比SDPO基线，平均mean@16提升1.68%、best@16提升2.82%，训练熵高出35%~98%；在OOD基准GPQA上平均准确率高出7.91%，无SDPO的后期性能下降问题。
> 最值得记住的结论：自蒸馏不是要让学生完全复刻教师，而是选择性吸收教师的可迁移知识，同时保留学生独立推理的探索能力
