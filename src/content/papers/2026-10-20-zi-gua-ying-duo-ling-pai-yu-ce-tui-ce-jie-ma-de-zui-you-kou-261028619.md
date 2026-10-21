---
title: 'Adaptive Multi-Token Prediction: How far should we go?'
title_zh: 自适应多令牌预测：推测解码的最优窗口选择方法
authors:
- Emile Anand
- Mohammed Rehan Parwani
- Xinyuan Cao
affiliations:
- Georgia Institute of Technology
arxiv_id: '2610.28619'
url: https://arxiv.org/abs/2610.28619
pdf_url: https://arxiv.org/pdf/2610.28619
published: '2026-10-20'
collected: '2026-10-21'
category: LLM
direction: LLM推理加速 · 多令牌预测优化
tags:
- Multi-token Prediction
- Speculative Decoding
- Inference Acceleration
- Online Learning
- LLM Serving
one_liner: 无需重训练的轻量级多令牌预测窗口控制器，自适应选择推测长度提升LLM解码吞吐量
practical_value: '- 电商/推荐场景的LLM文案生成、Agent实时对话服务可直接集成AMTP，无需微调现有MTP/Medusa模型，即可降低推理延迟、提升单卡吞吐量，削减部署成本

  - 基于speculative decoding的RAG检索、语义召回服务可复用其ε-贪心探索+逆概率加权的在线调优思路，动态调整候选集大小，平衡检索效率与召回准确率

  - 可借鉴acceptance survival指标评估MTP解码可靠性，为不同业务场景（实时客服、批量内容生成）定制差异化的窗口选择策略，兼顾效果与成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多令牌预测（MTP）是LLM推测解码的主流加速方案，但固定推测窗口的模式存在显著缺陷：窗口过长时大量预测令牌被验证环节拒收，浪费算力；窗口过短时无法充分摊销验证成本，加速效果有限。且MTP需要在生成预测前固定窗口，现有自适应窗口方案都需要额外训练模型或修改验证逻辑，落地成本高。
### 方法关键点
- 定义acceptance survival指标，量化不同长度的预测前缀被全部接受的概率，可精确计算每个候选窗口的期望吞吐量
- 设计零训练开销的在线控制器AMTP，每轮推理前基于上下文特征预测各位置的拒绝风险，直接选择当前吞吐量最优的窗口，无需修改原有MTP模型与验证逻辑
- 采用ε-贪心探索+逆概率加权的方法解决短窗口下后续位置反馈缺失的问题，通过在线梯度下降更新风险预测模型，保证学习过程无偏
### 关键实验
在GSM8K、AIME2025推理数据集上，覆盖Qwen3、Llama3.1、Meta MTP等5种draft-target模型配对，对比标准自回归解码、最优固定窗口MTP：AMTP解码速度最高达标准解码的4.1倍，10组实验中有8组效果持平或超过最优固定窗口，吞吐量最高提升10%。
### 核心结论
MTP的最优推测窗口高度依赖上下文，无需微调模型的在线自适应控制能以极低 overhead 带来可直接落地的推理吞吐量提升。
