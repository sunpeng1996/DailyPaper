---
title: Text Template Tokens Are Implicit Semantic Registers in Diffusion Transformers
title_zh: 扩散Transformer中的文本模板令牌是隐式语义寄存器
authors:
- Maohua Li
- Qirui Li
- Yanke Zhou
- Yiduo Li
- Zhaosheng Chi
- Chao Xu
- Cuifeng Shen
- Yixuan Xu
- Hanlin Tang
- Kan Liu
affiliations:
- Nanjing University
- Alibaba Group
- Zhejiang University
arxiv_id: '2607.19139'
url: https://arxiv.org/abs/2607.19139
pdf_url: https://arxiv.org/pdf/2607.19139
published: '2026-07-20'
collected: '2026-07-22'
category: Multimodal
direction: 多模态大模型可解释与推理优化
tags:
- Diffusion Transformer
- Interpretability
- Attention Pruning
- Text-to-Image
- Semantic Register
one_liner: 提出DiT因果可解释框架，发现模板令牌为隐式语义寄存器，实现无训练剪枝降20%注意力算力
practical_value: '- 电商商品图生成场景可复用该无训练剪枝规则，裁剪DiT中对prompt注意力高的头，降20%推理算力仅损失极少量生成质量

  - 多模态生成类Agent的DiT模块优化可参考该结论，优先保障语义寄存器相关注意力头，降低生成内容的一致性偏差

  - 可借鉴该因果可解释框架分析推荐/广告场景的多模态Transformer模块，定位冗余计算单元降低推理延迟'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文生图Diffusion Transformer（DiT）去噪过程内部计算机制不透明，缺乏可解释的因果分析框架支撑推理性能优化。
### 方法关键点
1. 提出融合注意力分解与跨令牌段、头、层定向干预的DiT因果可解释框架，区分prompt内容令牌与结构模板令牌
2. 发现结构模板令牌是DiT内部的隐式语义寄存器，语义先注入图像隐空间再回写至模板令牌，而非直接从prompt令牌传递
3. 基于上述结论设计无训练剪枝规则，裁剪对prompt令牌注意力最强的冗余注意力头
### 关键结果
剪枝后降低20%注意力FLOPs，仅在GenEval指标上下降1.4分；同时揭示DiT计算分层组织规律：语义路由与视觉合成分离，生成过程从身份形成到传播再到精细化迭代。
