---
title: 'F$^2$Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading'
title_zh: F²Agent：面向多模态交易的智能体金融融合框架
authors:
- Changshuo Liu
- Yanzheng Jin
- Shangfeng Cai
- Peng Fang
- Xiaokui Xiao
- Beng Chin Ooi
affiliations:
- National University of Singapore
- Huazhong University of Science and Technology
- Zhejiang University
arxiv_id: '2608.05668'
url: https://arxiv.org/abs/2608.05668
pdf_url: https://arxiv.org/pdf/2608.05668
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 多模态Agent 跨模态融合决策
tags:
- Multimodal Agent
- Cross-modal Fusion
- Consistency Regularization
- Decision Making
- Noise Robustness
one_liner: 提出分层专能智能体+模态感知自适应融合的多模态交易框架，平均年化收益相对提升超20%
practical_value: '- 多模态信号处理可复用分层专能智能体架构，先按模态拆分特征提取任务再融合，降低跨模态建模复杂度

  - 模态感知自适应融合机制可迁移至多模态推荐/广告选品场景，动态加权不同模态信号权重适配业务目标

  - 噪声鲁棒一致性正则化方法可用于提升用户行为/内容等含噪输入下的模型稳定性，降低业务效果波动'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
金融交易场景多模态异质信息来源复杂，现有LLM Agent存在跨模态依赖捕捉不足、抗市场噪声能力弱的问题，难以支撑高质量交易决策。
### 方法关键点
1. 设计分层专能智能体架构，分模态独立提取专属特征信号；
2. 提出模态感知自适应融合机制，动态捕捉细粒度跨模态依赖；
3. 加入噪声鲁棒一致性正则化，提升输出信号抗噪性。
### 关键结果
在6支股票及加密资产数据集上，相对16个SOTA基线平均年化收益提升超20%；在GOOG、TSLA标的上分别实现120.48%、148.41%的累计收益，适配不同市场波动场景。
