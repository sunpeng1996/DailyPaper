---
title: Retrosynthesis of Synthetic Media for Explainable AI Provenance Forensics
title_zh: 面向可解释AI来源取证的合成媒体逆合成方法
authors:
- Yijie Lin
- Ching-Chun Chang
- Isao Echizen
- Hui Li
- Chin-Chen Chang
arxiv_id: '2609.02268'
url: https://arxiv.org/abs/2609.02268
pdf_url: https://arxiv.org/pdf/2609.02268
published: '2026-09-02'
collected: '2026-09-06'
category: Other
direction: 生成式AI内容可解释溯源取证
tags:
- Generative AI Forensics
- Content Provenance
- Self-embedding
- Round-trip Verification
- Explainable AI
one_liner: 在不改动生成器架构参数前提下，提出自引用逆合成框架实现可解释生成内容来源取证
practical_value: '- 电商AIGC商品图、营销素材溯源可复用该框架，无需改动现有生成模型架构，避免水印损伤内容视觉质量

  - 生成式推荐/广告场景的内容合规校验可借鉴往返一致性校验逻辑，无需嵌入额外标记即可快速判定内容是否来自自有生成系统

  - AIGC权属纠纷场景可复用该自编码-解码校验思路，输出可解释的来源判定证据，降低举证成本'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
MLaaS平台生成式服务快速普及，现有合成媒体来源追溯方案要么需要修改生成器架构参数，要么需要嵌入水印影响生成内容质量，无侵入式的可解释溯源是核心痛点。
### 方法关键点
提出固定生成器场景下的自引用逆合成取证框架，联合优化编码器-解码器对实现自嵌入机制，支持往返一致性校验：推理时先编码用户输入再送入生成器得到高保真输出，取证时比对重合成图像与查询图像的一致性判定来源，全程无需修改生成器、无需嵌入水印。
### 关键结果
编码输入生成的图像视觉质量与原生成器原生输出持平，解码追溯输入的匹配准确率可靠，可输出可解释的来源判定依据，满足实用级取证需求。
