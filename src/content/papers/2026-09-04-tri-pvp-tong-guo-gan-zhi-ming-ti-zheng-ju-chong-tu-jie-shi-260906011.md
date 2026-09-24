---
title: 'Tri-PvP: Exposing Modality Bias in Omni-Modal Large Language Models through
  Perceptual-Propositional Evidence Conflicts'
title_zh: Tri-PvP：通过感知-命题证据冲突揭示全模态大模型的模态偏差
authors:
- Yen-Ting Piao
- Shu-Yun Chen
- Chin-Hui Chu
- Chun-Wei Chen
- Shih-Yun Shan Kuan
- Hung-yi Lee
- Yun-Nung Chen
affiliations:
- National Taiwan University
- NTU Artificial Intelligence Center of Research Excellence (NTU AI-CoRE)
arxiv_id: '2609.06011'
url: https://arxiv.org/abs/2609.06011
pdf_url: https://arxiv.org/pdf/2609.06011
published: '2026-09-04'
collected: '2026-09-24'
category: Multimodal
direction: 多模态大模型 · 模态偏差评测
tags:
- Omni-modal LLM
- Modality Bias
- Benchmark
- Perceptual Signal
- Propositional Signal
one_liner: 构建8000样本三模态冲突基准Tri-PvP，揭示全模态大模型的模态与证据形式不对称偏差
practical_value: '- 做多模态电商搜推/客服Agent的模态融合时，可参考发现的不对称偏差规则：视觉优先取感知信号、音频优先取命题信号，调整模态融合权重，降低决策错误

  - 开发多模态输入的导购/内容推荐Agent时，可复用Tri-PvP的冲突检测思路，提前校验模型在多模态输入冲突时的输出可靠性，避免错误应答

  - 多模态大模型微调纠偏时，可针对模态偏差在早期层即可被解码的结论，设计中层表示对齐损失，而非仅做表层输出校正，提升纠偏效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
全模态大模型（OLLMs）已实现多模态联合处理并落地，但跨模态冲突场景下的模态偏差研究不足，现有基准混淆单模态内感知信号（如图像、原声）与命题信号（如文字描述、语音断言），无法准确定位偏差来源。

### 方法关键点
构建Tri-PvP基准，包含8000个覆盖视觉、音频、文本的三模态冲突样本，视觉、音频各自设置感知、命题两种证据形式，可解耦模态偏差与证据形式偏差。

### 关键结果
1. 评测5款主流OLLMs，发现绝大多数模型存在稳定的视觉优先偏差；
2. 证据形式偏差存在系统性不对称：模型对视觉模态更偏好感知信号，对音频模态更偏好命题信号；
3. 模态偏差在模型早期表示层即可线性解码，仅采用表层干预策略只能部分缓解偏差，需更深度的纠偏方案。
