---
title: A Full-Ledger Counterfactual Audit of Adaptive Reasoning
title_zh: 自适应推理的全账本反事实审计框架FLCVA
authors:
- Xiaopeng Chu
- Wenzheng Kong
- Wei Liu
- Wenyi Zhang
affiliations:
- University of Science and Technology of China
arxiv_id: '2611.22778'
url: https://arxiv.org/abs/2611.22778
pdf_url: https://arxiv.org/pdf/2611.22778
published: '2026-11-17'
collected: '2026-11-18'
category: Reasoning
direction: LLM自适应推理 · 计算分配价值审计
tags:
- Adaptive Reasoning
- Counterfactual Evaluation
- LLM Inference
- Compute Allocation
- FLCVA
one_liner: 提出全账本反事实审计框架FLCVA，量化LLM自适应推理的计算投入产出价值
practical_value: '- 落地LLM导购Agent、生成式推荐文案场景时，可先上线「当前答案置信度」基线策略：仅给置信度低于阈值的请求分配额外推理计算，该简单策略可覆盖80%以上的自适应推理收益

  - 评估任何推理增强方案（多步思考、多采样重排、PRM打分等）的业务价值时，必须计入所有信号采集、额外推理的token/FLOP成本，避免实验室指标好看但线上成本超支

  - 设计自适应停止逻辑时，可加入「历史答案一致性（Persistence）」特征：连续多次返回相同的正确答案时直接停止推理，避免过度推理把原本正确的结果改坏'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM自适应推理方法大多仅能识别当前答案是否错误，但无法判断追加计算是否真的能修复错误，也没有统一框架量化推理投入的实际ROI，导致很多策略只关注精度提升而忽略成本，落地性价比极低。
### 方法关键点
- 提出全账本反事实审计框架FLCVA：固定已生成的推理前缀，对比立即回答与4条等长（默认256token）续推分支的结果差异，除以总推理成本，得到每千token的正确性变化率作为推理价值核心指标
- 拆解三大评估维度：续推价值的离线测量、可观测信号对续推价值的预测能力、基于预测的在线计算分配效果
- 采用全成本核算规则：所有信号采集（如PRM打分、多路径采样）的token/FLOP开销全部计入总预算，避免高估策略价值
### 关键实验
在GSM8K、MATH-500数据集上测试3款开源模型：
- 256token续推可修复26.6%的Qwen3-8B错误答案、18.9%的DeepSeek-R1-7B错误答案，仅损坏1.4%/1.9%的正确答案
- 仅用「当前答案是否错误」的简单分配策略，就比轮询分配提升1.78%（Qwen3）/1.55%（DeepSeek）的精度-成本曲线AUC，现有轻量复杂策略在此基础上几乎无额外增益
### 核心结论
自适应推理的大部分收益来自识别并给错误答案分配更多计算，复杂续推价值预测策略如果不能覆盖自身信号成本，性价比反而不如简单基线
