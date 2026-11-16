---
title: 'VEPO: Mitigating Multilingual Hallucinations in LVLMs via Visual Evidence-guided
  Preference Optimization'
title_zh: VEPO：基于视觉证据引导偏好优化缓解LVLM多语言幻觉
authors:
- Chengpeng Fu
- Xiaocheng Feng
- Wenshuai Huo
- Yichong Huang
- Baohang Li
- Duyu Tang
- Ting Liu
affiliations:
- Harbin Institute of Technology
- Peng Cheng Laboratory
- Zhongguancun Academy
arxiv_id: '2611.18096'
url: https://arxiv.org/abs/2611.18096
pdf_url: https://arxiv.org/pdf/2611.18096
published: '2026-11-13'
collected: '2026-11-16'
category: Multimodal
direction: 多模态大模型 · 幻觉抑制优化
tags:
- LVLM
- Hallucination Mitigation
- Preference Optimization
- Multimodal
- Low-resource Language
one_liner: 提出无需外部模型的视觉证据引导偏好优化方法，降低LVLM低资源语言对象幻觉
practical_value: '- 多模态商品理解、内容审核场景下，可复用基于跨模态注意力定位关键视觉区域的方法，减少低资源语言场景下的识别幻觉

  - 无需额外标注的偏好对构造思路（全图vs关键区域掩码共享正确答案），可迁移到多模态推荐模型的对齐训练，大幅降低标注成本

  - 低资源语言跨模态对齐优化思路，可用于出海电商多语言商品搜索/推荐的多模态模型微调，提升多语言场景下的推荐准确性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
LVLM易出现对象幻觉，输出语义通顺但缺乏视觉依据的内容，该问题在低资源语言场景下更突出：弱跨模态对齐导致模型更依赖语言先验而非图像证据。现有方案存在标注成本高、依赖外部翻译/奖励模型、推理阶段干预易破坏输出语言质量等缺陷。

### 方法关键点
VEPO为训练阶段优化方法，无需外部模型即可将英语侧的可靠视觉对齐能力迁移到其他语言：首先通过英语查询的中间层跨模态注意力定位关键视觉证据，构造共享同一正确答案、证据充分度不同的偏好对（全图 vs 关键区域掩码图），基于偏好对做DPO训练，引导低资源输入优先选择有完整视觉证据支撑的答案。

### 关键结果
在中、法、印地语的多语言POPE、MME基准上幻觉持续降低、感知能力提升，最低资源语言增益最大；验证了证据引导掩码优于随机掩码，可强化问题相关注意力。
