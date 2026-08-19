---
title: 'Auditing Exposure to Harmful Content on TikTok using Multimodal Language Models:
  A Cross-National, Age-Stratified Study'
title_zh: 基于多模态大模型的TikTok有害内容暴露审计：跨国分年龄研究
authors:
- Hamidreza Saffari
- Francesco Pierri
affiliations:
- Politecnico di Milano
arxiv_id: '2608.17583'
url: https://arxiv.org/abs/2608.17583
pdf_url: https://arxiv.org/pdf/2608.17583
published: '2026-08-18'
collected: '2026-08-19'
category: Multimodal
direction: 多模态LLM · 内容安全审计
tags:
- Multimodal LLM
- Content Moderation
- Short Video
- User Safety
- Cross-national Audit
one_liner: 基于多模态LLM实现低成本跨国分年龄的TikTok有害内容暴露审计，明确不同场景下的有害率差异
practical_value: '- 短视频/内容平台大规模内容标注可采用「视频抽帧+文本字幕」喂给MLLM的方案，Gemini 2.5 Flash成本仅原生视频上传的1/2，性价比极高

  - 做分人群/分地域的推荐内容安全审计时，可采用虚拟账号模拟不同年龄、地域用户行为的方案，低成本获取不同群体的内容曝光数据

  - 关键词搜索后的推荐流有害率远高于被动feed，内容安全防护需重点监控搜索后链路的临时内容分发策略'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
短视频平台年轻用户有害内容暴露问题突出，传统人工标注成本高、跨语言标注一致性差，独立安全审计落地难度大。
### 方法关键点
1. 搭建13/16/19/40岁四个年龄层虚拟账号，在法、意、瑞三国采集36971条TikTok被动推荐feed、关键词搜索后feed的视频数据；
2. 基于300条母语者标注的参考集验证4款MLLM标注效果，选择最优的Gemini 2.5 Flash（输入8帧抽帧+文本字幕）做规模化标注，单调用成本仅原生视频上传的1/2，10%样本总API花费仅50美元。
### 关键结果
1. 关键词搜索后feed有害率达35%~56%，12组国家-年龄组合中有10组是被动feed的1.5~7.5倍，该有害率峰值为临时特征，抹平了法、瑞两国原本的年龄层有害率差异；
2. 被动feed中意大利各年龄层有害率最高，19岁群体达48.6%；
3. 平台自带安全过滤器拒审率仅1.1%，严重漏判最明确的有害内容。
