---
title: Direct or Mediated? Task-Dependent Audio Information Routing in Large Audio
  Language Models
title_zh: 直接还是中介？大音频语言模型中任务依赖的音频信息路由机制
authors:
- Yizhou Zhang
- Wangjin Zhou
- Xin Gu
- Yichi Wang
- Wei Tan
- Yi Zhao
- Zhi Gong
- Keisuke Imoto
- Tatsuya Kawahara
affiliations:
- Graduate School of Informatics, Kyoto University, Japan
- WXG, Tencent, China
arxiv_id: '2608.27026'
url: https://arxiv.org/abs/2608.27026
pdf_url: https://arxiv.org/pdf/2608.27026
published: '2026-08-27'
collected: '2026-08-28'
category: Multimodal
direction: 多模态大模型 · 信息路由机制
tags:
- LALM
- Audio Understanding
- Information Routing
- ASR
- AQA
- Attention Mechanism
one_liner: 揭示大音频语言模型任务依赖的信息路由路径，解释拼接音频输入下的跨任务鲁棒性差异
practical_value: '- 开发电商语音导购、语音搜索类Agent时，ASR任务可直接拼接多段用户语音输入，性能衰减可控；AQA类（如基于语音交互的商品咨询）任务需避免直接拼接多段输入，或增加引导prompt强化中介通路的信息提取

  - 优化多模态大模型任务性能时可针对性微调对应通路：ASR优化输出层对音频token的直接注意力，AQA优化中间层prompt的音频信息整合能力

  - 排查多模态大模型badcase时不要仅验证输入编码是否丢失信息，需额外检查下游生成阶段的信息检索瓶颈，即使中后层已存在目标特征，生成阶段也可能无法正确调取'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有大音频语言模型（LALM）大多在单段连贯音频输入场景下评测，多段拼接输入等非典型配置下的性能表现与内部机制尚不明确，实测发现不同任务的鲁棒性存在显著差距。
### 方法关键点
通过分层注意力敲除技术分析LALM解码器的音频信息路由路径，同时探测不同解码层prompt token的任务相关特征可解码性，定位性能差异的根本原因。
### 关键结果
- ASR任务依赖答案token直接检索音频token的直连通路，拼接输入下性能保持稳定；AQA任务依赖音频信息先整合进prompt再被生成调用的中介通路，拼接输入下性能大幅下降
- 即使AQA性能骤降，解码器中后层prompt表征仍保留完整的任务相关音频属性，性能退化本质是生成阶段检索/利用中介信息的下游瓶颈，而非信息丢失
