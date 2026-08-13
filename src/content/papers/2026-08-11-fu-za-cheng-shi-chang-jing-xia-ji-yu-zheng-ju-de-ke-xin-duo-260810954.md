---
title: Evidence-Grounded Trustworthy Multimodal Reasoning and Evaluation Benchmark
  in Complex Urban Scenes
title_zh: 复杂城市场景下基于证据的可信多模态推理与评估基准
authors:
- Zhaoyang Wei
- Bowen Jiang
- Xumeng Han
- Jiashu Li
- Xuehui Yu
- Yuling Liu
- Guorong Li
- Zhenjun Han
- Jianbin Jiao
affiliations:
- University of Chinese Academy of Sciences
- Tencent CDG
- Institute of Information Engineering, CAS
arxiv_id: '2608.10954'
url: https://arxiv.org/abs/2608.10954
pdf_url: https://arxiv.org/pdf/2608.10954
published: '2026-08-11'
collected: '2026-08-12'
category: Multimodal
direction: 多模态大模型 · 可信推理
tags:
- MLLM
- Multimodal Reasoning
- Visual Grounding
- Benchmark
- Chain of Evidence
one_liner: 提出AD2-Bench多模态推理评估基准与EGVOR推理框架，解决复杂场景下感知与推理脱节问题
practical_value: '- 电商多模态推荐/广告场景下，针对低质模糊商品图、嘈杂背景场景图的推理优化，可借鉴EGVOR的显式空间-语义三元组证据链思路，减少感知理解错误

  - 多模态Agent决策可解释性优化，可复用Chain of Evidence分层拆解推理过程的方法，快速定位推理链路的故障点

  - 多模态模型效果评估可参考AD2-Bench的细粒度诊断框架，从仅评估最终结果升级为覆盖感知-推理全链路的效果校验'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
MLLM在复杂恶劣场景下认知可靠性骤降，普遍采用无充分视觉证据的隐式推理，导致感知与推理链路脱节；现有面向结果的评估基准无法诊断底层推理过程的故障点。
### 方法关键点
1. 提出AD2-Bench评估基准，引入分层视觉诊断框架，将推理拆解为结构化Chain of Evidence（CoE），定位出推理失败的两大核心原因：空间歧义（目标定位错误）、语义不确定性（特征退化导致的语义理解错误）。
2. 提出Evidence-grounded Visual Reasoning（EGVOR）框架，将隐式推理替换为显式Evidence Atoms（结构化空间-语义三元组）生成，强制定位与语义理解严格对齐；采用分层课程训练策略，从反射监督构建过渡到显式奖励降低推理方差的强化学习阶段。
### 关键结果
实验证明EGVOR大幅提升恶劣条件下的推理稳定性，为可信多模态认知提供了更鲁棒的实现框架
