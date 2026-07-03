---
title: Towards Robustness against Typographic Attack with Training-free Concept Localization
title_zh: 面向排版攻击鲁棒性的免训练概念定位方法
authors:
- Bohan Liu
- Wenqian Ye
- Guangzhi Xiong
- Zhenghao He
- Sanchit Sinha
- Aidong Zhang
affiliations:
- University of Virginia
arxiv_id: '2607.02494'
url: https://arxiv.org/abs/2607.02494
pdf_url: https://arxiv.org/pdf/2607.02494
published: '2026-07-02'
collected: '2026-07-03'
category: Multimodal
direction: 多模态模型 · 排版攻击鲁棒性优化
tags:
- CLIP
- LVLM
- Typographic Attack
- Mechanistic Interpretability
- Vision Transformer
one_liner: 提出免训练多模态排版攻击防御方案，定位ViT词汇编码组件做干预提升鲁棒性
practical_value: '- 多模态商品检索/内容推荐场景，可复用该方法定位CLIP中受商品图水印、内嵌营销文字干扰的注意力头，调整权重降低误判，无需重训即可提升召回/排序准确率

  - 多模态Agent处理用户上传的商品截图、聊天配图等含文字的视觉输入时，可集成该免训练干预逻辑，提升输入理解鲁棒性，减少理解偏差导致的应答错误

  - LVLM驱动的商品视觉问答、文案生成场景，可直接套用该方法修改ViT编码器，低成本提升抗图内无关文字干扰的效果，减少bad case'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
CLIP是当前绝大多数LVLM的核心视觉编码器，存在严重未被充分研究的排版攻击漏洞：图像内的无关文本会误导视觉表征偏向词汇语义，而非真实视觉语义，给多模态交互、内容识别等高可靠性要求场景带来风险，现有防御方法要么需要重训成本高，要么效果不佳。
### 方法关键点
1. 提出免训练的机制可解释性方案，基于采样分析隐层表征，量化单个注意力头对语义/词汇信息的关注权重；
2. 通过概率分析与电路挖掘，定位ViT中过度编码词汇信息的组件，明确排版攻击的机制来源；
3. 对定位到的电路直接做注意力权重选择性调整等轻量干预，无需额外训练即可实现防御。
### 关键结果
- 目标分类任务上，效果优于所有现有监督及免训练防御方法；
- RIO-Bench数据集排版攻击场景下，多个SOTA LVLM的视觉问答准确率获显著提升，方案通用性强。
