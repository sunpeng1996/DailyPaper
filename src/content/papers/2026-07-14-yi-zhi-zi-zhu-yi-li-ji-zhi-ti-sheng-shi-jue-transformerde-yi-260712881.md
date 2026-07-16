---
title: 'Inhibited Self-Attention: Sharpening Focus in Vision Transformers'
title_zh: 抑制自注意力机制：提升视觉Transformer的注意力聚焦能力
authors:
- Peter R. D. van der Wal
- Nicola Strisciuglio
- George Azzopardi
affiliations:
- University of Groningen
- University of Twente
- Stellenbosch University
- University of Malta
arxiv_id: '2607.12881'
url: https://arxiv.org/abs/2607.12881
pdf_url: https://arxiv.org/pdf/2607.12881
published: '2026-07-14'
collected: '2026-07-16'
category: Other
direction: 视觉Transformer · 自注意力机制优化
tags:
- Vision Transformer
- Self-Attention
- Inhibitory Mechanism
- Feature Selection
- Out-of-Distribution Generalization
one_liner: 受生物视觉抑制机制启发，提出保留负注意力得分的ISA，提升ViT特征选择性与分布外泛化能力
practical_value: '- 多模态电商推荐/广告的ViT特征提取模块可替换ISA，抑制商品图背景噪音，提升物品特征表征准确性

  - 搜索场景商品图识别、违规内容检测任务引入ISA，降低背景干扰带来的识别错误，提升模型鲁棒性

  - 负注意力得分的设计思路可迁移到推荐系统注意力模块，用负权重抑制无关用户行为/物品特征干扰'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
ViT的自注意力机制常将权重分散在背景区域，依赖虚假相关性而非目标对象相关线索，导致特征选择性差、鲁棒性不足，分布外场景表现不佳。
### 方法关键点
受生物视觉系统的抑制机制启发，抑制自注意力（ISA）打破常规自注意力经softmax归一化后仅输出正注意力值的限制，保留并利用负注意力得分抑制无关特征，强化对目标对象区域的注意力聚焦。
### 关键结果
在ImageNet-1k、COCO等数据集及多个鲁棒性基准测试中，ISA有效增强了对象中心选择性，降低了模型对捷径特征的依赖，显著提升分布外泛化能力；相关性热力图验证，搭载ISA的ViT注意力更集中在目标对象区域，背景特征干扰大幅降低。
