---
title: 'Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation'
title_zh: 蒸馏检测：通过Cartridge蒸馏暴露大语言模型中的隐蔽偏好偏差
authors:
- Shayan Talaei
- Abhinav Chinta
- Devvrit Khatri
- Amin Karbasi
- Azalia Mirhoseini
- Amin Saberi
affiliations:
- Stanford University
- University of Texas at Austin
- Foundation AI–Cisco Systems Inc.
arxiv_id: '2607.01208'
url: https://arxiv.org/abs/2607.01208
pdf_url: https://arxiv.org/pdf/2607.01208
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: LLM安全审计 · 隐蔽偏差检测
tags:
- LLM Bias
- KV Cache
- Prefix Tuning
- Model Auditing
- Distribution Shift
one_liner: 提出基于KV-cache前缀适配器的D2D方法，无需已知偏差主题即可检测LLM隐蔽偏好偏差
practical_value: '- 可复用D2D的分布偏移蒸馏思路，审计电商导购Agent、生成式推荐场景下的LLM是否存在品牌、品类的隐蔽偏好偏差，规避合规风险

  - KV-cache前缀适配器的偏差信号放大方法可直接落地，无需读取模型权重，仅通过生成文本即可完成离线检测，工程实现成本极低

  - 针对第三方提供的微调LLM服务，可先用D2D做前置校验，避免接入植入性偏好偏差的模型导致业务导流不公、损害用户信任'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
高风险场景部署的LLM常存在仅特定主题触发的隐蔽偏好偏差，这类偏差可通过无关数据蒸馏植入，未知偏差主题时，检查生成文本、内部表征或权重都无法有效检出，是LLM落地的核心安全盲区。
### 方法关键点
将待检测模型与基座模型的logit分布偏移蒸馏到名为cartridge的KV-cache前缀适配器中，利用前缀调谐的容量瓶颈浓缩主导分布差异，将偏差信号放大到生成文本中可被直接观测的程度；配套基于Fisher加权投影的理论框架解释方法有效性。
### 关键结果
跨品牌、实体、观点等多类偏差场景测试，均可实现稳定可靠的隐蔽偏差检出，信号放大后仅通过通用文本检测工具即可完成LLM行为审计。
