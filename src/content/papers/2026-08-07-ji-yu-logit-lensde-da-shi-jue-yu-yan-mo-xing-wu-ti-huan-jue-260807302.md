---
title: 'Same Attention, Different Truths: Put Logit-Lens over Visual Attention to
  Detect and Mitigate LVLM Object Hallucination'
title_zh: 基于Logit Lens的大视觉语言模型物体幻觉检测与缓解方法
authors:
- Zichuan Wang
- Songlin Yang
- Bo Peng
- Zhenchen Tang
- Yang Li
- Beibei Dong
- Jing Dong
affiliations:
- School of Artificial Intelligence, University of Chinese Academy of Sciences
- New Laboratory of Pattern Recognition, Institute of Automation, Chinese Academy
  of Science
- Hong Kong University of Science and Technology
arxiv_id: '2608.07302'
url: https://arxiv.org/abs/2608.07302
pdf_url: https://arxiv.org/pdf/2608.07302
published: '2026-08-07'
collected: '2026-08-10'
category: Multimodal
direction: 多模态大模型 · 幻觉检测与缓解
tags:
- LVLM
- Hallucination Mitigation
- Logit Lens
- Visual Attention
- Training-free
one_liner: 揭示LVLM物体幻觉并非源于注意力强度不足，提出免训练的分场景幻觉检测与缓解框架
practical_value: '- 电商场景用LVLM生成商品文案、做图文理解时，可直接复用Logit Lens一致性检查检测幻觉，避免生成不存在的商品属性/配件，降低客诉

  - 无需重新训练LVLM即可落地幻觉缓解能力：视觉混淆类幻觉用HARM掩蔽高注意力混淆区域，先验类幻觉用VEED引入视觉证据约束解码，落地成本极低

  - 多模态RAG、商品搜推的图文匹配校验环节可复用该方法，过滤图文不匹配的召回结果，提升多模态检索准确率'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
LVLM普遍存在物体幻觉问题，此前研究普遍将其归因于视觉注意力不足，但实验发现真实与幻觉物体在模型中高层的注意力强度无显著差异，核心诱因未被明确。
### 方法关键点
1. 引入Logit Lens解码高注意力区域的视觉特征，发现真实物体对应区域可正确解码为目标token，幻觉物体对应区域无法完成正确解码；
2. 识别两类幻觉机制：视觉不确定性类（语义相似/易混淆区域引发，掩蔽对应区域即可消除幻觉）、上下文先验类（强共现先验引发，掩蔽初始关注区域后注意力会漂移，幻觉仍存在）；
3. 提出免训练的Detect-Mitigate框架：先通过Logit-Lens一致性检查检测幻觉，再分别用HARM处理视觉不确定性类幻觉，用VEED处理上下文先验类幻觉。
### 关键结果
在多个LVLM幻觉评测基准上取得SOTA性能。
