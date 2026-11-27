---
title: 'PoVi: Agentic Poetry-to-Video Generation with Knowledge Grounding and Figurative
  Understanding'
title_zh: PoVi：知识落地与修辞理解驱动的智能体诗歌转视频基准及框架
authors:
- Yuxia Zhu
- Shiying Zhang
- Lingzhuang Sun
- Song Yang
- Siheng Wu
- Xinglong Xu
- Sizhe Qiu
- Hao Liang
- Cheng Tan
- Asher Qin
affiliations:
- Peking University
- University of Chinese Academy of Sciences
- Tongji University
- Tencent
arxiv_id: '2611.34690'
url: https://arxiv.org/abs/2611.34690
pdf_url: https://arxiv.org/pdf/2611.34690
published: '2026-11-25'
collected: '2026-11-27'
category: Agent
direction: Agent 知识驱动多模态内容生成
tags:
- Agent
- Knowledge Grounding
- Multimodal Generation
- Text-to-Video
- Benchmark
one_liner: 提出具备Knowledge Grounding与修辞理解的智能体式诗歌转视频生成框架与评测基准
practical_value: '- 处理高度压缩的隐含语义（如电商短文案、用户模糊搜索Query）时，可复用「先重构为带证据边界的语义表示→分层拆解为多模块可执行计划→下游生成」的Agent流水线，解决隐式知识、修辞类内容的生成失真问题

  - 多模态内容生成任务（如商品短视频生成、营销素材生成）中，可复用分层规划对齐思路：先完成文案、资产、分镜的前置规划，再对齐生成最终内容，大幅提升长序列多片段生成的一致性

  - 涉及文化、领域知识的生成任务（如国潮电商内容、IP衍生内容），可参考PoVi的Knowledge Grounding评测维度，优化生成内容的事实准确性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有文本转视频生成方案默认输入是明确的视觉需求描述，无法处理诗歌这类高度压缩、依赖文化背景、大量使用修辞暗喻的文本，生成内容常出现语义不符、常识错误问题。
### 方法关键点
提出PoVi评测基准与Agent框架，首先将诗歌语义重构为带证据边界的表示，再渐进式转换为旁白、语义解读、角色资产、镜头级视觉规划，最终生成与旁白对齐的视频，评测维度覆盖semantic grounding、上下文连贯性、音视频实现效果。
### 关键结果
在3种规划backbone、4种视频生成器上测试，效果持续优于单轮调用生成方案，对隐含背景知识、隐喻关系相关场景的生成效果提升幅度最大。
